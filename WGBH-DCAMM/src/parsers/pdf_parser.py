
import PyPDF2

# convert all PDFs in a directory
import tabula

def convert_str(s):
    types = [int, float]
    for t in types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip('\"')

def batch_transform(data_dir, debug):
    tabula.convert_into_by_batch(data_dir, output_format='csv', pages='all')
     # data_dir = "data"


def frame_import(filename, debug):
    df2 = tabula.read_pdf(
        "./data/WorkforceUtilizationSummaryReportApril2019.pdf")
    if debug:
        print(df2)
        #         "./data/WorkforceUtilizationSummaryReportApril2019.pdf")


def import_pypdf2(filename, debug):
    with open(filename, 'r') as f:
        pdfReader = PyPDF2.PdfFileReader(f)
        print(pdfReader.numPages)
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
        f.close()


def read_csv(csv_file_path, debug):
        """
            Given a path to a csv file, return a matrix (list of lists)
            in row major.
        """
        res = []
        with open("data/WorkforceUtilizationSummaryReportDec2019.csv", 'r') as csv_file:
            lines = csv_file.readlines()
            for line in lines:
                row = []
                values = line.strip('\n').split(',')
                for val in values:
                    row.append(convert_str(val))
                res.append(row)
            print(res)
        return res