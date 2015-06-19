# pep2pdf.py - script for downloading the latest PEPs and converting it to PDF
#
# Copyright 2015 Andriy Korchak <AndriyKorchak at gmail dot com>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.

"""
pep2pdf.py - module for downloading the latest PEPs and converting it to PDF

Usage:
    python pep2pdf.py PEP_number [pdf_file]

Contains:
    pep2pdf(PEP_number, pdf_file="") - main function. Dowloads the PEP with
        number PEP_number and converts it to PDF file named pdf_file
"""

import sys

def pep2pdf(PEP_number, pdf_file=""):
    """
    Downloads the PEP with given number from official Mercurial
    repository and converts it to PDF

    :param PEP_number: (str, int) - number of PEP. For instance: "8",
    :param pdf_file: (str) - name of generated file. If not specified,
        will be formed like "PEP0257.pdf".
    :return: None
    """

def _get_source_filename(PEP_number):


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Not enough arguments"
        print __doc__
