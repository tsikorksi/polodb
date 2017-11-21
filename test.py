import unittest2
import encrypt
from forms import InternalMethods, Stats
from web import Validation
i = InternalMethods
v = Validation


class FormsTest(unittest2.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(i.bubble_sort(['8', '7', '1']), ['1', '7', '8'])
        self.assertRaises(TypeError, i.bubble_sort(['8', '7', 'a']))
        self.assertEqual(i.bubble_sort(['0', '99999', '1']), ['0', '1', '99999'])

    def test_split(self):
        self.assertEqual(i.split('a.bb.ccc.dddd.'), ['a', 'bb', 'ccc', 'dddd'])
        self.assertRaises(TypeError, i.split)
        self.assertEqual(i.split('ooooo'), [])

    def test_maths(self):
        self.assertEqual(i.maths([4, 6, 2, 4, 0, 8], 4), (3.0, 8, 4, 2.5819888974716116))
        errors = IndexError, ZeroDivisionError
        with self.assertRaises(errors):
            i.maths([], 0)

    def test_double_var(self):
        self.assertEqual(Stats.double_variable_stats('dora', 'eric', 0), (0, 0, 0, 0, 0, True))
        self.assertAlmostEqual(Stats.double_variable_stats('eric', 'dora', 2),
                               (3.3333333333333335, 4, 4, 2, 0.9428090415820626, False), 3)

    def test_single_var(self):
        self.assertAlmostEqual(Stats.single_variable_stats('eric', 0),
                               (4.96969696969697, 5, 8, 1, 2.0814454255847754, False), 3)
        self.assertEqual(Stats.single_variable_stats('dora', 0), (0, 0, 0, 0, 0, True))


class EncryptTest(unittest2.TestCase):
    def test_shift_encode(self):
        self.assertEqual(encrypt.shift_encode('testcasedefault', 5),
                         ['y', 'j', 'x', 'y', 'h', 'f', 'x', 'j', 'i', 'j', 'k', 'f', 'z', 'q', 'y'])
        self.assertEqual(encrypt.shift_encode('!@#$%^&*(){}_+<>', 1209),
                         ['.', 'M', '0', '1', '2', 'k', '3', '7', '5', '6', '\x88', '\x8a', 'l', '8', 'I', 'K'])
        self.assertRaises(TypeError, encrypt.shift_encode)

    def test_shift_decode(self):
        self.assertEqual(encrypt.shift_decode('yjxyhfxjijkfzqy', 5),
                         ['t', 'e', 's', 't', 'c', 'a', 's', 'e', 'd', 'e', 'f', 'a', 'u', 'l', 't'])
        self.assertEqual(encrypt.shift_decode('.M012k3756\x88\x8al8IK', 1209),
                         ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '_', '+', '<', '>'])
        self.assertRaises(TypeError, encrypt.shift_decode)


class WebTest(unittest2.TestCase):
    def test_validate(self):
        self.assertEqual(v.validate('aa.aada.dqrrq.adadar.gsgwgwfafagg.adadagag.'), True)
        self.assertEqual(v.validate('..afgshsgagagag'), False)
        self.assertEqual(v.validate('daghsbwrshs.h.n.\n\x88.'), True)


if __name__ == '__main__':
    unittest2.main()
