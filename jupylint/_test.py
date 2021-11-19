#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The testing framework for the Jupylint package
"""

from subprocess import check_output, CalledProcessError, STDOUT
from os import path, remove
import unittest

from .jupylint import Jupylint


class TestJupylint(unittest.TestCase):
    """Unit tests for the Jupylint package"""

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
        args = {
            "in_file_name": ["./jupylint/test_files/running_code_old.ipynb"],
            "out_file_name": "./.jupylint_tmp_out.py",
            "save_file": False
        }
        results = Jupylint.execute(args)
        self.assertTrue("too old (<=4.0)" in results)

    def test_file_malformed(self):
        """Check that a malformed input file is correctly identified"""
        args = {
            "in_file_name": ["./jupylint/test_files/malformed.ipynb"],
            "out_file_name": "./.jupylint_tmp_out.py",
            "save_file": False
        }
        results = Jupylint.execute(args)
        self.assertEqual("Malformed input file", results)

    def test_stylish_code(self):
        """Check that a perfectly stylish file is not penalised"""
        args = {
            "in_file_name": ["./jupylint/test_files/stylish.ipynb"],
            "out_file_name": "./.jupylint_tmp_out.py",
            "save_file": False
        }
        results = Jupylint.execute(args)
        self.assertTrue("Your code has been rated at 10.00/10" in results)

    def test_ugly_code(self):
        """Check that an ugly file is penalised"""
        args = {
            "in_file_name": ["./jupylint/test_files/running_code.ipynb"],
            "out_file_name": "./.jupylint_tmp_out.py",
            "save_file": False
        }
        results = Jupylint.execute(args)
        self.assertTrue("Your code has been rated at" in results)
        self.assertFalse("Your code has been rated at 10.00/10" in results)

    def test_no_params(self):
        """Check that running with no parameters fails"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py".split(" ")
        )
        self.assertTrue("error" in result)

    def test_params_input_file_valid(self):
        """Check that running with a valid input file works"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb".split(" ")
        )
        self.assertTrue("Your code has been rated" in result)

    def test_params_input_file_not_found(self):
        """Check that running with an invalid input file fails"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/non_existent_file.ipynb".split(" ")
        )
        self.assertEqual("Input file cannot be found\n", result)

    def test_params_output_file(self):
        """Check that running with a valid output file works, and changes the
        output file location"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb ./jupylint_test_out.py --keep".split(" ")
        )
        self.assertTrue(path.isfile("./jupylint_test_out.py"))
        self.assertTrue("Your code has been rated" in result)

    def test_keep_code_file_default(self):
        """Check that running without the keep flag deletes the file"""
        _ = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb ./.jupylint_tmp_out.py".split(" ")
        )
        self.assertFalse(path.isfile("./.jupylint_tmp_out.py"))

    def test_keep_code_file_set(self):
        """Check that running with the keep flag doesn't delete the file"""
        _ = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb ./.jupylint_tmp_out.py --keep".split(" ")
        )
        self.assertTrue(path.isfile("./.jupylint_tmp_out.py"))

    def test_no_pylintrc_inclusion(self):
        """Check that not specifying a pylintrc file won't use one"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb".split(" ")
        )
        self.assertTrue("Report\n======" not in result)

    def test_pylintrc_inclusion(self):
        """Check that using a pylintrc file will change the output style"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb --rcfile ./jupylint/test_files/hidden_pylintrc".split(" ")
        )
        self.assertTrue("Report\n======" in result)

    def test_pylintrc_not_found(self):
        """Check that using a non-existent pylintrc file will fail"""
        result = get_jupylint_output(
            "python3 ./jupylint_runner.py ./jupylint/test_files/stylish.ipynb --rcfile ./jupylint/test_files/no_pylintrc".split(" ")
        )
        self.assertEqual("The config file ./jupylint/test_files/no_pylintrc doesn't exist!\n\n", result)

    @classmethod
    def tearDownClass(cls):
        """Clean up, removing any output files left around"""
        if path.isfile("./.jupylint_tmp_out.py"):
            remove("./.jupylint_tmp_out.py")
        if path.isfile("./jupylint_test_out.py"):
            remove("./jupylint_test_out.py")


def get_jupylint_output(command):
    """Run a command to get its output, abstracting away error handling"""
    try:
        return check_output(command, stderr=STDOUT).decode("unicode_escape")
    except CalledProcessError as err:
        return err.output.decode("unicode_escape")
