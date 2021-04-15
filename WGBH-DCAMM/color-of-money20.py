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
    csv_file = "data2020/WorkforceUtilizationSummaryReport"
    pdf_file = "data20/WorkforceUtilizationSummaryReportJan2020.pdf"
    #  The above pdf file has an apprentice section shifted to the right one cell for Ceiling
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportFeb2020.pdf"
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportMar2020.pdf"
    #  The above pdf file has a field with over 1000 hours for Manafort-Precision, LLC
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportApr2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportMay2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportJun2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportJul2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportAug2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportSep2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportOct2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportNov2020.pdf"
       #  Next Month
    os.system(f'python3 src/parsers/pd_parser.py {pdf_file} {csv_file} {debug} | tee -a proof.txt')
    pdf_file = "data20/WorkforceUtilizationSummaryReportDec2020.pdf"
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

    # rows = import_pdf("data2020/WorkforceUtilizationSummaryReportApril2020.pdf", debug)
    # print(rows)