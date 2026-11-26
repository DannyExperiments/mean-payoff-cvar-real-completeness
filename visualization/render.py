"""Render the last four mass units of the lower half as rotating 3D bars."""

import argparse
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BG = "#101c30"
TEXT = "#f5f8fd"
MUTED = "#cbd7ed"
TEAL = "#78dcd1"
BLUE = "#8daeff"
AMBER = "#ffcd82"
BARS = [(1, 1.25, TEAL), (1, 2.375, TEAL), (1, 3, TEAL),
        (0.5, 5, BLUE), (0.5, 7.75, AMBER)]
FACES = [(0,1,3,2),(4,6,7,5),(0,4,5,1),
         (2,3,7,6),(0,2,6,4),(1,5,7,3)]


def project(point, yaw):
    x, y, z = point
    rx = x*cos(yaw)+z*sin(yaw)
    rz = z*cos(yaw)-x*sin(yaw)
    pitch = .33+.08*cos(yaw)
    ry = y*cos(pitch)-rz*sin(pitch)
    depth = y*sin(pitch)+rz*cos(pitch)
    scale = 390/(5.5-depth)
    return 238+scale*rx, 263-scale*ry, depth


def cube(start, end, reward):
    base, top = -1.3, reward/3-1.3
    return [(x,y,z) for x in (start,end) for y in (base,top) for z in (-.48,.48)]


def shade(color, multiplier):
    raw = tuple(int(color[i:i+2],16) for i in (1,3,5))
    return tuple(round(x*multiplier) for x in raw)


def frame(angle, fonts):
    title, label, result, body = fonts
    image = Image.new("RGB", (880, 596), BG)
    draw = ImageDraw.Draw(image)
    draw.text((24, 24), "A tail cutoff multiplies two choices", font=title, fill=TEXT)
    draw.line((28, 81, 852, 81), fill="#3c5274", width=2)
    draw.text((33, 111), "Last 4h of the lower half", font=body, fill=MUTED)

    faces = []
    offset = -2
    for mass, reward, color in BARS:
        vertices = [project(point,angle) for point in cube(offset+.02, offset+mass-.02, reward)]
        for idx, order in enumerate(FACES):
            ordered = [vertices[i] for i in order]
            depth = sum(node[2] for node in ordered)/4
            faces.append((depth, ordered, shade(color,(.72,.83,.52,1,.64,.89)[idx])))
        offset += mass
    for _, face, fill in sorted(faces):
        draw.polygon([point[:2] for point in face],fill=fill,outline=BG,width=2)

    draw.rounded_rectangle((486, 106, 853, 432), radius=16, fill="#1a2b47")
    draw.text((506, 126), "Check z = xy", font=label, fill=TEXT)
    draw.text((506, 193), "1/2 × 3/4", font=result, fill=TEXT)
    draw.text((506, 257), "= 3/8", font=result, fill=TEAL)
    draw.line((506,324,829,324),fill="#3c5274",width=2)
    draw.text((506, 354), "Both tail margins = 0", font=body, fill=MUTED)

    for y,color,caption in (
        (469,TEAL,"Three compensation blocks have width h"),
        (510,BLUE,"The low branch uses width hx"),
        (551,AMBER,"The pivot supplies the remaining h(1 − x)")
    ):
        draw.ellipse((31,y+12,47,y+28),fill=color)
        draw.text((61,y),caption,font=body,fill=MUTED)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/tail-multiplication.gif"))
    args = parser.parse_args()
    fonts = tuple(ImageFont.truetype(font,size) for font,size in (
        (args.bold_font,42),(args.bold_font,35),(args.bold_font,50),(args.regular_font,31)
    ))
    frames = [frame(.5+tau*index/64, fonts).quantize(colors=120,method=2) for index in range(64)]
    frames[0].save(args.output,save_all=True,append_images=frames[1:],
                   duration=92,loop=0,disposal=2,optimize=True)


if __name__ == "__main__":
    main()
