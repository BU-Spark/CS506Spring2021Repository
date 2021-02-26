
import PyPDF2

# convert all PDFs in a directory
import pandas as pd
import tabula
import pandera as pa
import numpy as np

from pandera import Column, DataFrameSchema, Check, Index


def import_pdf(filename):
    with open(filename, 'rb') as f:
        pdfReader = PyPDF2.PdfFileReader(f)
        print(pdfReader.numPages)
        numpages = pdfReader.numPages
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
    f.close()
    return  numpages


def convert_str(s):
    types = [int, float]
    for t in types:
        try:
            return t(s)
        except ValueError:
            pass
    return str(s).strip('\"')


def batch_transform(data_dir):
    tabula.convert_into_by_batch(data_dir, output_format='csv', pages='all')
     # data_dir = "data"

def new_row(columnlist):
    df3 = pd.DataFrame()
    df3 = df3.reindex(columnlist.columns.tolist(), axis=1)
    df3.loc[len(df3.index)] = ''
    return df3


def frame_import(filename, outfile, debug):
    reader = PyPDF2.PdfFileReader(open(filename, mode='rb'))
    m = reader.getNumPages()
    # print(reader)
    print(m)
    ratioajdf = pd.DataFrame()
    newHiredf = pd.DataFrame()

    subtotaldf = pd.DataFrame()
    totaldf = pd.DataFrame()

    df3 = pd.DataFrame()
    df4 = pd.DataFrame()
    project_hdr = ''
    contractor_hdr = ''
    trade_hdr = ''
    line_type = 0
    state = 'start'
    monthYear = str(filename)[len(filename) - 13:len(filename) - 4]
    for i in range(m):
        n = i + 1

        if n == 1:
            df2 = tabula.read_pdf(
                "./data/WorkforceUtilizationSummaryReportApril2019.pdf",pages=n, lattice=True, area=(11, 26, 582, 829), pandas_options={'header': None})

            if len(df2) > 0:
                if df2[0].iloc[0][0][0:7] == 'Project':
                    state = 'PROJECT_HDR'
                    project_hdr = df2[0].iloc[0][0]
                    df3 = df3.reindex(['MONTHYEAR','PROJECT','PROJECT_CODE'], axis=1)
                    df3.loc[len(df3.index)] = ''
                    strings = project_hdr.split(sep='\r')
                    df3['MONTHYEAR'] = monthYear
                    df3['PROJECT'] = strings[1]
                    df3['PROJECT_CODE'] = strings[3]
            if len(df2) > 1:
                state = 'CONTRACTOR_HDR'
                if df2[1].shape[0] > 0:
                    for l in range(1,df2[1].shape[0]):
                        if state == 'NEW_HIRE':
                            if df2[1].values[l][1] == 'Subtotal':
                                state = 'TRADE_SUBTOTAL'
                                df3 = pd.DataFrame()
                                df3 = df3.reindex(df4.columns.tolist(), axis=1)
                                df3.loc[len(df3.index)] = ''
                                df3.iloc[0][0] = monthYear
                                df3.iloc[0][1] = strings[1]
                                df3.iloc[0][2] = strings[3]
                                df3['CONTRACTOR'] = contractor_hdr
                                df3['CONSTRUCTION_TRADE'] = trade_hdr
                                df3.rename(columns={str(df2[0].values[1][0]).replace('\r', '_').upper(): 'TRADE_SUBTOTAL'},
                                           errors="raise", inplace=True)
                                df3['TRADE_SUBTOTAL'] = str(df2[1].values[l + 3][1]).replace('/', '_').replace(' ', '_')
                                q = 1
                                for k in range(q, len(df2[1].values[0]) - 1):
                                    df3[str(df2[0].values[2][k]).replace('\r', '_').upper()] = float(
                                        str(df2[1].values[l][k + 1]))
                                subtotaldf = subtotaldf.append(df3.copy())


                        if state == 'A_J_RATIO':
                            if str(df2[1].values[l][1]) == 'New Hire':
                                state = 'NEW_HIRE'
                                df3 = pd.DataFrame()
                                df3 = df3.reindex(df4.columns.tolist(), axis=1)
                                df3.loc[len(df3.index)] = ''
                                df3.iloc[0][0] = monthYear
                                df3.iloc[0][1] = strings[1]
                                df3.iloc[0][2] = strings[3]
                                df3['CONTRACTOR'] = contractor_hdr
                                df3['CONSTRUCTION_TRADE'] = trade_hdr
                                df3.rename(columns ={str(df2[0].values[1][0]).replace('\r', '_').upper():'NEW_HIRE'}, errors = "raise", inplace=True)
                                df3['NEW_HIRE'] = str(df2[1].values[l][1]).replace('/','_').replace(' ','_')

                                if len(df2[1].values[0]) == 12:
                                    q = 1
                                for k in range(q,len(df2[1].values[0])-1):
                                    df3[str(df2[0].values[2][k]).replace('\r', '_').upper()] = float(str(df2[1].values[l][k+1]))
                                newHiredf = newHiredf.append(df3.copy())

                        if state == 'TRADE_FTR':
                            if str(df2[1].values[l][1]) == 'A/J Ratio':
                                state = 'A_J_RATIO'
                                df3 = pd.DataFrame()
                                df3 = df3.reindex(df4.columns.tolist(), axis=1)
                                df3.loc[len(df3.index)] = ''
                                df3.iloc[0][0] = monthYear
                                df3.iloc[0][1] = strings[1]
                                df3.iloc[0][2] = strings[3]
                                df3['CONTRACTOR'] = contractor_hdr
                                df3['CONSTRUCTION_TRADE'] = trade_hdr
                                df3.rename(columns ={str(df2[0].iloc[2][0]).replace('\r', '_').upper():'SKILL_RATIO'}, errors = "raise",inplace=True)
                                df3['SKILL_RATIO'] = str(df2[1].iloc[l][1]).replace('/','_').replace(' ','_')

                                if len(df2[1].values[0]) == 12:
                                    q = 1
                                for k in range(q,len(df2[1].values[0])-1):
                                    df3[str(df2[0].values[2][k]).replace('\r', '_').upper()] = float(str(df2[1].values[l][k+1]))
                                ratioajdf = ratioajdf.append(df3.copy())

                        if state == 'TRADE_HDR':
                            state = 'TRADE_FTR'
                            df3=pd.DataFrame()
                            df3 = df3.reindex(df4.columns.tolist(), axis=1)
                            df3.loc[len(df3.index)] = ''
                            df3.iloc[0][0] = monthYear
                            df3.iloc[0][1] = strings[1]
                            df3.iloc[0][2] = strings[3]
                            df3['CONTRACTOR'] = contractor_hdr
                            df3['CONSTRUCTION_TRADE'] = str(df2[1].iloc[1][0]).replace('\r', '_').capitalize()
                            df3['CRAFT_LEVEL'] = str(df2[1].iloc[l][1]).replace('\r', '_').upper()

                            if len(df2[1].values[0]) == 12:
                                q = 1
                            for k in range(q,len(df2[1].values[0])-2):
                                df3[str(df2[0].values[2][k]).replace('\r', '_').upper()] = float(str(df2[1].iloc[l][k+1]))
                            df4=df4.append(df3.copy())

                        if state == 'TRADE_SUBTOTAL':
                            if str(df2[1].values[l][0]) == str(df2[1].values[l][0]).upper():
                                trade_hdr = str(df2[1].values[l][0]).capitalize()
                                state = 'TRADE_HDR'
                                df3 = pd.DataFrame()
                                df3 = df3.reindex(df4.columns.tolist(), axis=1)
                                df3.loc[len(df3.index)] = ''
                                df3.iloc[0][0] = monthYear
                                df3.iloc[0][1] = strings[1]
                                df3.iloc[0][2] = strings[3]
                                df3['CONTRACTOR'] = contractor_hdr
                                df3['CONSTRUCTION_TRADE'] = trade_hdr
                                df4[str(df2[1].values[1][0]).replace('\r', '_').upper()] = str(df2[1].values[l][1]).replace('Journey', 'Journeyman')
                                if len(df2[1].values[0]) == 12:
                                    q = 1
                                for k in range(q,len(df2[1].values[0])-2):
                                    df3[str(df2[0].values[1][k]).replace('\r', '_').upper()] = float(str(df2[1].values[l][k+1]))
                                df4=df4.append(df3.copy())

                        if state == 'CONTRACTOR_HDR':
                            if l == 1:
                                contractor_hdr = df2[1].iloc[0][0]
                            else:
                                contractor_hdr = df2[1].iloc[l][0]
                            df3['CONTRACTOR'] = contractor_hdr
                            # df4.loc[len(df4.columns.tolist())] = contractor_hdr
                            # df['CONTRACTOR_HDR'] = df['CONTRACTOR_HDR'].replace(['old value'], 'new value')
                            if str(df2[1].values[l][0]) == str(df2[1].values[l][0]).upper():
                                trade_level_hdr = str(df2[0].values[2][0]).replace('\r','_').upper()
                                trade = str(df2[1].values[l][0]).replace('\r', '_').upper()
                                df3['CONSTRUCTION_TRADE'] = trade
                                state = 'TRADE_HDR'
                                q = 0
                                df3[trade_level_hdr] = str(df2[1].values[l][1]).replace('Journey', 'Journeyman')

                                if len(df2[1].values[l]) == 12:
                                    q = 1
                                for k in range(q, len(df2[1].values[l]) - 2):
                                    df3[str(df2[0].iloc[2][k]).replace('\r', '_').upper()] = float(str(df2[1].iloc[l][k + 1]))
                                df4=df4.append(df3.copy())

            if debug:
                print(df4)
        #         "./data/WorkforceUtilizationSummaryReportApril2019.pdf")
    df4.to_csv(outfile, index=False)


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


def main():
    pass


if __name__ == "__main__":
    main()


# schema = DataFrameSchema(
#     {
#         "column1": Column(pa.Int),
#         "column2": Column(pa.Float, Check(lambda s: s < -1.2)),
#         # you can provide a list of validators
#         "column3": Column(pa.String, [
#            Check(lambda s: s.str.startswith("value")),
#            Check(lambda s: s.str.split("_", expand=True).shape[1] == 2)
#         ]),
#     },
#     index=Index(pa.Int),
#     strict=True,
#     coerce=True,
# )
#
#
#
# df = pd.DataFrame({"column1": [5, 1, np.nan]})
#
# non_null_schema = DataFrameSchema({
#     "column1": Column(pa.Int, Check(lambda x: x > 0))
# })
#
# non_null_schema.validate(df)