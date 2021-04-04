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
    csv_file = "data2/WorkforceUtilizationSummaryReport"
    pdf_file = "data/WorkforceUtilizationSummaryReportJan2019.pdf"
    #  The above pdf file has an apprentice section shifted to the right one cell for Ceiling
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportFeb2019.pdf"
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportMar2019.pdf"
    #  The above pdf file has a field with over 1000 hours for Manafort-Precision, LLC
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportApr2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportMay2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportJun2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportJul2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportAug2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportSep2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportOct2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportNov2019.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data/WorkforceUtilizationSummaryReportDec2019.pdf"
       #  Next Month
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