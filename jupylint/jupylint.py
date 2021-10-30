#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple tool to extract python code from a Jupyter notebook, and then run
pylint on it for static analysis."""

from argparse import ArgumentParser
from subprocess import check_output, CalledProcessError
from json import load, decoder
from os import remove, path


class OldJupyterVersionError(Exception):
    """A custom exception for when the Jupyter version is too old"""


class Jupylint:
    """The tool to extract from Jupyter notebooks and run pylint"""
    CELL_SEPARATOR = "# " + ("=" * 78) + "\n"
    DEFAULT_OUT_FILE = "out.py"

    @staticmethod
    def get_arguments():
        """Parse keyword arguments for the tool"""
        parser = ArgumentParser(description="""A simple tool to extract
        python code from a Jupyter notebook, and then run pylint on it for static
        analysis.""")
        parser.add_argument("in_file_name", metavar="input_file_name", type=str,
            nargs=1, help="the name of the Jupyter notebook file to extract the code from")
        parser.add_argument("out_file_name", metavar="output_file_name", type=str,
            nargs="?", default=Jupylint.DEFAULT_OUT_FILE,
            help="the name of the output file to write the extracted code to")
        parser.add_argument("-k", "--keep", dest="save_file", action="store_true",
            help="a boolean specifying whether to keep or delete the extracted python file")
        return parser.parse_args()

    @staticmethod
    def get_json_content(in_file_name):
        """Extract the json contents from the Jupyter file"""
        json_content = ""
        with open(in_file_name, "r", encoding="utf-8") as in_file:
            json_content = load(in_file)
        if json_content["nbformat"] >= 4:
            return json_content["cells"]
        raise OldJupyterVersionError(f"The Jupyter version of '{in_file_name}' is too old (<=4.0)")

    @staticmethod
    def get_code_content(json_content):
        """Extract the code blocks from the json"""
        code_content = ""
        for cell in json_content:
            if cell["cell_type"] == "code":
                code_content += Jupylint.CELL_SEPARATOR
                for line in cell["source"]:
                    code_content += line
                code_content += "\n\n"
        # Drop the trailing new line
        return code_content[:-1]

    @staticmethod
    def execute(args):
        """Call the chain of functions composing the tool given a set of
        arguments, and return the output"""
        # Run the internal functions, catching errors on invalid JSON files
        try:
            file_json_content = Jupylint.get_json_content(args["in_file_name"][0])
        except FileNotFoundError:
            return "Input file cannot be found"
        except decoder.JSONDecodeError:
            return "Malformed input file"
        except OldJupyterVersionError as err:
            return str(err)

        file_code_content = Jupylint.get_code_content(file_json_content)
        with open(args["out_file_name"], "w+", encoding="utf-8") as out_file:
            out_file.write(file_code_content)
        # Use subprocess to run pylint. Catch error codes, as pylint sometimes
        # exits with a non-zero value resulting in a runtime error on
        # check_output and decode the message to a string, as the return type is
        # a binary string
        try:
            return check_output(["pylint", args["out_file_name"]]).decode("unicode_escape")
        except CalledProcessError as err:
            return err.output.decode("unicode_escape")

    @staticmethod
    def run():
        """Provide a simple function call to take user input through arguments
        and print the results to standard output"""
        # Get the arguments for the tool
        args = vars(Jupylint.get_arguments())

        # Run the tool and display its output
        print(Jupylint.execute(args))
        # Clean up if required
        if not args["save_file"] and path.isfile(args["out_file_name"]):
            remove(args["out_file_name"])


def main():
    """External run hook"""
    Jupylint.run()
