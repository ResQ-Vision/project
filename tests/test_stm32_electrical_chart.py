"""Actual serialized terminal topology and architecture boundaries, not hardware tests."""
import json
from pathlib import Path
import unittest

BASE=Path(__file__).resolve().parents[1]/'hardware/easyeda-stm32'


def topology(project):
    sheet=project['schematics'][0]['dataStr']['shape']
    pins={}
    wires=[]
    for shape in sheet:
        if shape.startswith('LIB~'):
            ps=shape.split('#@$')[1:]
            ref=next(p.split('~')[12] for p in ps if p.startswith('T~P~'))
            for p in ps:
                if p.startswith('P~'):
                    bits=p.split('^^'); config=bits[0].split('~')
                    point=tuple(float(x) for x in bits[1].split('~'))
                    pins[point]=(ref,config[3])
        if shape.startswith('W~'):
            coords=[float(x) for x in shape.split('~')[1].split()]
            wires.append(((coords[0],coords[1]),(coords[-2],coords[-1])))
    connections=[]
    for a,b in wires:
        if a not in pins or b not in pins:
            raise AssertionError(f'Wire misses an editable terminal: {a} -> {b}')
        connections.append(frozenset((pins[a],pins[b])))
    return pins,connections


class STM32DrawingTests(unittest.TestCase):
    def setUp(self):
        self.project=json.loads((BASE/'resq-vision-stm32.json').read_text())
        self.manifest=json.loads((BASE/'drawing-manifest.json').read_text())
        self.pins,self.connections=topology(self.project)

    def test_each_rear_motor_harness_preserves_all_six_functions(self):
        for motor in ['M_L','M_R']:
            for name in ['M+','M-','VCC','GND','A','B']:
                self.assertIn(frozenset(((motor,f'{motor}_{name}'),('U1',f'BOARD_{motor}_{name}'))),self.connections)

    def test_servo_supply_and_signal_are_distinct(self):
        for board,servo in [('SERVO_SIGNAL','SIGNAL_WHITE'),('SERVO_SUPPLY','POWER_RED'),('SERVO_RETURN','RETURN_BLACK')]:
            self.assertIn(frozenset((('U1',board),('SV1',servo))),self.connections)
        self.assertEqual(len(self.connections),17)  # 12 harness + 3 servo + 2 input functions.

    def test_unassigned_contacts_and_radio_never_become_conductive_nets(self):
        connected={p for c in self.connections for p in c}
        self.assertFalse(any(ref in ['S_F','S_R','C3','CAM1','L1','PC1'] for ref,_ in connected))
        self.assertFalse(any(s.startswith('W~') for s in self.project['schematics'][1]['dataStr']['shape']))
        self.assertFalse(self.manifest['physical_pinout_approved'])
        self.assertEqual(self.manifest['open_checks'],list('ABCDEF'))

    def test_current_design_has_no_obsolete_candidate_hardware(self):
        models=' '.join(c['model'] for c in self.manifest['components'])
        for required in ['Hiwonder','STM32F407VET6','LD-1501MG','Likely JGB37-520R30-12']:
            self.assertIn(required,models)
        for stale in ['MDD10A','Pololu','HS-422','WROOM-32E','LSM6DSOX','SN74','RPLIDAR A1']:
            self.assertNotIn(stale,models)
        self.assertEqual(self.manifest['battery'],'existing / owner accepted')
        self.assertEqual(len(self.project['schematics']),2)


if __name__=='__main__':unittest.main()
