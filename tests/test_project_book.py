"""Document-generation regressions; these do not test rover hardware."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / 'docs/school/project-book'
SPEC = importlib.util.spec_from_file_location('book_builder', ROOT / 'scripts/build_project_book.py')
BUILDER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILDER)
NS = BUILDER.NS


class ProjectBookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.output = Path(cls.temp.name) / 'book.docx'
        cls.pages = json.loads((BOOK / 'page-map.json').read_text()) if (BOOK / 'page-map.json').exists() else None
        BUILDER.build(cls.output, cls.pages)
        with zipfile.ZipFile(BOOK / 'template.docx') as z:
            cls.source = {n: z.read(n) for n in z.namelist()}
        with zipfile.ZipFile(cls.output) as z:
            cls.final = {n: z.read(n) for n in z.namelist()}
        cls.doc = ET.fromstring(cls.final['word/document.xml'])

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_preserve_template_parts_and_geometry(self):
        editable = {'word/document.xml', 'word/settings.xml', 'word/_rels/document.xml.rels'}
        for name, content in self.source.items():
            if name not in editable:
                self.assertEqual(content, self.final[name], name)
        original = ET.fromstring(self.source['word/document.xml'])
        self.assertEqual(
            ET.tostring(original.find('w:body/w:sectPr', NS)),
            ET.tostring(self.doc.find('w:body/w:sectPr', NS)),
        )
        expected = json.loads((BOOK / 'source-map.json').read_text())['template_sha256']
        self.assertEqual(expected, hashlib.sha256((BOOK / 'template.docx').read_bytes()).hexdigest())

    def test_manuscript_coverage_and_no_template_examples(self):
        texts = [''.join(p.itertext()) for p in self.doc.findall('.//w:p', NS)]
        joined = '\n'.join(texts)
        for line in (BOOK / 'book.md').read_text().splitlines():
            if line and not line.startswith('|') and line != '[[SYSTEM_DIAGRAM]]':
                self.assertIn(line.removeprefix('## ').removeprefix('# '), texts)
        for example in ['readTemperature()', 'sendIoTData()', 'DS18B20', '10/11/2026', 'Gemini (Version 3.5)']:
            self.assertNotIn(example, joined)
        for boundary in ['טיוטת התקדמות', 'לא מתועדים ניסויי נסיעה', 'אינה אישור לתנועה', 'לא משולב בבסיס הספר']:
            self.assertTrue(boundary in joined, f'Missing evidence boundary: {boundary}')

    def test_unsigned_declarations_and_toc_refresh(self):
        source = ET.fromstring(self.source['word/document.xml'])
        originals = source.find('w:body', NS).findall('w:p', NS)[21:41]
        final_texts = [''.join(p.itertext()) for p in self.doc.findall('.//w:p', NS)]
        for p in originals:
            text = ''.join(p.itertext())
            if text:
                self.assertIn(text, final_texts)
        fields = [x.text or '' for x in self.doc.findall('.//w:instrText', NS)]
        self.assertEqual(1, sum('TOC ' in x for x in fields))
        self.assertFalse(any('PAGEREF _Toc' in x for x in fields))
        self.assertIn(b'<w:updateFields w:val="true"/>', self.final['word/settings.xml'])

    def test_diagram_relation_and_rtl_table_safety(self):
        rels = ET.fromstring(self.final['word/_rels/document.xml.rels'])
        ids = [r.get('Id') for r in rels]
        self.assertEqual(len(ids), len(set(ids)))
        figure = [r for r in rels if r.get('Id') == 'rIdResQBookDiagram']
        self.assertEqual(1, len(figure))
        self.assertEqual((BOOK / 'system-diagram.png').read_bytes(), self.final['word/media/resq-system.png'])
        for table in self.doc.findall('.//w:tbl', NS):
            self.assertIsNotNone(table.find('w:tblPr/w:bidiVisual', NS))
            self.assertIsNotNone(table.find('w:tr/w:trPr/w:tblHeader', NS))
            for row in table.findall('w:tr', NS):
                self.assertIsNotNone(row.find('w:trPr/w:cantSplit', NS))

    def test_export_is_current_and_repeatable(self):
        with zipfile.ZipFile(BOOK / 'resq-vision-book.docx') as current:
            for part, data in self.final.items():
                self.assertEqual(data, current.read(part), part)

    def test_reject_stale_or_incomplete_page_cache(self):
        with self.assertRaisesRegex(ValueError, 'stale'):
            BUILDER.build(self.output, {'_manuscript_sha256': 'old'})
        with self.assertRaisesRegex(ValueError, 'every chapter'):
            BUILDER.build(self.output, {'_manuscript_sha256': hashlib.sha256((BOOK / 'book.md').read_bytes()).hexdigest()})


if __name__ == '__main__':
    unittest.main()
