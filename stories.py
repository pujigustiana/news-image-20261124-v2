# STORIES — data for the News-24 v2 front page.
# Every story happened, or was first reported, on Tuesday 24 November 2026.
# Times are UTC unless marked KST. "24 Nov" means the source page carries a
# 24 Nov dateline but no hour on the wire (see DATE CHECK in render.py).
# Labels: CONFIRMED = verified by 2+ sources or the record itself;
# OFFICIAL = a government or institution statement;
# REPORTED = carried by the day's wires; CLAIM / DENIAL = one side's position.

TITLE = "Tuesday 24 November 2026 — 30 stories with UTC timestamps, 7 regions"
WIRES_READ = "06:00 UTC"

REGION_COLORS = {
    "ASIA": "#B03A2E",
    "EUROPE": "#1F618D",
    "OCEANIA": "#148F77",
    "AMERICAS": "#7D3C98",
    "MIDDLE EAST": "#B7950B",
    "AFRICA": "#CA6F1E",
    "WORLD": "#2C3E50",
}

# n, time, region, label, headline, fact, source, lon, lat
STORIES = [
    (1, "00:57 UTC", "WORLD", "CONFIRMED",
     "Asian shares surge as Huang returns to Nvidia",
     "Nikkei hit 58,871 (+4.3%) in morning trade, closed 58,645 (+3.9%); "
     "KOSPI +6.3% to 5,006; Taiwan +9.0% to 40,122.",
     "Reuters / TradingView", 139.7, 35.7),
    (2, "02:45 UTC", "ASIA", "CLAIM",
     "Hasina: I'll fly home on 16 Dec — Dhaka: only in handcuffs",
     "Spokesman: return on Biman for Victory Day, 16 Dec. Minister: she can "
     "return only by extradition, in handcuffs; death sentence stands.",
     "Reuters", 90.4, 23.8),
    (3, "07:52 KST", "ASIA", "REPORTED",
     "Russian jets near Ulleung; shelter alert, then a correction",
     "About 5 Russian jets entered KADIZ; Ulleung shelter alert lifted in "
     "~3 minutes; JCS: no airspace violation.",
     "Reuters / Yonhap / JCS", 130.9, 37.5),
    (4, "01:32 UTC", "ASIA", "CONFIRMED",
     "Quake shakes Nepal's Koshi hills",
     "Magnitude 5.3, 10 km deep (EMSC); felt in India, Bhutan, Bangladesh "
     "and China; no casualties reported.",
     "Reuters / EMSC / USGS", 87.9, 27.9),
    (5, "00:30 UTC", "MIDDLE EAST", "REPORTED",
     "Strike near police post kills three in Khan Younis",
     "3 killed, 5 wounded beside a police position; 2 of the dead were police "
     "officers; 6 killed across Gaza on Tuesday.",
     "Reuters (Cairo)", 34.5, 31.3),
    (6, "11:20 UTC", "AMERICAS", "REPORTED",
     "Court revives Trump's bid to erase hush-money verdict",
     "2nd Circuit orders a lower court to rule on moving the case to federal "
     "court; order issued Mon 23 Nov; state appeal paused; 34 counts, "
     "$130,000 payment.",
     "AP", -74.5, 40.7),
    (7, "24 Nov", "AMERICAS", "REPORTED",
     "Huang returns to Nvidia — and faces five probes",
     "FBI, DOJ antitrust over the $12.9bn Hugging Face deal, SEC, California, "
     "Congress; Senate hearing 3 Dec; shares +31.5% on Monday.",
     "Reuters / Seoul Econ. Daily", -121.2, 37.8),
    (8, "01:30 UTC", "ASIA", "REPORTED",
     "Bank of Korea tipped to lift rates to 3.25% on Thursday",
     "Reuters poll of 34 economists: 32 expect a 25bp rise to 3.25% on "
     "26 Nov, then 3.50% in Q1 2027.",
     "Reuters", 127.0, 37.5),
    (9, "03:00 UTC", "ASIA", "OFFICIAL",
     "Singapore PM: Megaspeed inquiry goes on",
     "PM Lawrence Wong: the probe continues, a day after the US put Megaspeed "
     "and 6 affiliates on the Entity List.",
     "Reuters", 103.8, 1.35),
    (10, "14:00 UTC", "EUROPE", "OFFICIAL",
     "World chess: youngest final ever starts today",
     "Gukesh vs Sindarov, both 20, in Cologny, Geneva; max 14 classical games; "
     "Sindarov has white in game 1; $2.5m prize fund.",
     "FIDE / Chess.com", 6.1, 46.2),
    (11, "04:35 UTC", "EUROPE", "REPORTED",
     "Sky News wins International Emmy for Ukraine film",
     "'24 Hours in the Kill Zone' wins News at the 54th ceremony in New York; "
     "Carême takes Drama, Bobby Schofield Best Actor.",
     "Sky News", -73.3, 41.2),
    (12, "24 Nov", "EUROPE", "REPORTED",
     "London Museum unveils £437m Smithfield home",
     "Unveiled Tue 24 Nov; doors open Sat 28 Nov; fatberg, Banksy's Piranhas "
     "and Pankhurst's hunger-strike medal on show.",
     "London Museum", -0.1, 51.5),
    (13, "11:00 UTC", "AFRICA", "REPORTED",
     "Pastor Angel remanded as bail hearing is deferred",
     "Harare court places Angel on remand; bail hearing Wed 25 Nov; single "
     "charge: aggravated indecent assault; 3 officers held over VIP cell.",
     "NewsDay / Christian Post", 31.0, -17.8),
    (14, "00:45 UTC", "EUROPE", "REPORTED",
     "Burnham urged to cool talk of Britain rejoining the EU",
     "Andy Burnham pressed to damp down debate on rejoining the EU.",
     "BBC", 0.9, 51.9),
    (15, "01:31 UTC", "EUROPE", "REPORTED",
     "'No 10 North' in Manchester under closer watch",
     "PM's Manchester office watched more closely as Burnham's 10-year plan "
     "takes shape.",
     "BBC", -1.1, 51.2),
    (16, "01:53 UTC", "EUROPE", "REPORTED",
     "Severely ill spared repeat PIP assessments",
     "Timms review: people with severe conditions no longer need reassessment "
     "for PIP.",
     "BBC", 0.9, 51.1),
    (17, "01:11 UTC", "EUROPE", "REPORTED",
     "Breeders sold sick puppies for £2,000 a pup",
     "BBC investigation: ratings were cut but five-star ads stayed up.",
     "BBC", -1.1, 51.9),
    (18, "01:03 UTC", "EUROPE", "REPORTED",
     "Autumn's coldest spell drags on: ice, hill snow, heavy rain",
     "The coldest spell of the autumn continues across the UK.",
     "BBC", 0.0, 52.1),
    (19, "00:01 UTC", "EUROPE", "REPORTED",
     "Green leader backs pro-NATO report, keeps nuclear arms",
     "Zack Polanski backs Verdant's 42-page report: stay in NATO, keep the "
     "Dreadnought subs, work closer with France.",
     "The Guardian", 1.7, 51.5),
    (20, "24 Nov", "EUROPE", "REPORTED",
     "Faith in COP 'misplaced', says Macfarlane",
     "Reaction to the COP31 collapse: trust in the COP process called misplaced.",
     "The Guardian", -1.7, 51.5),
    (21, "02:21 UTC", "AMERICAS", "REPORTED",
     "Nvidia HQ split over Huang's return",
     "Reaction at Nvidia's Santa Clara HQ: some delighted, some anxious.",
     "BBC", -122.8, 37.0),
    (22, "24 Nov", "AMERICAS", "REPORTED",
     "Harrelson turned down Haymitch twice",
     "Woody Harrelson twice refused the Haymitch role before accepting.",
     "Variety", -118.3, 34.1),
    (23, "24 Nov", "OCEANIA", "REPORTED",
     "Pacific Elders accuse Australia of climate betrayal",
     "Pacific Elders' Voice accused Australia of betraying the Pacific on "
     "climate at COP31.",
     "PINA", 178.4, -17.7),
    (24, "24 Nov", "OCEANIA", "REPORTED",
     "Kanton Island emptied at a day's notice",
     "All 40–50 residents of Kanton, Kiribati, moved to Tarawa; told return "
     "may take 4 years; ex-US base.",
     "PINA / TVNZ", -171.7, -2.8),
    (25, "24 Nov", "OCEANIA", "REPORTED",
     "Origin star Hudson Young joins PNG Chiefs",
     "Hudson Young signed for the PNG Chiefs' first season.",
     "PINA", 147.2, -9.5),
    (26, "24 Nov", "OCEANIA", "REPORTED",
     "Pacific bloc unites before key tuna talks",
     "South Pacific Group united ahead of key WCPFC tuna talks next week.",
     "PINA", 158.2, 6.9),
    (27, "24 Nov", "OCEANIA", "REPORTED",
     "Solomons PM flies to Canberra to meet Albanese",
     "PM Matthew Wale flew to Canberra to meet PM Albanese.",
     "PINA", 149.1, -35.3),
    (28, "24 Nov", "OCEANIA", "REPORTED",
     "Lamarre-Condon takes 'long road' to witness box",
     "Accused Beau Lamarre-Condon chose the 'long road' to the witness box.",
     "The Guardian", 151.2, -33.9),
    (29, "24 Nov", "OCEANIA", "OFFICIAL",
     "UNSW launches world-first AI 'megafire' simulator",
     "UNSW and Fire and Rescue NSW launched iFire 2.3: AI plus immersive "
     "visualisation for training.",
     "Medianet", 151.9, -33.5),
    (30, "01:01 UTC", "EUROPE", "REPORTED",
     "'I pay £250 a month for someone to run my life'",
     "A busy mother on both sides of the Atlantic pays £250 a month for a "
     "life-admin service.",
     "BBC", 0.0, 50.8),
]

