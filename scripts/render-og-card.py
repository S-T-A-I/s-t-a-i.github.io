#!/usr/bin/env python3
"""Render the default link-preview (Open Graph) card.

Writes static/img/og-default-v2.png at 2400x1260 -- a 1200x630 layout drawn at
deviceScaleFactor 2, which is the 2:1 ratio every preview surface expects.

Why a script and not a hand-made PNG: the card carries live text from
config.toml, and every earlier revision was re-drawn by hand with no source.

Two things keep the render crisp under a platform's downscale.

  1. Type is drawn from the same system fonts the site uses, at 2x density.
  2. The logo is cropped out of static/img/stai-logos-bright.pdf, which is
     vector, so the wordmark downsamples instead of stretching. The raster
     static/img/stai_logo.png is only 916px wide and cannot fill the frame.

The layout fills the frame on purpose. A card sits at roughly 400-600 CSS px
in a feed, so a 4-6x downscale is normal; small type inside a mostly empty
frame is what reads as "low resolution" even when the file is 2400px wide.

Requires: Google Chrome and ImageMagick (brew install imagemagick).

Usage: python3 scripts/render-og-card.py [--out PATH] [--keep-temp]
"""

import argparse
import base64
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOGO_PDF = ROOT / "static" / "img" / "stai-logos-bright.pdf"
DEFAULT_OUT = ROOT / "static" / "img" / "og-default-v2.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# --- canvas -----------------------------------------------------------------
W, H, SCALE = 1200, 630, 2

# --- palette, mirroring the :root tokens in static/css/stai.css -------------
INK = "#111014"
INK_2 = "#38343F"
MAGENTA = "#A6249D"
GRAD = "linear-gradient(90deg,#A6249D 0%,#C2417A 34%,#E0603F 66%,#FF9A1F 100%)"
SERIF = '"Iowan Old Style","Charter","Source Serif Pro",Georgia,serif'
UI = '"Avenir Next","Avenir","Helvetica Neue",Arial,sans-serif'

# --- copy -------------------------------------------------------------------
EYEBROW = "KAIST AI - RESEARCH GROUP"
TITLE = "Scalable Trustworthy AI"
SUBTITLE = "Creating scalable and trustworthy AI with human guidance"

# --- type scale, in CSS px on the 1200x630 layout ---------------------------
# The card fills the frame: ~6% margins, and the four elements are spaced
# apart to span the remaining height. Sizes here are ceilings. The title is
# held to one line and the subtitle to two, so both are fitted in the page
# (see FIT_JS) rather than hard-coded -- the copy comes from config.toml and
# a longer slogan must shrink to fit instead of overflowing the frame.
PAD_X, PAD_TOP, PAD_BOTTOM = 70, 58, 48
BAR_H = 14
EYEBROW_PX = 27
LOGO_H = 118
TITLE_MAX, TITLE_MIN = 132, 72
SUBTITLE_MAX, SUBTITLE_MIN = 52, 34
SUBTITLE_LINES = 2

# Runs in the page before the screenshot. Steps the size down until the line
# count is right, so the fit is measured by the same engine that draws it.
FIT_JS = """
const inner = %d;
const h1 = document.querySelector('h1');
for (let s = %d; s >= %d; s -= 1) {
  h1.style.fontSize = s + 'px';
  if (h1.scrollWidth <= inner) break;
}
const dek = document.querySelector('.dek');
for (let s = %d; s >= %d; s -= 1) {
  dek.style.fontSize = s + 'px';
  const lh = parseFloat(getComputedStyle(dek).lineHeight);
  if (dek.getBoundingClientRect().height <= lh * %d + 1) break;
}
"""

# The bright PDF stacks three elements: the swoosh, the STAI wordmark, then a
# tagline the card sets in its own type. Bands are ink bounding boxes measured
# at the render density below; they are stable because the source is vector.
CROP_DENSITY = 2400
BAND_SWOOSH = (0, 0, 3093, 1172)
BAND_STAI = (888, 1197, 3885, 2309)

# The horizontal lockup is not in the PDF, so it is rebuilt here from the two
# crops. Fractions come from static/img/stai_logo.png (916x174), the lockup as
# the group's designer set it.
LOCKUP_AR = 916 / 174
SWOOSH_BOX = (5 / 916, 10 / 174, 420 / 916, 159 / 174)  # left, top, w, h
STAI_BOX = (454 / 916, 3 / 174, 456 / 916, 169 / 174)


