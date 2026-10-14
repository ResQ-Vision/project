"""Build the Hebrew progress book by patching the retained Word template.

Standard library only; never modify the template or canonical engineering docs.
The manuscript supports headings, paragraphs, simple tables and a diagram marker.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'docs/school/project-book'
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
REL = 'http://schemas.openxmlformats.org/package/2006/relationships'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
PIC = 'http://schemas.openxmlformats.org/drawingml/2006/picture'
NS = {'w': W}
for prefix, uri in [('w', W), ('r', R), ('a', A), ('wp', WP), ('pic', PIC)]:
    ET.register_namespace(prefix, uri)


def el(tag, attrs=None, text=None):
    prefix, name = tag.split(':')
    uri = dict(w=W, r=R, a=A, wp=WP, pic=PIC)[prefix]
    node = ET.Element(f'{{{uri}}}{name}')
    for key, value in (attrs or {}).items():
        if ':' in key:
            p, k = key.split(':')
            key = f'{{{dict(w=W, r=R)[p]}}}{k}'
        node.set(key, str(value))
    node.text = text
    return node


def sub(node, tag, attrs=None, text=None):
    child = el(tag, attrs, text)
    node.append(child)
    return child


def set_prop(props, tag, value=None):
    old = props.find(f'w:{tag}', NS)
    if old is not None:
        props.remove(old)
    props.append(el('w:' + tag, {'w:val': value} if value is not None else {}))


def paragraph(text, prototype, heading=False):
    p = el('w:p')
    original = prototype.find('w:pPr', NS)
    props = copy.deepcopy(original) if original is not None else el('w:pPr')
    # Keep the source roles, but clear instruction-only numbering/page breaks.
    for tag in ['numPr', 'sectPr', 'pageBreakBefore']:
        old = props.find('w:' + tag, NS)
        if old is not None:
            props.remove(old)
    set_prop(props, 'bidi')
    set_prop(props, 'jc', 'right')
    if heading:
        set_prop(props, 'keepNext')
    else:
        # Template body rhythm (1.5 lines) with readable spacing, no stale indents.
        old = props.find('w:ind', NS)
        if old is not None:
            props.remove(old)
        spacing = props.find('w:spacing', NS)
        if spacing is None:
            spacing = sub(props, 'w:spacing')
        spacing.set(f'{{{W}}}after', '100')
        spacing.set(f'{{{W}}}line', '360')
        spacing.set(f'{{{W}}}lineRule', 'auto')
        set_prop(props, 'widowControl')
    p.append(props)
    # Split scripts so English names and punctuation render in their own direction.
    for chunk in re.split(r'([A-Za-z][A-Za-z0-9_./= *×]*[A-Za-z0-9]|[A-Za-z])', text):
        if not chunk:
            continue
        run = sub(p, 'w:r')
        rp = sub(run, 'w:rPr')
        sub(rp, 'w:rFonts', {'w:ascii': 'David', 'w:hAnsi': 'David', 'w:cs': 'David'})
        sub(rp, 'w:rtl', {'w:val': '0' if re.match('[A-Za-z]', chunk) else '1'})
        node = sub(run, 'w:t', text=chunk)
        node.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    return p


def table(rows, prototype, normal):
    t = el('w:tbl')
    props = copy.deepcopy(prototype.find('w:tblPr', NS))
    if props is None:
        props = el('w:tblPr')
    set_prop(props, 'bidiVisual')
    set_prop(props, 'tblLayout', 'fixed')
    width = props.find('w:tblW', NS)
    if width is None:
        width = sub(props, 'w:tblW')
    width.set(f'{{{W}}}w', '8306')
    width.set(f'{{{W}}}type', 'dxa')
    t.append(props)
    cols = len(rows[0])
    grid = sub(t, 'w:tblGrid')
    widths = [8306 // cols] * cols
    for width in widths:
        sub(grid, 'w:gridCol', {'w:w': width})
    for i, row in enumerate(rows):
        if len(row) != cols:
            raise ValueError('Inconsistent table column count')
        tr = sub(t, 'w:tr')
        trp = sub(tr, 'w:trPr')
        sub(trp, 'w:cantSplit')
        if i == 0:
            sub(trp, 'w:tblHeader')
        for text, width in zip(row, widths):
            tc = sub(tr, 'w:tc')
            tcp = sub(tc, 'w:tcPr')
            sub(tcp, 'w:tcW', {'w:w': width, 'w:type': 'dxa'})
            if i == 0:
                sub(tcp, 'w:shd', {'w:fill': 'EDEDED', 'w:val': 'clear'})
            margins = sub(tcp, 'w:tcMar')
            for side in ['top', 'left', 'bottom', 'right']:
                sub(margins, 'w:' + side, {'w:w': 80, 'w:type': 'dxa'})
            p = paragraph(text, normal)
            pp = p.find('w:pPr', NS)
            pp.find('w:spacing', NS).set(f'{{{W}}}line', '260')
            pp.find('w:spacing', NS).set(f'{{{W}}}after', '30')
            for rp in p.findall('w:r/w:rPr', NS):
                sub(rp, 'w:sz', {'w:val': 22})
                sub(rp, 'w:szCs', {'w:val': 22})
                if i == 0:
                    sub(rp, 'w:b')
                    sub(rp, 'w:bCs')
            tc.append(p)
    return t


def picture():
    # One unique inline object; no floating anchors or layout overlays.
    xml = f'''<w:p xmlns:w="{W}" xmlns:r="{R}" xmlns:wp="{WP}" xmlns:a="{A}" xmlns:pic="{PIC}">
    <w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:drawing><wp:inline>
    <wp:extent cx="5200000" cy="3510000"/><wp:docPr id="9001" name="ResQ system" descr="Conceptual architecture with one laptop, local safety, direct C3 and unresolved power"/>
    <a:graphic><a:graphicData uri="{PIC}"><pic:pic><pic:nvPicPr><pic:cNvPr id="9001" name="ResQ system"/><pic:cNvPicPr/></pic:nvPicPr>
    <pic:blipFill><a:blip r:embed="rIdResQBookDiagram"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
    <pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="5200000" cy="3510000"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
    </pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''
    return ET.fromstring(xml)


def build(output, page_map=None):
    mapping = json.loads((BOOK / 'source-map.json').read_text())
    template = BOOK / 'template.docx'
    if hashlib.sha256(template.read_bytes()).hexdigest() != mapping['template_sha256']:
        raise ValueError('Template fingerprint changed; distill the new reference first')
    if page_map is not None:
        manuscript_hash = hashlib.sha256((BOOK / 'book.md').read_bytes()).hexdigest()
        if page_map.get('_manuscript_sha256') != manuscript_hash:
            raise ValueError('Page map is stale; render the changed manuscript before caching page numbers')
    with zipfile.ZipFile(template) as archive:
        parts = {item.filename: archive.read(item.filename) for item in archive.infolist()}
        infos = archive.infolist()
    doc = ET.fromstring(parts['word/document.xml'])
    body = doc.find('w:body', NS)
    paragraphs = body.findall('w:p', NS)
    normal, h1, h2 = paragraphs[23], paragraphs[21], paragraphs[60]
    table_proto = body.find('w:tbl', NS)
    sect = copy.deepcopy(body.find('w:sectPr', NS))
    cover = [copy.deepcopy(p) for p in paragraphs[:21]]
    replacements = {
        0: '[שם בית הספר ולוגו להשלמה]', 3: 'ספר פרויקט ResQ Vision',
        5: 'פרויקט גמר במגמת', 8: 'בחלופת אינטרנט של הדברים',
        9: 'סמל שאלון 841589', 11: 'נושא שנתי: אינטרנט של הדברים',
        14: 'שם התלמיד: יותם משה    תעודת זהות: להשלמה בעותק ההגשה',
        15: 'שם השותף ותעודת זהות: להשלמה בעותק ההגשה',
        17: 'מנחה הפרויקט: להשלמה', 18: 'רכז המגמה: להשלמה',
        20: 'שנת הלימודים תשפ״ז    טיוטת התקדמות 14 באוקטובר 2026',
    }
    for index, text in replacements.items():
        old = cover[index]
        new = paragraph(text, old)
        set_prop(new.find('w:pPr', NS), 'jc', 'center')
        if index == 3:
            set_prop(new.find('w:pPr', NS), 'pStyle', 'a3')
            for rp in new.findall('w:r/w:rPr', NS):
                sub(rp, 'w:color', {'w:val': '000000'})
        cover[index] = new
    declaration = [copy.deepcopy(p) for p in paragraphs[21:41]]
    declaration.insert(1, paragraph('טיוטה בלבד. הטפסים שלהלן אינם חתומים ואינם מעידים על אישור או על כתיבה עצמאית מלאה. פירוט הסיוע מופיע ביומן AI.', normal))
    toc = el('w:sdt')
    content = sub(toc, 'w:sdtContent')
    toc_heading = paragraph('תוכן עניינים', h1, True)
    set_prop(toc_heading.find('w:pPr', NS), 'pageBreakBefore')
    # A real TOC field with updated visible cache, not obsolete template bookmarks.
    field_start = sub(content, 'w:p')
    for kind in ['begin']:
        sub(sub(field_start, 'w:r'), 'w:fldChar', {'w:fldCharType': kind})
    sub(sub(field_start, 'w:r'), 'w:instrText', text=' TOC \\o "1-1" \\h \\z \\u ')
    sub(sub(field_start, 'w:r'), 'w:fldChar', {'w:fldCharType': 'separate'})
    headings = ['הצהרת הלומד/ים'] + [line[2:] for line in (BOOK / 'book.md').read_text().splitlines() if line.startswith('# ')]
    if page_map is not None and any(not isinstance(page_map.get(title), int) or page_map[title] < 1 for title in headings):
        raise ValueError('Page map must include a positive rendered page number for every chapter')
    for title in headings:
        page = (page_map or {}).get(title)
        content.append(paragraph(f'{title}    {page if page is not None else ""}', normal))
    sub(sub(sub(content, 'w:p'), 'w:r'), 'w:fldChar', {'w:fldCharType': 'end'})
    for node in list(body):
        body.remove(node)
    body.extend(cover + declaration + [toc_heading, toc])
    lines = (BOOK / 'book.md').read_text().splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        if line.startswith('# '):
            p = paragraph(line[2:], h1, True)
            set_prop(p.find('w:pPr', NS), 'pageBreakBefore')
            body.append(p)
        elif line.startswith('## '):
            body.append(paragraph(line[3:], h2, True))
        elif line == '[[SYSTEM_DIAGRAM]]':
            body.append(picture())
        elif line.startswith('|'):
            rows = []
            while True:
                if not re.match(r'^\|[\s:|\-]+\|$', line):
                    rows.append([cell.strip() for cell in line.strip('|').split('|')])
                if i >= len(lines) or not lines[i].strip().startswith('|'):
                    break
                line = lines[i].strip()
                i += 1
            body.append(table(rows, table_proto, normal))
        else:
            body.append(paragraph(line, normal))
    body.append(sect)
    parts['word/document.xml'] = ET.tostring(doc, encoding='utf-8', xml_declaration=True)
    # Patch settings without round-tripping any unrelated bytes.
    settings = parts['word/settings.xml']
    flag = b'<w:updateFields w:val="true"/>'
    if re.search(rb'<w:updateFields\b[^>]*/>', settings):
        settings = re.sub(rb'<w:updateFields\b[^>]*/>', flag, settings)
    else:
        settings = settings.replace(b'</w:settings>', flag + b'</w:settings>')
    parts['word/settings.xml'] = settings
    rels = parts['word/_rels/document.xml.rels']
    relation = (f'<Relationship Id="rIdResQBookDiagram" Type="{R}/image" Target="media/resq-system.png"/>').encode()
    parts['word/_rels/document.xml.rels'] = rels.replace(b'</Relationships>', relation + b'</Relationships>')
    parts['word/media/resq-system.png'] = (BOOK / 'system-diagram.png').read_bytes()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for info in infos:
            archive.writestr(info, parts.pop(info.filename))
        for name, data in parts.items():
            archive.writestr(name, data)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=BOOK / 'resq-vision-book.docx')
    parser.add_argument('--page-map', type=Path, default=BOOK / 'page-map.json')
    args = parser.parse_args()
    pages = json.loads(args.page_map.read_text()) if args.page_map.exists() else None
    print(build(args.output, pages))
