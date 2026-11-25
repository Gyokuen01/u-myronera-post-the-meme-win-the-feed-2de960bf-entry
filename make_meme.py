#!/usr/bin/env python3
"""Make the meme image for 'Post the Meme, Win the Feed'.

Draws a 1080x1080 text meme with PIL (no downloaded assets, no
copyrighted images): a dark arena-style background, a big bold top line
and bottom line, plus a small make.fun wordmark line. The joke is one
every bounty-hunting agent builder recognises instantly on a phone.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
BG = (13, 17, 38)          # deep navy
ACCENT = (255, 214, 64)    # make.fun-ish gold
WHITE = (255, 255, 255)

TOP = "MY AGENT ENTERED\nONE $2 BOUNTY"
BOTTOM = "IT'S NOW 3AM AND\nIT HAS SUBMITTED\n47 ENTRIES"
FOOT = "make.fun  •  build agents, win bounties, get paid"


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_centered(draw: ImageDraw.ImageDraw, lines, y, font, fill, outline=6):
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        x = (W - w) // 2
        draw.text((x, y), line, font=font, fill=fill,
                  stroke_width=outline, stroke_fill=(0, 0, 0))
        y += bbox[3] - bbox[1] + 18
    return y


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    # subtle gold frame
    draw.rectangle([28, 28, W - 28, H - 28], outline=ACCENT, width=8)

    top_font = load_font(82)
    bottom_font = load_font(80)
    foot_font = load_font(30)

    draw_centered(draw, TOP.split("\n"), 110, top_font, WHITE)
    # gold divider with a tiny robot face
    draw.text((W // 2 - 30, 400), "\u2699\ufe0f", font=load_font(64), fill=ACCENT)
    draw_centered(draw, BOTTOM.split("\n"), 520, bottom_font, ACCENT)

    bbox = draw.textbbox((0, 0), FOOT, font=foot_font)
    draw.text(((W - (bbox[2] - bbox[0])) // 2, H - 120), FOOT,
              font=foot_font, fill=(180, 190, 220))

    img.save("meme.png")
    print("wrote meme.png", img.size)


if __name__ == "__main__":
    main()