LEADS = (1, 2, 3)
MIDS = tuple(range(4, 14))
ALSO = tuple(range(14, 31))

# The two-sided lead panels: (story n, left head, left text, right head, right text)
LEAD_SIDES = {
    2: ("HASINA CLAIMS", "Return 16 Dec on Biman for Victory Day",
        "DHAKA ANSWERS", "Only by extradition — in handcuffs"),
    3: ("THE ALERT SAID", "Airspace violated — take shelter",
        "JCS CORRECTED", "No violation; wrongly named N. Korea"),
}

# Timeline strip: (time, short label)
TIMELINE = [
    ("00:01", "Polanski backs NATO"),
    ("00:30", "Khan Younis"),
    ("00:57", "Nikkei 58,871"),
    ("01:32", "Nepal M5.3"),
    ("02:45", "Hasina"),
    ("04:35", "Emmy"),
    ("07:52 KST", "KADIZ alert"),
    ("11:00", "Angel in court"),
    ("11:20", "Trump court"),
    ("14:00", "Chess Game 1"),
]

# The day in numbers: (big, caption)
NUMBERS = [
    ("5.3", "Nepal quake magnitude"),
    ("58,871", "Nikkei intraday peak"),
    ("5,006", "KOSPI close, over 5,000"),
    ("3", "killed in Khan Younis"),
    ("16 Dec", "Hasina's planned return"),
    ("14", "chess games · $2.5m fund"),
]

