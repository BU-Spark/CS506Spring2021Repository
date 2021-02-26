import unittest
from sys import argv

from src.parsers.pdf_parser import import_pdf, batch_transform
from src.parsers.tabula_parser import convert_reader
from src.parsers.threetierledger import threetier_convert


def main(arg):
    debug = False
    print("================================")
    pdf_file = "data/WorkforceUtilizationSummaryReportApril2019.pdf"
    csv_file = "data2/WorkforceUtilizationSummaryReportApril2019.csv"
    convert_reader(pdf_file,csv_file)

    # threetier_convert(csv_file,'data2')
    # uncomment the row below to create csv files in one batch
    # batch_transform("data")

    # rows = import_pdf("data/WorkforceUtilizationSummaryReportApril2019.pdf", debug)
    # print(rows)
    print("================================")


if __name__ == "__main__":
    main(argv)
    unittest.main(argv)

