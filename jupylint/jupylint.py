#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple tool to extract python code from a Jupyter notebook, and then run
pylint on it for static analysis."""

from argparse import ArgumentParser
from os import system, remove
from json import load

class Jupylint:
    """The tool to extract from Jupyter notebooks and run pylint"""
    CELL_SEPARATOR = "# " + ("=" * 78) + "\n"
    DEFAULT_IN_FILE = "Q1.ipynb"
    DEFAULT_OUT_FILE = "out.py"

    @staticmethod
    def extract_content(content, out_file_name="out.py"):
        """Extract the code blocks from the json and write it out to a file"""
        with open(out_file_name, "w+", encoding='utf-8') as out_file:
            for cell in content:
                if cell["cell_type"] == "code":
                    out_file.write(Jupylint.CELL_SEPARATOR)
                    for line in cell["source"]:
                        out_file.write(line)
                    out_file.write("\n\n")

    @staticmethod
    def get_json_contents(in_file_name):
        """Extract the json contents from the Jupyter file"""
        content = ""
        with open(in_file_name, "r", encoding='utf-8') as in_file:
            content = load(in_file)

        if content["nbformat"] >= 4:
            return content["cells"]
        return content["worksheets"][0]["cells"]

    @staticmethod
    def run():
        """Run the tool, running pylint on the code within a specified Jupyter
        notebook"""

        # Parse keyword arguments
        parser = ArgumentParser(description="""A simple tool to extract
        python code from a Jupyter notebook, and then run pylint on it for static
        analysis.""")

        parser.add_argument('in_file_name', metavar='input file name', type=str,
            nargs='?', default=Jupylint.DEFAULT_IN_FILE,
            help='the name of the Jupyter notebook file to extract the code from')
        parser.add_argument('out_file_name', metavar='output file name', type=str,
            nargs='?', default=Jupylint.DEFAULT_OUT_FILE,
            help='the name of the output file to write the extracted code to')
        parser.add_argument('-k', '--keep', dest='save_file', action='store_false',
            help='a boolean specifying whether to keep the extracted python file')
        args = parser.parse_args()
        print(args)

        # Call the extract and write out the code contents
        json_contents = Jupylint.get_json_contents(args.in_file_name)
        Jupylint.extract_content(json_contents)

        # Run pylint
        system(f"pylint {args.out_file_name}")

        # Clean up
        if not args.save_file:
            remove(args.out_file_name)


if __name__ == "__main__":
    Jupylint.run()
