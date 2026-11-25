#!/usr/bin/env python3
"""Render the News-24 v2 front page (1024x1024 PNG) from stories.py.

Deterministic: same input data -> same bytes. No network, no clock, no
randomness. Run: python3 render.py [out.png]
"""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

import stories as S

W, H = 1024, 1024
M = 14  # side margin
CW = W - 2 * M  # content width

INK = (20, 32, 43)
MUTED = (90, 107, 122)
NAVY = (15, 42, 68)
NAVY_SOFT = (191, 208, 222)
BAND = (238, 242, 245)
LINE = (201, 212, 222)
PAPER = (255, 255, 255)
OCEAN = (217, 233, 246)
LAND = (227, 234, 217)
LAND_LINE = (154, 164, 143)
GOLD = (201, 162, 39)

BADGE = {
    "CONFIRMED": (30, 122, 52),
    "REPORTED": (31, 97, 141),
    "OFFICIAL": (91, 44, 111),
    "CLAIM": (176, 58, 46),
}

DJ = "/usr/share/fonts/truetype/dejavu/"


def F(size, bold=False, serif=False, italic=False):
    if serif:
        name = "DejaVuSerif-Bold.ttf" if bold else "DejaVuSerif.ttf"
        return ImageFont.truetype(os.path.join(DJ, name), size)
    if italic:
        return ImageFont.truetype(
            "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf", size)
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(DJ, name), size)


def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_h(font, lines, leading):
    return len(lines) * leading


def pill(d, x, y, label, font, bg):
    w = int(font.getlength(label)) + 12
    h = 16
    d.rounded_rectangle([x, y, x + w, y + h], radius=8, fill=bg)
    d.text((x + 6, y + 3), label, font=font, fill=(255, 255, 255))
    return w


def num_badge(d, cx, cy, n, color, r=11):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color, outline=(255, 255, 255), width=1)
    f = F(11 if n < 10 else 9, bold=True)
    t = str(n)
    d.text((cx - f.getlength(t) / 2, cy - (6 if n < 10 else 5)), t, font=f, fill=(255, 255, 255))


# ---------------------------------------------------------------- continents
NA = [(-168, 66), (-150, 70), (-130, 71), (-110, 73), (-95, 80), (-85, 76), (-80, 73),
      (-70, 62), (-65, 60), (-55, 52), (-60, 46), (-70, 42), (-75, 35), (-81, 26),
      (-84, 30), (-90, 21), (-97, 16), (-102, 18), (-110, 24), (-117, 33), (-125, 40),
      (-124, 49), (-135, 58), (-150, 60), (-168, 66)]
SA = [(-80, 9), (-72, 12), (-62, 9), (-52, 5), (-50, 0), (-42, -3), (-35, -8),
      (-38, -15), (-40, -22), (-48, -27), (-55, -34), (-62, -41), (-68, -50), (-70, -54),
      (-73, -45), (-73, -37), (-70, -20), (-77, -12), (-81, -6), (-80, 2), (-80, 9)]
EU = [(-10, 36), (-9, 43), (-2, 48), (-4, 50), (2, 51), (7, 54), (8, 57), (12, 56),
      (18, 56), (21, 59), (24, 60), (28, 62), (30, 70), (40, 68), (44, 66), (48, 60),
      (44, 55), (40, 50), (38, 47), (33, 45), (30, 46), (28, 44), (26, 40), (23, 36),
      (22, 37), (19, 40), (15, 44), (12, 44), (8, 44), (3, 43), (0, 40), (-2, 37),
      (-6, 36), (-9, 37), (-10, 36)]
AF = [(-17, 15), (-16, 20), (-10, 30), (-6, 33), (0, 36), (10, 37), (15, 32), (20, 32),
      (25, 32), (30, 31), (32, 31), (34, 28), (37, 22), (40, 15), (43, 12), (48, 11),
      (51, 11), (50, 5), (45, 0), (42, -5), (40, -12), (38, -18), (35, -22), (33, -26),
      (31, -29), (28, -33), (25, -34), (20, -35), (17, -32), (15, -27), (13, -18),
      (12, -12), (9, -1), (9, 4), (4, 6), (-4, 5), (-8, 5), (-13, 8), (-17, 12), (-17, 15)]
AS = [(40, 68), (48, 70), (55, 72), (65, 73), (75, 74), (85, 75), (95, 76), (105, 77),
      (115, 76), (125, 73), (135, 72), (145, 72), (155, 70), (162, 68), (170, 66),
      (178, 65), (178, 62), (170, 60), (162, 56), (158, 52), (150, 59), (142, 54),
      (142, 45), (140, 40), (135, 35), (130, 33), (127, 35), (126, 38), (122, 32),
      (120, 28), (118, 25), (112, 22), (108, 18), (105, 10), (103, 7), (100, 6),
      (98, 10), (95, 16), (92, 21), (89, 22), (86, 20), (82, 17), (80, 10), (77, 8),
      (76, 12), (73, 18), (70, 21), (66, 25), (62, 25), (58, 26), (55, 27), (52, 28),
      (50, 29), (48, 30), (46, 32), (44, 36), (42, 40), (40, 44), (40, 50), (40, 58),
      (40, 68)]
