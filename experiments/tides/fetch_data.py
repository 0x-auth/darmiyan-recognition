#!/usr/bin/env python3
"""Download the exact NOAA record used in this test and verify it.

Station 9414290 (San Francisco), product hourly_height, datum MLLW, metric, GMT, all of 2023.
Writes noaa_9414290_sanfrancisco_2023_hourly.csv next to this script (8,760 rows + header).
"""
import calendar, hashlib, os, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "noaa_9414290_sanfrancisco_2023_hourly.csv")
SHA256 = "efa55a20565806f37581af083e9e77a7b4f4843819437a0ff58f04a7a7ff2f42"
URL = ("https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=hourly_height"
       "&application=darmiyan_test&begin_date=2023{m:02d}01&end_date=2023{m:02d}{d}"
       "&datum=MLLW&station=9414290&time_zone=gmt&units=metric&format=csv")

lines = []
for m in range(1, 13):
    d = calendar.monthrange(2023, m)[1]
    txt = urllib.request.urlopen(URL.format(m=m, d=d), timeout=60).read().decode().splitlines()
    if not lines:
        lines.append(txt[0])
    lines += txt[1:]
data = ("\n".join(lines) + "\n").encode()
open(OUT, "wb").write(data)
h = hashlib.sha256(data).hexdigest()
print(f"wrote {OUT}: {len(lines)-1} rows, sha256 {h}")
print("MATCHES the record used in the test" if h == SHA256 else
      "WARNING: differs from the record used in the test (NOAA may have revised the data)")
