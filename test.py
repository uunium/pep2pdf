# test.py - simple test for pep2pdf.py: imports range of PEPs
#
# Copyright 2015 Andriy Korchak <AndriyKorchak at gmail dot com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

"""
A simple test for pep2pdf.py. Downloads all PEPs with
numbers between min_number and max_number, and converts it to pdf.
Output files are stored in the given directory.

Usage:
    python test.py min_number max_number output_directory

"""

import sys
from pep2pdf import pep2pdf as pep2pdf
import os


def import_peps(min_number, max_number, output_directory):
    num = 0
    for i in range(min_number, max_number + 1):
        filename = "pep-" + ("0000" + str(i))[-4:] + ".pdf"
        print("Importing " + filename + "...")
        file_path = os.path.join(output_directory, filename)
        result = pep2pdf(i, file_path)
        if result:
            num += 1
    message = "Succesfully imported {0} files".format(num)
    print(message)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Not enough arguments")
        print(__doc__)
    else:
        min_number = int(sys.argv[1])
        max_number = int(sys.argv[2])
        output_directory = sys.argv[3]
        import_peps(min_number, max_number, output_directory)
