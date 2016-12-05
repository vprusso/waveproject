from django.test import TestCase, Client
from .forms import UploadFileForm
from django.core.files.uploadedfile import SimpleUploadedFile

from .utils import SanitizeInput, CurrencyHelper

import os
import csv
import unittest


class TestCurrency(unittest.TestCase):

    def setUp(self):

        self.sanitize = SanitizeInput()
        self.currency_helper = CurrencyHelper()

    def test_currency_well_formed(self):
        test_well_formed_1 = self.sanitize.sanitize_float_format('123.00')
        test_well_formed_2 = self.sanitize.sanitize_float_format('1234.00')
        test_well_formed_3 = self.sanitize.sanitize_float_format('12345.00')

        self.assertEqual(
            test_well_formed_1,
            12300
        )

        self.assertEqual(
            test_well_formed_2,
            123400
        )

        self.assertEqual(
            test_well_formed_3,
            1234500
        )

    def test_currency_dollar_sign(self):
        test_dollar_sign = self.sanitize.sanitize_float_format('$350.00')

        self.assertEqual(
            test_dollar_sign,
            35000
        )

    def test_currency_no_decimal(self):
        test_no_decimal = self.sanitize.sanitize_float_format('350')

        self.assertEqual(
            test_no_decimal,
            35000
        )

    def test_currency_comma(self):
        test_comma = self.sanitize.sanitize_float_format('1,999.00')

        self.assertEqual(
            test_comma,
            199900
        )


class TestParseCSV(unittest.TestCase):

    def setUp(self):

        self.sanitize = SanitizeInput()
        self.currency_helper = CurrencyHelper()

        self.data_well_formed = (
            os.getcwd() +
            r'\upload\static\test_data\test_data_well_formed.csv'
        )

        self.data_invalid_currency = (
            os.getcwd() +
            r'\upload\static\test_data\test_data_invalid_currency.csv'
        )

    def test_csv_read_headers(self):

        with open(self.data_well_formed, newline='') as f:
            reader = csv.reader(f)
            header_row = next(reader)

            self.assertEqual(
                header_row,
                ['date', 'category', 'employee name', 'employee address',
                 'expense description', 'pre-tax amount',
                 'tax name', 'tax amount']
            )

        with open(self.data_invalid_currency, newline='') as f:
            reader = csv.reader(f)
            header_row = next(reader)

            self.assertEqual(
                header_row,
                ['date', 'category', 'employee name', 'employee address',
                 'expense description', 'pre-tax amount',
                 'tax name', 'tax amount']
            )

    def test_csv_invalid_currency(self):
        reader = csv.DictReader(open(self.data_invalid_currency))
        for row in reader:
            ptax = self.sanitize.sanitize_float_format(row['pre-tax amount'])
            

    def test_csv_tax_amount(self):
        pass


if __name__ == '__main__':
    unittest.main()