AU = [(113, -22), (114, -28), (115, -33), (118, -35), (124, -33), (129, -32), (132, -32),
      (135, -35), (137, -35), (140, -38), (143, -39), (146, -39), (149, -37), (150, -35),
      (152, -32), (153, -27), (153, -24), (151, -23), (149, -20), (146, -19), (144, -15),
      (142, -11), (141, -13), (138, -15), (136, -12), (134, -12), (132, -11), (130, -13),
      (128, -14), (126, -14), (124, -16), (122, -17), (120, -19), (117, -20), (114, -21),
      (113, -22)]
SEA = [(95, 6), (98, 4), (100, 0), (102, -2), (105, -4), (108, -6), (111, -7), (114, -8),
       (117, -8), (120, -9), (123, -10), (126, -9), (129, -8), (131, -4), (134, -4),
       (137, -3), (140, -4), (142, -6), (145, -7), (147, -9), (146, -7), (142, -4),
       (138, -2), (135, 0), (132, 1), (130, 2), (128, 3), (126, 2), (124, 1), (122, 0),
       (120, 1), (118, 2), (116, 1), (114, 0), (112, -1), (110, 0), (108, 1), (106, 2),
       (104, 1), (102, 2), (100, 4), (98, 5), (95, 6)]
NZ = [(167, -45), (170, -42), (173, -40), (175, -38), (177, -38), (178, -37), (175, -40),
      (172, -43), (169, -46), (167, -45)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51), (-1, 50),
      (-4, 50), (-5, 50)]
JP = [(130, 31), (132, 33), (134, 34), (136, 35), (138, 35), (140, 37), (141, 39),
      (141, 41), (142, 43), (144, 44), (143, 42), (141, 40), (140, 38), (139, 36),
      (137, 35), (135, 34), (133, 34), (131, 32), (130, 31)]
CONTINENTS = [NA, SA, EU, AF, AS, AU, SEA, NZ, UK, JP]

# pixel offsets so clustered pins stay readable (UK grid expanded)
PIN_OFF = {
    3: (8, -6), 8: (-6, 6),
    6: (-9, 0), 11: (9, 0),
    7: (-9, 0), 21: (9, 0),
    28: (-9, 0), 29: (9, 0),
}
UK_GRID = {12: (-16, -14), 14: (0, -14), 15: (16, -14),
           16: (-16, 0), 17: (0, 0), 18: (16, 0),
           19: (-16, 14), 20: (0, 14), 30: (16, 14)}


