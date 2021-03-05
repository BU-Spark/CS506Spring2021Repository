import tabula
pdf_path = "/Users/richardlee/Downloads/WorkforceUtilizationSummaryReportApril2019.pdf"

dfs = tabula.read_pdf(pdf_path, pages = 1)
tabula.convert_into(pdf_path, "out_put.csv", output_format= "csv", pages='all')

