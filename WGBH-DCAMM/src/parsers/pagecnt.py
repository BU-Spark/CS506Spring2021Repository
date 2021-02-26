import PyPDF2


def main():
    pdf_file =[ "data/WorkforceUtilizationSummaryReportJan2019.pdf",
               "data/WorkforceUtilizationSummaryReportFeb2019.pdf",
               "data/WorkforceUtilizationSummaryReportMar2019.pdf",
               "data/WorkforceUtilizationSummaryReportApr2019.pdf",
               "data/WorkforceUtilizationSummaryReportMay2019.pdf",
               "data/WorkforceUtilizationSummaryReportJun2019.pdf",
               "data/WorkforceUtilizationSummaryReportJul2019.pdf",
               "data/WorkforceUtilizationSummaryReportAug2019.pdf",
               "data/WorkforceUtilizationSummaryReportSep2019.pdf",
               "data/WorkforceUtilizationSummaryReportOct2019.pdf",
               "data/WorkforceUtilizationSummaryReportNov2019.pdf",
               "data/WorkforceUtilizationSummaryReportDec2019.pdf" ]

    print()
    z = 0
    for file in pdf_file:
        reader = PyPDF2.PdfFileReader(open(file, mode='rb'))
        m = reader.getNumPages()
        print(f'                        {file[len(file)-11:len(file)-4]} pages {m}')
        z = z + m
    print(f' Total pages processed by the parser: {z}')


if __name__ == "__main__":
    main()

