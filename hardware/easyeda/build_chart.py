"""Build editable EasyEDA Standard sheets from the provisional module pin matrix."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COUNTER = 0


def uid():
    global COUNTER
    COUNTER += 1
    return f"gge{COUNTER}"


def text(x, y, value, size=11, color="#172B4D", kind="L"):
    assert not any(c in value for c in "~`\n")
    return f"T~{kind}~{x}~{y}~0~{color}~Arial~{size}pt~~~~comment~{value}~1~start~{uid()}~0"


def rect(x, y, w, h, color="#334155", fill="none"):
    return f"R~{x}~{y}~~~{w}~{h}~{color}~1~0~{fill}~{uid()}~0"


def pin(x, y, label, number, side):
    delta = 20 if side == "left" else -20
    anchor = "start" if side == "left" else "end"
    return (f"P~show~0~{number}~{x}~{y}~{180 if side == 'left' else 0}~{uid()}~0"
            f"^^{x}~{y}^^M {x} {y} h {delta}~#334155"
            f"^^1~{x+delta+(5 if delta>0 else -5)}~{y+4}~0~{label}~{anchor}~~9pt"
            f"^^0~{x}~{y-4}~0~{number}~{anchor}~~7pt^^0~{x}~{y}^^0~M {x} {y}")


def symbol(c):
    x, y, w = c["x"], c["y"], c.get("width", 260)
    h = max(len(c["left"]), len(c["right"])) * 30 + 65
    parts = [f"LIB~{x}~{y}~package`NONE`Manufacturer Part`{c['model']}`spicePre`U`~~0~{uid()}~~~0~~yes~yes",
             text(x, y-28, c["ref"], 12, kind="P"),
             text(x, y-10, c["model"], 10, kind="N"), rect(x, y, w, h, c.get("color", "#334155"))]
    stubs = []
    for side in ("left", "right"):
        for i, (label, number, net) in enumerate(c[side]):
            px = x-20 if side == "left" else x+w+20
            py = y+30+i*30
            parts.append(pin(px, py, label, number, side))
            if net is not None:
                end = px-85 if side == "left" else px+85
                stubs.append(f"W~{px} {py} {end} {py}~#008800~1~0~none~{uid()}~0")
                stubs.append(f"N~{end}~{py}~0~#075985~{net}~{uid()}~{'end' if side == 'left' else 'start'}~{end}~{py-5}~Arial~9pt~0")
            else:
                # A deliberately open engineering boundary, not an ERC no-connect waiver.
                stubs.append(text(px-5, py-9, "OPEN", 8, "#B91C1C"))
    return ["#@$".join(parts), *stubs]


def build():
    global COUNTER
    COUNTER = 0
    model = json.loads((ROOT/"design.json").read_text())
    project = {"editorVersion": "6.5.60", "docType": "5", "title": "ResQ-Vision - provisional electrical chart", "description": "Candidate parts only; no fabrication or physical safety validation.", "colors": {}, "schematics": []}
    rows = []
    for index, sheet in enumerate(model["sheets"], 1):
        shapes = [rect(0, 0, 1590, 1040), text(30, 40, "ResQ-Vision / " + sheet["title"], 20),
                  text(30, 69, "PROVISIONAL CANDIDATES - confirm class hardware before wiring", 13, "#B91C1C"),
                  text(30, 95, "Native module symbols / named nets / no PCB footprints / Rev P1 / 2026-10-19", 10)]
        for c in sheet["components"]:
            shapes.extend(symbol(c))
            for side in ("left", "right"):
                rows.extend([index, c["ref"], c["model"], p[1], p[0], p[2] or "OPEN", "provisional"] for p in c[side])
        for i, note in enumerate(sheet["notes"]):
            shapes.append(text(35, 880+i*24, note, 11, "#334155"))
        shapes.append(text(35, 1020, f"Sheet {index}/{len(model['sheets'])} - Source: design.json and docs/hardware/electrical-chart.md", 9))
        project["schematics"].append({"docType": "1", "title": sheet["title"], "description": "Provisional module interconnect", "dataStr": {"head": {"docType": "1", "editorVersion": "6.5.60", "newgId": True, "c_para": {"Prefix Start": "1"}, "c_spiceCmd": None}, "canvas": "CA~1600~1050~#FFFFFF~none~#CCCCCC~5~1600~1050~line~5~pixel~5~0~0", "shape": shapes, "BBox": {"x": 0, "y": 0, "width": 1590, "height": 1040}, "colors": {}}})
    (ROOT/"resq-vision-electrical.json").write_text(json.dumps(project, indent=2)+"\n")
    with (ROOT/"pin-matrix.csv").open("w") as f:
        writer = csv.writer(f)
        writer.writerow(["sheet", "reference", "candidate_model", "pin_id", "function", "net", "status"])
        writer.writerows(rows)
    return project


if __name__ == "__main__":
    build()
