"""Synthetic contract examples; no robot/hardware/model execution."""
import json
from pathlib import Path
import unittest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]

class ProposedContractTests(unittest.TestCase):
    def test_schemas_are_valid_and_explicitly_proposed(self):
        paths = list((ROOT / 'contracts').rglob('*.schema.json'))
        self.assertEqual(len(paths), 6)
        for path in paths:
            with self.subTest(schema=path.name):
                schema = json.loads(path.read_text())
                Draft202012Validator.check_schema(schema)
                self.assertEqual(schema['x-status'], 'proposed')
                self.assertTrue(schema['x-owner'])

    def test_valid_and_failure_examples(self):
        for filename, expected in [('contracts-valid.json', True), ('contracts-invalid.json', False)]:
            cases = json.loads((ROOT / 'tests/fixtures' / filename).read_text())
            for case in cases:
                with self.subTest(case=case['name']):
                    schema = json.loads((ROOT / 'contracts' / case['schema']).read_text())
                    errors = list(Draft202012Validator(schema).iter_errors(case['data']))
                    self.assertEqual(not errors, expected, '\n'.join(e.message for e in errors))

if __name__ == '__main__':
    unittest.main()
