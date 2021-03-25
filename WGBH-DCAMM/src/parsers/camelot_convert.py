import camelot

pdf_file = "data/WorkforceUtilizationSummaryReportApril2019.pdf"
csv_file = "data2/WorkforceUtilizationSummaryReportApril2019.csv"
tables = camelot.read_pdf(pdf_file)
tables
tables.export(csv_file, f='csv', compress=True) # json, excel, html
tables[0]
tables[0].parsing_report
tables[0].to_csv(csv_file) # to_json, to_excel, to_html
tables[0].df # get a pandas DataFrame!