import unittest
from sys import argv
from src.parsers.pdf_parser import  read_csv


def main(arg):
    debug = False
    print("================================")
    rows = read_csv("data/WorkforceUtilizationSummaryReportApril2019.pdf", debug)

    print("================================")

if __name__ == "__main__":
    main(argv)
    unittest.main(argv)