def story(n):
    return S.STORIES[n - 1]


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------------------------------------------------------------- header
    d.rectangle([0, 0, W, 64], fill=NAVY)
    d.rectangle([0, 64, W, 66], fill=GOLD)
    d.text((M, 8), "THE WORLD TODAY", font=F(30, bold=True, serif=True), fill=(255, 255, 255))
    d.text((M, 43), "30 stories with UTC timestamps  ·  7 regions",
           font=F(12), fill=NAVY_SOFT)
    right = "TUESDAY 24 NOVEMBER 2026"
    d.text((W - M - F(19, bold=True).getlength(right), 10), right,
           font=F(19, bold=True), fill=(255, 255, 255))
    sub = "Every story timed — read the day in one image"
    d.text((W - M - F(11, italic=True).getlength(sub), 42), sub,
           font=F(11, italic=True), fill=NAVY_SOFT)

    # ------------------------------------------------------- timeline strip
    d.rectangle([0, 66, W, 104], fill=BAND)
    d.line([(M, 88), (W - M, 88)], fill=LINE, width=2)
    cell = CW / len(S.TIMELINE)
    for i, (t, label) in enumerate(S.TIMELINE):
        cx = M + cell * (i + 0.5)
        d.ellipse([cx - 3, 85, cx + 3, 91], fill=NAVY)
        tf = F(11, bold=True)
        d.text((cx - tf.getlength(t) / 2, 70), t, font=tf, fill=NAVY)
        lf = F(9)
        d.text((cx - lf.getlength(label) / 2, 92), label, font=lf, fill=MUTED)

    # ------------------------------------------------------- day in numbers
    d.text((M, 110), "THE DAY IN NUMBERS", font=F(10, bold=True), fill=NAVY)
    ncell = CW / len(S.NUMBERS)
    for i, (big, cap) in enumerate(S.NUMBERS):
        x = M + ncell * i
        if i:
            d.line([(x - 6, 112), (x - 6, 152)], fill=LINE, width=1)
        bf = F(22, bold=True)
        d.text((x, 122), big, font=bf, fill=NAVY)
        for j, ln in enumerate(wrap(cap, F(10), ncell - 14)):
            d.text((x, 148 + j * 11), ln, font=F(10), fill=MUTED)
    d.line([(M, 156), (W - M, 156)], fill=LINE, width=1)

    # ---------------------------------------------------------------- leads
    lead_w = (CW - 20) // 3
    lead_x = [M, M + lead_w + 10, M + 2 * (lead_w + 10)]
    lead_y, lead_h = 164, 228
    for k, n in enumerate(S.LEADS):
        _, t, region, label, head, fact, src, _, _ = story(n)
        x, y = lead_x[k], lead_y
        col = S.REGION_COLORS[region]
        d.rectangle([x, y, x + lead_w, y + lead_h], outline=LINE, width=1, fill=PAPER)
        d.rectangle([x, y, x + lead_w, y + 5], fill=col)
        kf = F(10, bold=True)
        d.text((x + 10, y + 12), "LEAD %d · %s" % (k + 1, region), font=kf, fill=col)
        tf = F(11, bold=True)
        d.text((x + lead_w - 10 - tf.getlength(t), y + 12), t, font=tf, fill=INK)
        badge = label if label != "CLAIM" else "CLAIM vs DENIAL"
        pill(d, x + 10, y + 32, badge, F(9, bold=True), BADGE.get(label, (31, 97, 141)))
        cy = y + 56
        for ln in wrap(head, F(16, bold=True), lead_w - 20):
            d.text((x + 10, cy), ln, font=F(16, bold=True), fill=INK)
            cy += 19
        cy += 4
        if n in S.LEAD_SIDES:
            lh, lt, rh, rt = S.LEAD_SIDES[n]
            bw = (lead_w - 30) // 2
            for j, (hh, tt, cc) in enumerate(((lh, lt, (176, 58, 46)), (rh, rt, (31, 97, 141)))):
                bx = x + 10 + j * (bw + 10)
                d.rectangle([bx, cy, bx + bw, cy + 56], outline=LINE, width=1, fill=BAND)
                d.text((bx + 6, cy + 5), hh, font=F(9, bold=True), fill=cc)
                for m, ln in enumerate(wrap(tt, F(11, bold=True), bw - 12)):
                    d.text((bx + 6, cy + 20 + m * 13), ln, font=F(11, bold=True), fill=INK)
            cy += 62
        for ln in wrap(fact, F(12), lead_w - 20):
            d.text((x + 10, cy), ln, font=F(12), fill=(43, 56, 68))
            cy += 15
        d.text((x + 10, y + lead_h - 18), "Source: " + src, font=F(10, italic=True), fill=MUTED)

    # ----------------------------------------------------------------- mids
    my = lead_y + lead_h + 10
    d.text((M, my), "MORE OF THE DAY — 10 stories", font=F(12, bold=True), fill=NAVY)
    d.line([(M, my + 18), (W - M, my + 18)], fill=LINE, width=1)
    mid_y = my + 26
    mid_w = (CW - 16) // 2
    mid_h = 48
    for i, n in enumerate(S.MIDS):
        _, t, region, label, head, fact, src, _, _ = story(n)
        col = S.REGION_COLORS[region]
        cx = M + (i % 2) * (mid_w + 16)
        ry = mid_y + (i // 2) * mid_h
        num_badge(d, cx + 11, ry + 13, n, col)
        tx = cx + 28
        tw = mid_w - 28
        tf, hf = F(11, bold=True), F(12, bold=True)
        tpre = t + "  "
        d.text((tx, ry + 1), t, font=tf, fill=col)
        hlines = wrap(head, hf, tw - tf.getlength(tpre))
        d.text((tx + tf.getlength(tpre), ry + 1), hlines[0], font=hf, fill=INK)
        fy = ry + 15
        max_fact = 2
        if len(hlines) > 1:
            d.text((tx, ry + 14), hlines[1], font=hf, fill=INK)
            fy = ry + 28
            max_fact = 1
        flines = wrap(fact, F(11), tw)[:max_fact]
        # Decide the source placement BEFORE drawing: trim the last fact line
        # first if the source would not fit after it (drawing over text does
        # not erase it, so trimming must happen before any drawing).
        src_txt = " · " + src
        sw = F(10).getlength(src_txt)
        last = flines[-1] if flines else ""
        if F(11).getlength(last) + sw + 4 <= tw:
            draw_lines = flines
            src_x = tx + F(11).getlength(last) + 4
        else:
            trimmed = last
            while trimmed and F(11).getlength(trimmed + "…") + sw + 4 > tw:
                trimmed = trimmed.rsplit(" ", 1)[0]
            draw_lines = flines[:-1] + [trimmed + "…"]
            src_x = tx + F(11).getlength(trimmed + "…") + 4
        for ln in draw_lines:
            d.text((tx, fy), ln, font=F(11), fill=(43, 56, 68))
            fy += 13
        d.text((src_x, fy - 13), src_txt, font=F(10), fill=MUTED)

    # ----------------------------------------------------------------- also
    ay = mid_y + 5 * mid_h + 8
    d.text((M, ay), "ALSO TODAY — 17 stories", font=F(12, bold=True), fill=NAVY)
    d.line([(M, ay + 18), (W - M, ay + 18)], fill=LINE, width=1)
    also_y = ay + 26
    tails = {26: " — talks next week"}
    for i, n in enumerate(S.ALSO):
        _, t, region, label, head, fact, src, _, _ = story(n)
        col = S.REGION_COLORS[region]
        cx = M + (i % 2) * (mid_w + 16)
        ry = also_y + (i // 2) * 19
        num_badge(d, cx + 8, ry + 7, n, col, r=8)
        line = "%s — %s (%s)%s" % (t, head, src, tails.get(n, ""))
        d.text((cx + 20, ry), line, font=F(11), fill=INK)

    # ------------------------------------------------------------------ map
    map_y = also_y + 9 * 19 + 8
    d.text((M, map_y), "WHERE IT HAPPENED — 30 numbered pins",
           font=F(11, bold=True), fill=NAVY)
    lx = W - M
    legend = "ASIA 5 · EUROPE 11 · OCEANIA 7 · AMERICAS 4 · M. EAST 1 · AFRICA 1 · WORLD 1"
    d.text((lx - F(9).getlength(legend), map_y + 1), legend, font=F(9), fill=MUTED)
    map_top, map_bot = map_y + 18, 948
    d.rectangle([M, map_top, W - M, map_bot], fill=OCEAN, outline=LINE, width=1)

    def px(lon, lat):
        return (M + (lon + 180.0) / 360.0 * CW,
                map_top + (83.0 - lat) / 139.0 * (map_bot - map_top))

    for poly in CONTINENTS:
        d.polygon([px(lon, lat) for lon, lat in poly], fill=LAND, outline=LAND_LINE)
    for n in range(1, 31):
        _, _, region, _, _, _, _, lon, lat = story(n)
        x, y = px(lon, lat)
        if n in UK_GRID:
            ox, oy = UK_GRID[n]
            x, y = px(-0.1, 51.5)
            x, y = x + ox, y + oy
        elif n in PIN_OFF:
            ox, oy = PIN_OFF[n]
            x, y = x + ox, y + oy
        num_badge(d, x, y, n, S.REGION_COLORS[region], r=7)

    # --------------------------------------------------------------- footer
    fy = map_bot + 6
    fnt, bfnt = F(9), F(9, bold=True)
    lead = 10

    def para(y, head, rest):
        hw = bfnt.getlength(head)
        first = wrap(rest, fnt, CW - hw)
        lines = []
        if first:
            lines.append((head, first[0]))
            lines.extend([("", ln) for ln in first[1:]])
        for hd, ln in lines:
            if hd:
                d.text((M, y), hd, font=bfnt, fill=NAVY)
                d.text((M + hw, y), ln, font=fnt, fill=INK)
            else:
                d.text((M, y), ln, font=fnt, fill=INK)
            y += lead
        return y + 2

    date_check = (
        "Wires read to %s. Every story happened, or was first reported, on Tue 24 Nov 2026. "
        "Edge cases, stated plainly: KADIZ alert 07:52 KST Tue = 22:52 UTC Mon; Emmy winners "
        "announced Mon night in New York, reported 04:35 UTC Tue; Trump order issued Mon, AP report "
        "Tue 11:20 UTC; London Museum unveiled Tue, opens Sat 28 Nov; Chess Game 1 at 14:00 UTC is "
        "the scheduled start. 19 stories carry an exact UTC hour; 11 carry their source's 24 Nov "
        "dateline." % S.WIRES_READ)
    fy = para(fy, "DATE CHECK — ", date_check)
    fy = para(fy, "LEFT OUT — ", "earlier days, not 24 Nov: " + S.DROPPED)
    fy = para(fy, "HOW SURE — ",
              "REPORTED: the day's wires · CONFIRMED: 2+ sources or the record · "
              "OFFICIAL: government / institution · CLAIM: one side's claim · "
              "DENIAL / CORRECTION: the other side's answer.")
    assert fy <= H, "footer overflow: %d" % fy

    img.save(out, format="PNG")
    print("wrote %s %dx%d" % (out, W, H))


if __name__ == "__main__":
    main()
