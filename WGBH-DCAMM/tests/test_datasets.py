import csv

import PyPDF2
import pytest
import pandas as pd

from src.parsers.pdf_parser import import_pdf


def read_id(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []
    with open(csv_file_path, 'r') as csv_file:
        lines = csv.reader(csv_file, delimiter=',', quotechar='"', skipinitialspace=True)
        next(csv_file)
        for line in lines:
            row = []
            idx = 0
            for val in line:
                if idx == 0:
                    data_temp = val
                    row.append(data_temp)
                idx += 1
            res.append(row)
    return res


@pytest.mark.parametrize('dataset,expected_length', [
    (
        "data/WorkforceUtilizationSummaryReportApril2019.pdf",
        82
    ),
])

def test_read_tr_length(dataset, expected_length):
    reader = PyPDF2.PdfFileReader(open(dataset, mode='rb'))

    actual_data = import_pdf(dataset)
    expected_data = expected_length
    assert actual_data == expected_data

    def run(self, params={}):
        try:
            if params.get('contents'):
                pdfFile = base64.b64decode(params.get('contents'))
            else:
                raise Exception("File contents missing!")
        except Exception as e:
            self.logger.error("File contents missing: ", e)
            raise
        try:
            with open("temp.pdf", 'wb') as temp_pdf:
                temp_pdf.write(pdfFile)
                pdfReader = PyPDF2.PdfFileReader(open('temp.pdf', 'rb'))
                pdftext = ""
                for page in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(page)
                    pdftext += pageObj.extractText().replace('\n', '')
        except Exception as e:
            self.logger.info("An error occurred while extracting text: ", e)
            raise
        return {"output": pdftext}