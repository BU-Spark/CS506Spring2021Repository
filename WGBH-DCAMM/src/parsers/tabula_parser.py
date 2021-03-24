import pandas as pd
import numpy as np
from tabula import read_pdf
import PyPDF2


def convert_reader(pdf_file, outdatadir):
    reader = PyPDF2.PdfFileReader(open(pdf_file, mode='rb'))
    m = reader.getNumPages()
    #print(reader)
    print(m)
    for i in range(m):
        n = i+1
    
        if n==1:
            df = read_pdf(pdf_file, encoding='UTF-8', pages=n)
            # df = read_pdf(pdf_file, pandas_options={'header': None, 'error_bad_lines': False}, pages=n)
            index = np.where(df[0].isnull())[0]
            sect = df.iloc[index[0]:index[-1]]
            s = []
            headers = []
            for col in sect:
                colnames = sect[col].dropna().values.flatten()
                (s.insert(len(s), colnames))
                pic = [' '.join(s[col])]
                for i in pic:
                    headers.append(i)
            print(df)
            df.drop(sect, inplace=True)
            df.columns = headers
            new_df = pd.DataFrame(columns=headers)
            new_df = pd.concat([new_df, df], axis=0, ignore_index=True)
    
        else:
            df_2 = read_pdf(pdf_file, pandas_options={'header': None, 'error_bad_lines': False, 'encoding': "ISO-8859-1"}, pages=n)
            df_2.drop(sect, inplace=True)
            df_2.columns = headers
            new_df = pd.concat([new_df, df_2], axis=0, ignore_index=True)
    
    new_df.columns = headers
    print(new_df)
    new_df.to_csv(outdatadir, index=False)

def main():
    debug = False
    print("================================")
    pdf_file = 'data/WorkforceUtilizationSummaryReportApril2019.pdf'
    convert_reader(pdf_file, 'data2/out.csv')

if __name__ == "__main__":
    main()
