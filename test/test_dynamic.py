import time
import unittest

from bili_api.dynamic.dynamic_api import Dynamics


class TestDynamic(unittest.TestCase):
    def test_dynamic(self):
        dynamics = Dynamics(434565011)

        for i, dynamic in enumerate(dynamics):
            print(dynamic)
            if i == 100:
                break
            time.sleep(.1)


if __name__ == "__main__":
    unittest.main()
