import unittest
from beguidcalc import get_beguid


class BasicsTestCase(unittest.TestCase):
    beguid = "d4d20ab6f6e413c129a2bcbaa17677e5"

    def test_corrent_calc(self):
        calc = get_beguid(76561198057447143)
        self.assertEqual(self.beguid, calc)

    def test_incorrent_calc(self):
        calc = get_beguid(76561198057447142)
        self.assertNotEqual(self.beguid, calc)

if __name__ == '__main__':
    unittest.main()
