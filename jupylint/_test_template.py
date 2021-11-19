#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The template of the tests provided for the Jupylint package. Mostly used to
provide an outline to Sphinx autodoc of the testing functionality
"""

import unittest

class TestJupylint(unittest.TestCase):
    """Unit tests for the Jupylint package"""

    def test_file_markdown_cells(self):
        """Check that no code is captured out of a pure markdown file"""
        pass

    def test_file_running_code(self):
        """Check that code is correctly captured from a file containing code"""
        pass

    def test_file_old_format(self):
        """Check that old Jupyter formats are rejected"""
        pass

    def test_file_malformed(self):
        """Check that a malformed input file is correctly identified"""
        pass

    def test_stylish_code(self):
        """Check that a perfectly stylish file is not penalised"""
        pass

    def test_ugly_code(self):
        """Check that an ugly file is penalised"""
        pass

    def test_no_params(self):
        """Check that running with no parameters fails"""
        pass

    def test_params_input_file_valid(self):
        """Check that running with a valid input file works"""
        pass

    def test_params_input_file_not_found(self):
        """Check that running with an invalid input file fails"""
        pass

    def test_params_output_file(self):
        """Check that running with a valid output file works"""
        pass

    def test_keep_code_file_default(self):
        """Check that running without the keep flag deletes the file"""
        pass

    def test_keep_code_file_set(self):
        """Check that running with the keep flag doesn't delete the file"""
        pass

    def test_no_pylintrc_inclusion(self):
        """Check that not specifying a pylintrc file won't use one"""
        pass

    def test_pylintrc_inclusion(self):
        """Check that using a pylintrc file will change the output style"""
        pass

    def test_pylintrc_not_found(self):
        """Check that using a non-existent pylintrc file will fail"""
        pass

def get_jupylint_output(command):
    """Run a command to get its output, abstracting away error handling"""
    pass


if __name__ == "__main__":
    unittest.main()
    print("All tests passed")
