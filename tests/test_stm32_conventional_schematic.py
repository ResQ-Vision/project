"""Check serialized electrical nets and sensor coverage; no physical validation."""
import json
from pathlib import Path
import unittest
from test_stm32_electrical_chart import topology

BASE=Path(__file__).resolve().parents[1]/'hardware/easyeda-stm32'


class ConventionalSchematicTests(unittest.TestCase):
    def setUp(self):
        self.project=json.loads((BASE/'resq-vision-stm32-schematic.json').read_text())
        self.manifest=json.loads((BASE/'schematic-manifest.json').read_text())
        self.pins,self.connections=topology(self.project)

    def test_motor_and_encoder_functions_do_not_cross(self):
        for side in ['L','R']:
            for function in ['M+','M-','VCC','GND','A','B']:
                self.assertIn(frozenset((('U1',f'{side}_{function}'),(f'M_{side}',function))),self.connections)
        self.assertEqual(len(self.connections),17)

    def test_servo_has_three_separate_nets_and_no_assumed_battery_supply(self):
        for a,b in [('SERVO_SIGNAL','SIG'),('SERVO_SUPPLY','SUPPLY'),('SERVO_RETURN','RETURN')]:
            self.assertIn(frozenset((('U1',a),('SV1',b))),self.connections)
        names=[s.split('~')[5] for s in self.project['schematics'][0]['dataStr']['shape'] if s.startswith('N~')]
        self.assertEqual(len(names),17)
        self.assertEqual(len(set(names)),17)
        self.assertIn('SERVO_RAIL_TBD',names)
        self.assertIn('BAT_IN',names)

    def test_all_baseline_sensors_present_without_fake_physical_interfaces(self):
        self.assertEqual(set(self.manifest['sensors']),{'L1','CAM1','U1:onboard IMU','M_L:encoder','M_R:encoder','S_F','S_R'})
        refs={c['ref'] for c in self.manifest['components']}
        self.assertTrue({'L1','CAM1','S_F','S_R','M_L','M_R','U1','C3','PC1'}<=refs)
        connected={p for c in self.connections for p in c}
        self.assertFalse(any(ref in ['L1','CAM1','S_F','S_R','C3','PC1'] for ref,_ in connected))
        for ref,ident in [('L1','DATA_TBD'),('L1','POWER_TBD'),('CAM1','POWER_TBD'),('S_F','A'),('S_R','B')]:
            self.assertIn((ref,ident),self.pins.values())
        self.assertFalse(self.manifest['physical_pinout_approved'])
        text=json.dumps(self.project)
        self.assertIn('ONBOARD IMU',text)
        for stale in ['Raspberry','RPLIDAR A1','LSM6DSOX','MDD10A','ToF','cliff']:
            self.assertNotIn(stale,text)


if __name__=='__main__':unittest.main()
