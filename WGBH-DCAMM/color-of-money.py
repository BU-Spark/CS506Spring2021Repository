import unittest
from sys import argv
from  src.parsers import pd_parser
import os

from src.parsers.pdf_parser import import_pdf, batch_transform, frame_import
from src.parsers.tabula_parser import convert_reader
from src.parsers.threetierledger import threetier_convert



def main(arg):
    debug = False
    os.system("pwd")
    print("================================")
    pdf_file = "data/WorkforceUtilizationSummaryReportJan2019.pdf"
    csv_file = "data2/WorkforceUtilizationSummaryReportJan2019"
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportFeb2019.pdf"
    csv_file = "data2/WorkforceUtilizationSummaryReportFeb2019"
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportMar2019.pdf"
    csv_file = "data2/WorkforceUtilizationSummaryReportMar2019"
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    print("================================")


if __name__ == "__main__":
    main(argv)
    unittest.main(argv)

# OLD USEFUL COMMANDS
    # pd_parser.main(pdf_file, csv_file, True)

    # uncomment the row below to create csv files in one batch
    # batch_transform("data")

    # rows = import_pdf("data/WorkforceUtilizationSummaryReportApril2019.pdf", debug)
    # print(rows)