def crop_logo(tmp):
    """Cut the swoosh and the wordmark out of the vector PDF."""
    if not LOGO_PDF.exists():
        sys.exit(f"missing {LOGO_PDF}")
    full = tmp / "logo-full.png"
    subprocess.run(
        ["magick", "-density", str(CROP_DENSITY), str(LOGO_PDF),
         "-background", "white", "-flatten", str(full)],
        check=True,
    )
    out = {}
    for name, (x0, y0, x1, y1) in (("swoosh", BAND_SWOOSH), ("stai", BAND_STAI)):
        path = tmp / f"logo-{name}.png"
        subprocess.run(
            ["magick", str(full),
             "-crop", f"{x1 - x0}x{y1 - y0}+{x0}+{y0}", "+repage",
             # White is the PDF's page, not part of the mark. Drop it so the
             # crop composites onto the card instead of boxing it in.
             "-fuzz", "4%", "-transparent", "white",
             f"PNG32:{path}"],
            check=True,
        )
        out[name] = base64.b64encode(path.read_bytes()).decode()
    return out


def site_copy():
    """Read the card's text from config.toml so it cannot drift."""
    try:
        text = (ROOT / "config.toml").read_text()
    except OSError:
        return TITLE, SUBTITLE
    def param(key, fallback):
        m = re.search(rf'^\s*{key}\s*=\s*"(.*)"\s*$', text, re.M)
        return m.group(1) if m else fallback
    title = param("slogan", TITLE)
    # Keep an acronym off the start of a line -- the subtitle wraps, and
    # "trustworthy / AI" reads as a broken phrase.
    dek = re.sub(r" (?=[A-Z]{2,4}\b)", "\u00a0", param("slogan_text", SUBTITLE))
    return title, dek


def build_html(logos, title, subtitle):
    inner = W - 2 * PAD_X
    fit_js = FIT_JS % (inner, TITLE_MAX, TITLE_MIN,
                       SUBTITLE_MAX, SUBTITLE_MIN, SUBTITLE_LINES)
    return f"""<!doctype html>
<meta charset="utf-8">
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  html,body{{width:{W}px;height:{H}px}}
  body{{background:#fff;-webkit-font-smoothing:antialiased}}
  .card{{position:relative;width:{W}px;height:{H}px;
    padding:{PAD_TOP}px {PAD_X}px {PAD_BOTTOM + BAR_H}px;
    display:flex;flex-direction:column;justify-content:space-between}}
  .eyebrow{{font:600 {EYEBROW_PX}px/1 {UI};letter-spacing:.2em;
    text-transform:uppercase;color:{MAGENTA}}}
  .lockup{{position:relative;height:{LOGO_H}px;width:{LOGO_H * LOCKUP_AR:.1f}px}}
  .lockup img{{position:absolute;height:auto}}
  .sw{{left:{SWOOSH_BOX[0] * 100:.2f}%;top:{SWOOSH_BOX[1] * 100:.2f}%;
    width:{SWOOSH_BOX[2] * 100:.2f}%}}
  .wm{{left:{STAI_BOX[0] * 100:.2f}%;top:{STAI_BOX[1] * 100:.2f}%;
    width:{STAI_BOX[2] * 100:.2f}%}}
  h1{{font:400 {TITLE_MAX}px/1.02 {SERIF};letter-spacing:-.018em;color:{INK};
    white-space:nowrap}}
  .dek{{font:400 {SUBTITLE_MAX}px/1.22 {SERIF};color:{INK_2};
    width:{inner}px;text-wrap:balance}}
  .bar{{position:absolute;left:0;right:0;bottom:0;height:{BAR_H}px;
    background:{GRAD}}}
</style>
<div class="card">
  <p class="eyebrow">{EYEBROW}</p>
  <div class="lockup">
    <img class="sw" src="data:image/png;base64,{logos['swoosh']}" alt="">
    <img class="wm" src="data:image/png;base64,{logos['stai']}" alt="">
  </div>
  <h1>{title}</h1>
  <p class="dek">{subtitle}</p>
  <div class="bar"></div>
</div>
<script>{fit_js}</script>
"""


def shoot(html_path, out):
    if not pathlib.Path(CHROME).exists():
        sys.exit(f"missing Chrome at {CHROME}")
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
         f"--screenshot={out}", f"--window-size={W},{H}",
         f"--force-device-scale-factor={SCALE}",
         f"--default-background-color=ffffffff",
         html_path.as_uri()],
        check=True, capture_output=True,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT)
    ap.add_argument("--keep-temp", action="store_true")
    args = ap.parse_args()

    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        logos = crop_logo(tmp)
        title, subtitle = site_copy()
        html = tmp / "card.html"
        html.write_text(build_html(logos, title, subtitle))
        if args.keep_temp:
            keep = ROOT / "scripts" / "og-card-preview.html"
            keep.write_text(html.read_text())
            print(f"kept {keep}")
        shoot(html, args.out)

    # An optimise pass; the card is flat colour, so it compresses hard.
    subprocess.run(["magick", str(args.out), "-strip", "-define",
                    "png:compression-filter=5", "-define",
                    "png:compression-level=9", str(args.out)], check=True)
    size = args.out.stat().st_size
    try:
        shown = args.out.relative_to(ROOT)
    except ValueError:
        shown = args.out
    print(f"wrote {shown} ({size / 1024:.0f}KB)")


if __name__ == "__main__":
    main()