DROPPED = (
    "Iran–Bahrain strike (21 Nov) · El Chapo Isidro (20–21 Nov) · Sparta II (21 Nov) · "
    "COP31 collapse (22 Nov) · India 720/9 (22 Nov) · Democrats' 258 House seats (22 Nov) · "
    "Houthi / Riyadh (21 Nov) · Hormuz tanker (21–22 Nov) · Lewis Pugh (22 Nov) · "
    "Cúcuta drone attack (23 Nov) · Indonesia candy-factory fire (23 Nov)"
)

DATE_CHECK = (
    "Wires read to 06:00 UTC. Every story happened, or was first reported, on Tue 24 Nov 2026. "
    "Edge cases, stated plainly: KADIZ alert 07:52 KST Tue = 22:52 UTC Mon; Emmy winners announced "
    "Mon night in New York, reported 04:35 UTC Tue; Trump order issued Mon, AP report Tue 11:20 UTC; "
    "London Museum unveiled Tue, opens Sat 28 Nov; Chess Game 1 (14:00 UTC) is the day's scheduled "
    "start, announced in advance. 19 stories carry an exact UTC hour; 11 carry their source's "
    "24 Nov dateline with no hour on the wire."
)

HOW_SURE = (
    "REPORTED: carried by the day's wires · CONFIRMED: verified by 2+ sources or the record · "
    "OFFICIAL: a government or institution statement · CLAIM: one side's claim, not verified · "
    "DENIAL / CORRECTION: the other side's answer."
)

REGION_COUNTS = {"ASIA": 5, "EUROPE": 11, "OCEANIA": 7, "AMERICAS": 4,
                 "MIDDLE EAST": 1, "AFRICA": 1, "WORLD": 1}
