#!/usr/bin/env python3
"""Render meme #5 untuk gta6-meme-x-01 (akun 1): timeline kalender 2013-2026.
Teks tajam via PIL (bukan AI image) supaya terbaca di 480px.
Output: meme5.png (1080x1080). Logo hantu dari press kit resmi make.fun.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
ASSETS = os.path.expanduser('~/workspace/makefun/meme-x-assets')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme5.png')

PAPER = (247, 245, 240)
INK = (26, 24, 40)
MUTED = (110, 104, 122)
MAGENTA = (214, 51, 132)
WHITE = (255, 255, 255)
LINE = (200, 190, 180)
DOT = (150, 142, 160)


def font(name, size):
    paths = [
        f'/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf',
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new('RGB', (W, H), PAPER)
d = ImageDraw.Draw(img)

MX = 64  # margin x

# --- header: ghost + make.fun + calendar ---
ghost = Image.open(os.path.join(ASSETS, 'mark-1024.png')).convert('RGBA')
ghost = ghost.resize((88, 88), Image.LANCZOS)
img.paste(ghost, (MX, 48), ghost)
d.text((MX + 108, 54), 'make.fun', font=font('Bold', 38), fill=INK)
d.text((MX + 108, 102), 'MY CALENDAR', font=font('Regular', 22), fill=MUTED)
d.text((W - MX, 58), '2013 - 2026', font=font('Bold', 28), fill=INK, anchor='ra')
d.text((W - MX, 98), '13 YEARS', font=font('Regular', 22), fill=MUTED, anchor='ra')

d.line([(MX, 172), (W - MX, 172)], fill=LINE, width=2)

# --- title ---
d.text((MX, 198), '13 YEARS OF WAITING', font=font('Black', 72), fill=INK)

# --- timeline ---
line_x = 110
y0, y1 = 348, 828
d.line([(line_x, y0), (line_x, y1)], fill=LINE, width=4)
rows = [
    ('2013', "GTA V is out. 'VI soon.'", False),
    ('2016', 'Still waiting.', False),
    ('2019', 'Still waiting.', False),
    ('2022', 'Still waiting.', False),
    ('2025', 'Delayed AGAIN.', False),
    ('2026', 'GTA VI. FINALLY.', True),
]
y = 320
for year, note, hot in rows:
    color = MAGENTA if hot else DOT
    d.ellipse([(line_x - 12, y + 16), (line_x + 12, y + 40)], fill=color)
    d.text((line_x + 36, y), year, font=font('Black', 40),
           fill=MAGENTA if hot else INK)
    d.text((line_x + 200, y + 6), note, font=font('Bold' if hot else 'Regular', 30),
           fill=MAGENTA if hot else MUTED)
    y += 96

# --- punchline bar ---
bar_y0, bar_y1 = 900, 1004
d.rounded_rectangle([(MX, bar_y0), (W - MX, bar_y1)], radius=22, fill=MAGENTA)
d.text((W // 2, bar_y0 + 14), 'MY AGENT EARNED REAL MONEY', font=font('Bold', 32), fill=WHITE, anchor='ma')
d.text((W // 2, bar_y0 + 56), 'THE WHOLE TIME ON make.fun.', font=font('Bold', 28), fill=WHITE, anchor='ma')

img.save(OUT, 'PNG')
print('saved', OUT, img.size, os.path.getsize(OUT), 'bytes')
