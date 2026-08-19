import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from wicf_model import AirState, Doorway, door_open_load_kj, exchange_ramp_factor, humidity_ratio, moist_air_enthalpy_kj_per_kg_da


class WicfModelTests(unittest.TestCase):
    def test_humidity_ratio_is_positive_and_increases_with_rh(self):
        self.assertGreater(humidity_ratio(AirState(24, 80)), humidity_ratio(AirState(24, 40)))

    def test_warmer_moister_room_has_higher_enthalpy(self):
        self.assertGreater(moist_air_enthalpy_kj_per_kg_da(AirState(24, 50)), moist_air_enthalpy_kj_per_kg_da(AirState(2, 80)))

    def test_ramp_and_load_limits(self):
        door = Doorway(establishment_time_s=3)
        self.assertEqual(exchange_ramp_factor(0, 3), 0)
        self.assertAlmostEqual(exchange_ramp_factor(3, 3), 0.5)
        self.assertGreater(door_open_load_kj(AirState(24, 50), AirState(-18, 70), door, 60), door_open_load_kj(AirState(24, 50), AirState(-18, 70), door, 30))


if __name__ == "__main__":
    unittest.main()
