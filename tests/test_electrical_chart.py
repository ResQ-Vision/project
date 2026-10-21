"""Regression checks for electrical hazards in the serialized planning chart."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read_connections(project=None):
    """Recover nets from actual EasyEDA pins, wire endpoints and net labels."""
    if project is None:
        project = json.loads((ROOT/'hardware/easyeda/resq-vision-electrical.json').read_text())
    result = {}
    for sheet in project['schematics']:
        shapes = sheet['dataStr']['shape']
        labels = {}
        wires = []
        for shape in shapes:
            fields = shape.split('~')
            if fields[0] == 'N':
                labels[(fields[1], fields[2])] = fields[5]
            if fields[0] == 'W':
                coords = fields[1].split()
                wires.append(((coords[0], coords[1]), (coords[-2], coords[-1])))
        for shape in shapes:
            if not shape.startswith('LIB~'):
                continue
            primitives = shape.split('#@$')[1:]
            ref = next(p.split('~')[12] for p in primitives if p.startswith('T~P~'))
            pins = {}
            for primitive in primitives:
                if not primitive.startswith('P~'):
                    continue
                sections = primitive.split('^^')
                fields = sections[0].split('~')
                point = tuple(sections[1].split('~'))
                connected = {labels[b] for a, b in wires if a == point and b in labels}
                connected |= {labels[a] for a, b in wires if b == point and a in labels}
                if len(connected) > 1:
                    raise AssertionError(f'{ref}.{fields[3]} bridges {connected}')
                pins[fields[3]] = next(iter(connected), None)
            result[ref] = pins
    return project, result


class ElectricalChartTests(unittest.TestCase):
    def setUp(self):
        self.project, self.pins = read_connections()

    def test_all_documented_pins_have_their_serialized_net(self):
        model = json.loads((ROOT/'hardware/easyeda/design.json').read_text())
        for sheet in model['sheets']:
            for c in sheet['components']:
                expected = {p[1]: p[2] for p in c['left']+c['right']}
                self.assertEqual(self.pins[c['ref']], expected, c['ref'])

    def test_encoder_5v_never_reaches_esp_directly(self):
        self.assertEqual(self.pins['U4']['14'], '3V3_LOGIC')
        channels = [('2','3','J2.5','ENC_L_A'),('5','6','J2.6','ENC_L_B'),
                    ('9','8','J2.3','ENC_R_A'),('12','11','J2.4','ENC_R_B')]
        for input_pin, output_pin, gpio, name in channels:
            self.assertEqual(self.pins['U4'][input_pin], name+'_5V')
            self.assertEqual(self.pins['U4'][output_pin], name)
            self.assertEqual(self.pins['U1'][gpio], name)
        self.assertFalse(any(n and n.endswith('_5V') for n in self.pins['U1'].values()))
        for motor in ['M1','M2']:
            self.assertEqual(self.pins[motor]['Blue encoder VCC'], '5V_LOGIC')

    def test_power_boundaries_remain_explicit(self):
        self.assertEqual(set(self.pins['B1'].values()), {None})
        self.assertEqual(set(self.pins['S0'].values()), {None})
        self.assertEqual(self.pins['U3']['PWR+'], 'VMOTOR_SW')
        self.assertEqual(self.pins['SV1']['V+'], '5V_ACT')
        self.assertEqual(self.pins['U6']['5'], '5V_ACT')
        self.assertTrue(set(self.pins['U8'].values()).isdisjoint(self.pins['U1'].values()))
        self.assertTrue(set(self.pins['L1'].values()).isdisjoint(self.pins['U1'].values()))
        safety = self.project['schematics'][0]['dataStr']['shape']
        self.assertTrue(any('UNRESOLVED safety power stage' in x for x in safety))

    def test_steering_translation_and_contacts(self):
        self.assertEqual(self.pins['U6']['2'], 'STEER_3V3')
        self.assertEqual(self.pins['U6']['4'], 'STEER_5V')
        self.assertEqual(self.pins['SV1']['SIGNAL'], 'STEER_5V')
        for ref, net in [('R1','CONTACT_FRONT'),('R2','CONTACT_REAR')]:
            self.assertEqual(self.pins[ref], {'1':'3V3_LOGIC','2':net})


if __name__ == '__main__':
    unittest.main()
