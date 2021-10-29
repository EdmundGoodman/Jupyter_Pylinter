#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for the jupylint package
"""

from subprocess import check_output, CalledProcessError
from json.decoder import JSONDecodeError
import unittest

from .jupylint import Jupylint, OldJupyterVersionError


class ArgsBuilder:
    """A custom class to emulate the argparse Namespace object"""
    def __init__(self, in_file_name, out_file_name, save_file):
        """Initialise the class with the appropriate variables"""
        self.in_file_name = in_file_name
        self.out_file_name = out_file_name
        self.save_file = save_file


class TestCard(unittest.TestCase):
    def test_file_markdown_cells(self):
        """Check that no code is captured out of a pure markdown file"""
        json_content = Jupylint.get_json_content("./jupylint/test_files/markdown_cells.ipynb")
        # Assert that all 24 notebook cells are found
        self.assertEqual(24, len(json_content))
        code_content = Jupylint.get_code_content(json_content)
        # Assert that none of them are code cells
        self.assertEqual(0, len(code_content))

    def test_file_running_code(self):
        """Check that code is correctly captured from a file containing code"""
        json_content = Jupylint.get_json_content("./jupylint/test_files/running_code.ipynb")
        # Assert that all 28 notebook cells are found
        self.assertEqual(28, len(json_content))
        code_content = Jupylint.get_code_content(json_content)
        # Assert that some of them contain code
        self.assertGreater(len(code_content), 100)

    def test_file_old_format(self):
        """Check that old Jupyter formats are rejected"""
        err_occurred = False
        try:
            _ = Jupylint.get_json_content("./jupylint/test_files/running_code_old.ipynb")
        except OldJupyterVersionError:
            err_occurred = True
        self.assertTrue(err_occurred)

    def test_file_malformed(self):
        """Check that a malformed input file is correctly identified"""
        err_occurred = False
        try:
            _ = Jupylint.get_json_content("./jupylint/test_files/malformed.ipynb")
        except JSONDecodeError:
            err_occurred = True
        self.assertTrue(err_occurred)


    def test_stylish_code(self):
        """Check that a perfectly stylish file is not penalised"""
        args = ArgsBuilder(
            in_file_name=['./jupylint/test_files/stylish.ipynb'],
            out_file_name='out.py',
            save_file=False
        )
        results = Jupylint.execute(args)
        self.assertTrue("Your code has been rated at 10.00/10" in results)

    def test_ugly_code(self):
        """Check that an ugle file is penalised"""
        args = ArgsBuilder(
            in_file_name=['./jupylint/test_files/running_code.ipynb'],
            out_file_name='out.py',
            save_file=False
        )
        results = Jupylint.execute(args)
        self.assertTrue("Your code has been rated at" in results)
        self.assertFalse("Your code has been rated at 10.00/10" in results)


    def test_params_default(self):
        pass

    def test_params_input_file_valid(self):
        pass

    def test_params_input_file_not_found(self):
        pass

    def test_params_output_file(self):
        pass

    def test_keep_code_file(self):
        pass


if __name__ == "__main__":
    unittest.main()
    print("All tests passed")
