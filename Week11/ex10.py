from a2 import *
import unittest


class TestSetByPos(unittest.TestCase):

    def test_01_set_returns_none(self):
        subject1 = Female('test_subject_1')
        # try setting by position
        result = subject1.set_by_pos(1, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_02_get_by_pos_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        result = subject1.get_by_pos(1, 5)
        expected = 'AT'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_03_set_marker_returns_none(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        result = subject1.set_marker('sad123', 1, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")

    def test_04_set_by_marker_returns_none(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        subject1.set_marker('sad123', 1, 5)
        result = subject1.set_by_marker('sad123', 'GC')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_05_get_by_pos_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        subject1.set_marker('sad123', 1, 5)
        subject1.set_by_marker('sad123', 'GC')
        result = subject1.get_by_pos(1, 5)
        expected = 'GC'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_06_get_by_marker_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_by_pos(1, 5, 'AT')
        subject1.set_marker('sad123', 1, 5)
        subject1.set_by_marker('sad123', 'GC')
        result = subject1.get_by_marker('sad123')
        expected = 'GC'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_07_set_marker_returns_none(self):
        subject1 = Female('test_subject_1')
        result = subject1.set_marker('123456', 10, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")

    def test_08_get_by_pos_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        result = subject1.get_by_pos(10, 5)
        expected = ''
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_09_get_by_marker_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        result = subject1.get_by_marker('123456')
        expected = ''
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_01_set_returns_none(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        result = subject1.set_by_pos(10, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_08_get_by_pos_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        result = subject1.get_by_pos(10, 5)
        expected = 'AT'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_09_get_by_marker_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        result = subject1.get_by_marker('123456')
        expected = 'AT'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_10_set_by_marker_returns_none(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        result = subject1.set_by_marker('123456', 'GC')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_11_get_by_pos_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        subject1.set_by_marker('123456', 'GC')
        result = subject1.get_by_pos(10, 5)
        expected = 'GC'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_12_get_by_marker_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        subject1.set_by_marker('123456', 'GC')
        result = subject1.get_by_marker('123456')
        expected = 'GC'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

    def test_13_set_returns_none(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        subject1.set_by_marker('123456', 'GC')
        result = subject1.set_by_pos(10, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_14_get_by_marker_returns_nucleotide(self):
        subject1 = Female('test_subject_1')
        subject1.set_marker('123456', 10, 5)
        subject1.set_by_pos(10, 5, 'AT')
        subject1.set_by_marker('123456', 'GC')
        subject1.set_by_pos(10, 5, 'AT')
        result = subject1.get_by_marker('123456')
        expected = 'AT'
        self.assertEqual(result, expected,
                         str(result) + ' is not ' + str(expected))

if(__name__ == "__main__"):
    unittest.main(exit=False)
