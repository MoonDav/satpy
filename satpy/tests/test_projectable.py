#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""test projectable objects.
"""

import unittest
from satpy import projectable
import numpy as np
import sys
import mock

class TestDataset(unittest.TestCase):
    """
    Test the dataset class
    """

    def test_copy(self):
        """
        Test copying a dataset
        """
        ds = projectable.Dataset(np.arange(8), foo="bar")
        ds_copy = ds.copy()
        self.assertTrue(ds_copy.data is not ds.data
                     and all(ds.data == ds_copy.data))
        if sys.version >= "2.7":
            self.assertDictEqual(ds.info, ds_copy.info)

    def test_str_repr(self):
        ds = projectable.Dataset(np.arange(1, 25), foo="bar")
        ds_str = str(ds)
        ds_repr = repr(ds)

    def test_add(self):
        """Checks the __add__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 0, 0], bla=2, bli='hoj')
        c = a + b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a + 1
        self.assertDictEqual(c.info, a.info)
        c = 1 + a
        self.assertDictEqual(c.info, a.info)
        a += b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b += 1
        self.assertDictEqual(b.info, b_info)

    def test_sub(self):
        """Checks the __sub__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 0, 0], bla=2, bli='hoj')
        c = a - b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a - 1
        self.assertDictEqual(c.info, a.info)
        c = 1 - a
        self.assertDictEqual(c.info, a.info)
        a -= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b -= 1
        self.assertDictEqual(b.info, b_info)

    def test_mul(self):
        """Checks the __mul__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 0, 0], bla=2, bli='hoj')
        c = a * b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a * 1
        self.assertDictEqual(c.info, a.info)
        c = 1 * a
        self.assertDictEqual(c.info, a.info)
        a *= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b *= 1
        self.assertDictEqual(b.info, b_info)

    def test_floordiv(self):
        """Checks the __floordiv__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a // b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a // 1
        self.assertDictEqual(c.info, a.info)
        c = 1 // a
        self.assertDictEqual(c.info, a.info)
        a //= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b //= 1
        self.assertDictEqual(b.info, b_info)

    def test_mod(self):
        """Checks the __mod__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a % b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a % 1
        self.assertDictEqual(c.info, a.info)
        c = 1 % a
        self.assertDictEqual(c.info, a.info)
        a %= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b %= 1
        self.assertDictEqual(b.info, b_info)

    def test_divmod(self):
        """Checks the __divmod__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = divmod(a, b)
        self.assertDictEqual(c[0].info, {'bla': 2})
        self.assertDictEqual(c[1].info, {'bla': 2})
        c = divmod(a, 1)
        self.assertDictEqual(c[0].info, a.info)
        self.assertDictEqual(c[1].info, a.info)
        c = divmod(1, a)
        self.assertDictEqual(c[0].info, a.info)
        self.assertDictEqual(c[1].info, a.info)

    def test_pow(self):
        """Checks the __pow__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a ** b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a ** 1
        self.assertDictEqual(c.info, a.info)
        c = 1 ** a
        self.assertDictEqual(c.info, a.info)
        a **= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b **= 1
        self.assertDictEqual(b.info, b_info)

    def test_lshift(self):
        """Checks the __lshift__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a << b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a << 1
        self.assertDictEqual(c.info, a.info)
        c = 1 << a
        self.assertDictEqual(c.info, a.info)
        a <<= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b <<= 1
        self.assertDictEqual(b.info, b_info)

    def test_rshift(self):
        """Checks the __rshift__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a >> b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a >> 1
        self.assertDictEqual(c.info, a.info)
        c = 1 >> a
        self.assertDictEqual(c.info, a.info)
        a >>= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b >>= 1
        self.assertDictEqual(b.info, b_info)

    def test_and(self):
        """Checks the __and__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a & b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a & 1
        self.assertDictEqual(c.info, a.info)
        c = 1 & a
        self.assertDictEqual(c.info, a.info)
        a &= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b &= 1
        self.assertDictEqual(b.info, b_info)

    def test_xor(self):
        """Checks the __xor__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a ^ b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a ^ 1
        self.assertDictEqual(c.info, a.info)
        c = 1 ^ a
        self.assertDictEqual(c.info, a.info)
        a ^= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b ^= 1
        self.assertDictEqual(b.info, b_info)

    def test_or(self):
        """Checks the __or__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a | b
        self.assertDictEqual(c.info, {'bla': 2})
        c = a | 1
        self.assertDictEqual(c.info, a.info)
        c = 1 | a
        self.assertDictEqual(c.info, a.info)
        a |= b
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b |= 1
        self.assertDictEqual(b.info, b_info)

    @unittest.skipIf(sys.version_info >= (3, 0),
                     "Not needed in python 3")
    def test_div(self):
        """Checks the __div__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        b = projectable.Dataset([2, 1, 1], bla=2, bli='hoj')
        c = a.__div__(b)
        self.assertDictEqual(c.info, {'bla': 2})
        c = a.__div__(1)
        self.assertDictEqual(c.info, a.info)
        c = a.__rdiv__(1)
        self.assertDictEqual(c.info, a.info)
        a = a.__idiv__(b)
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b = b.__idiv__(1)
        self.assertDictEqual(b.info, b_info)

    def test_truediv(self):
        """Checks the __truediv__ function.
        """
        a = projectable.Dataset([7., 3., 1.], bla=2, blu='hej')
        b = projectable.Dataset([2., 1., 1.], bla=2, bli='hoj')
        c = a.__truediv__(b)
        self.assertDictEqual(c.info, {'bla': 2})
        c = a.__truediv__(1)
        self.assertDictEqual(c.info, a.info)
        c = a.__rtruediv__(1)
        self.assertDictEqual(c.info, a.info)
        a = a.__itruediv__(b)
        self.assertDictEqual(a.info, {'bla': 2})
        b_info = b.info.copy()
        b = b.__itruediv__(1)
        self.assertDictEqual(b.info, b_info)

    def test_neg(self):
        """Checks the __neg__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        c = -a
        self.assertDictEqual(c.info, a.info)

    def test_pos(self):
        """Checks the __pos__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        c = +a
        self.assertDictEqual(c.info, a.info)

    def test_abs(self):
        """Checks the __abs__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        c = abs(a)
        self.assertDictEqual(c.info, a.info)

    def test_invert(self):
        """Checks the __invert__ function.
        """
        a = projectable.Dataset([7, 3, 1], bla=2, blu='hej')
        c = ~a
        self.assertDictEqual(c.info, a.info)


class TestProjectable(unittest.TestCase):
    """
    Test the projectable class
    """
    def test_init(self):
        """
        Test initialization
        """
        self.assertTrue('name' in projectable.Projectable([]).info)

    def test_isloaded(self):
        """
        Test isloaded method
        """
        self.assertFalse(projectable.Projectable([]).is_loaded())
        self.assertTrue(projectable.Projectable(data=1).is_loaded())

    def test_str(self):
        # FIXME: Is there a better way to fake the area?
        class FakeArea(object):
            name = "fake_area"

        # Normal situation
        p = projectable.Projectable(np.arange(25),
                                    sensor="fake_sensor",
                                    wavelength_range=500,
                                    resolution=250,
                                    fake_attr="fakeattr",
                                    area=FakeArea(),
                                    )
        p_str = str(p)

        # Not loaded data
        p = projectable.Projectable([])
        p_str = str(p)
        self.assertTrue("not loaded" in p_str)

        # Data that doesn't have a shape
        p = projectable.Projectable(data=tuple())
        p_str = str(p)

    @mock.patch('satpy.resample.resample')
    def test_resample_2D(self, mock_resampler):
        data = np.arange(25).reshape((5, 5))
        mock_resampler.return_value = data
        p = projectable.Projectable(data)

        class FakeAreaDef:
            def __init__(self, name):
                self.name = name

        source_area = FakeAreaDef("here")
        destination_area = FakeAreaDef("there")
        p.info["area"] = source_area
        res = p.resample(destination_area)
        self.assertEqual(mock_resampler.call_count, 1)
        self.assertEqual(mock_resampler.call_args[0][0], source_area)
        self.assertEqual(mock_resampler.call_args[0][2], destination_area)
        np.testing.assert_array_equal(data, mock_resampler.call_args[0][1])
        self.assertTrue(isinstance(res, projectable.Projectable))
        np.testing.assert_array_equal(res.data, mock_resampler.return_value)

    @mock.patch('satpy.resample.resample')
    def test_resample_3D(self, mock_resampler):
        data = np.arange(75).reshape((3, 5, 5))
        mock_resampler.return_value = np.rollaxis(data, 0, 3)
        p = projectable.Projectable(data)

        class FakeAreaDef:
            def __init__(self, name):
                self.name = name

        source_area = FakeAreaDef("here")
        destination_area = FakeAreaDef("there")
        p.info["area"] = source_area
        res = p.resample(destination_area)
        self.assertTrue(mock_resampler.called)
        self.assertEqual(mock_resampler.call_args[0][0], source_area)
        np.testing.assert_array_equal(np.rollaxis(data, 0, 3), mock_resampler.call_args[0][1])
        self.assertEqual(mock_resampler.call_args[0][2], destination_area)
        self.assertTrue(isinstance(res, projectable.Projectable))
        np.testing.assert_array_equal(res.data, data)


def suite():
    """The test suite for test_projector.
    """
    loader = unittest.TestLoader()
    my_suite = unittest.TestSuite()
    my_suite.addTest(loader.loadTestsFromTestCase(TestDataset))
    my_suite.addTest(loader.loadTestsFromTestCase(TestProjectable))

    return my_suite
