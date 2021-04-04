import PyPDF2
# convert all PDFs in a directory
import pandas as pd
import tabula
from sys import argv

import numpy as np


def up_underscore(string):
    # leaving these examples here though they only clean up pd.DataFrames not python str
    # clean_df = df[0].replace('\r', ' ', regex=True)
    # clean_df[0].map('{:,d}'.=format)
    # df2['PROJECT'] = df2['PROJECT'].str.replace(',', '').str.replace('$', '').astype(int)
    return str(string).replace('\n','').replace('\r', '_').replace(' ', '_').upper()


def get_project(prj_str):
    strings = prj_str.split(sep='\r')
    return strings[1], strings[3]

def get_month(monthyr):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(monthyr[len(monthyr)-7:len(monthyr)-4])

def first_hdrs(df_num):
    d= df_num[0][0].split('\r')
    string = 'MONTH YEAR ' + up_underscore(d[0][0:7]) +' '+ up_underscore(d[2][0:12]) +' '+ \
             'CONTRACTOR' +' '+ up_underscore(df_num[0][1]) +' '+ up_underscore(df_num[0][2])
    for k in range(1, df_num.shape[1]):
        string += ' '+ up_underscore(df_num[k][2])
    string += ' '+ up_underscore(df_num[1][1]) + '_PER_MONTH'
    return string.split()

def make_it_happen(df_num, row_num, offset, STOREIT, NEWHIRE, COL, MONTH, MONTHYR, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE, CRAFT_LVL):
    temp_df = pd.DataFrame()
    temp_df = temp_df.reindex(COL, axis=1)
    temp_df.loc[len(temp_df.index)] = ''
    temp_df['MONTH'] = MONTH
    temp_df['YEAR'] = MONTHYR[3:7]
    temp_df['PROJECT'] = PROJCT
    temp_df['PROJECT_CODE'] = PROJCT_CD
    temp_df['CONTRACTOR'] = CONTRACTOR
    temp_df['CONSTRUCTION_TRADE'] = CONSTR_TRADE
    temp_df['CRAFT_LEVEL'] = CRAFT_LVL
    for k in range(2, len(df_num.values[1])):
        temp_df[[COL][0][k + 5]] = float(str(df_num.values[row_num][k-offset]).replace(',', ''))
    temp_df[[COL][0][len(COL) - 1]] = [COL][0][len(COL) - 1][0:5] + [COL][0][len(COL) - 1][
                                                                    12:len([COL][0][len(COL) - 1])]
    if CRAFT_LVL == 'New_Hire':
        NEWHIRE = NEWHIRE.append(temp_df.copy())
    else:
        STOREIT = STOREIT.append(temp_df.copy())

    return STOREIT, NEWHIRE, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE


def process_grp(remaining,df_num, row_num, grp_name, STOREIT, NEWHIRE, COL, MONTH, MONTHYR, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE):
    # if remaining > 0 : raise("err")
    CRAFT_LVL=''
    if grp_name == 'grand_total':
        remaining = 4
        seq = ['pj', 'pa', 'pnh', 'pgrand']
    elif grp_name == 'contractor' or grp_name == 'project':
        remaining = 1
        seq = ['cj']
    else:
        remaining = 5
        seq = ['j', 'a', 'aj', 'nh', 'sub']
    rows = 0
    if grp_name == 'project':
        PROJCT,PROJCT_CD = get_project (df_num.values[row_num][0])
        print(f' complete grp {seq[rows]}  {PROJCT}  {remaining} ')
        remaining -= 1; rows = 3
    elif grp_name =='trade':
        print(f' {grp_name} {remaining}')
        while remaining > 0 and len(df_num)-row_num-rows > 0:
            offset = 0
            if rows == 0:
                CONSTR_TRADE = str(df_num.values[row_num][0]).replace('\r',' ').replace('\n',' ')
                CRAFT_LVL = str(df_num.values[row_num][1]).replace('Journey','Journeymen')
            if rows == 1:
                if df_num.values[row_num+rows][1]=='0.00':
                    offset =1
                CRAFT_LVL = df_num.values[row_num+rows][1-offset]
            if rows == 3:
                if df_num.values[row_num+rows][1]=='0.00':
                    offset =1
                CRAFT_LVL = str(df_num.values[row_num+rows][1-offset]).replace(' ','_')
            if rows == 0 or rows == 1 or rows == 3:
                STOREIT, NEWHIRE, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE = \
                    make_it_happen(df_num, row_num+rows, offset, STOREIT, NEWHIRE, COL, MONTH, MONTHYR,
                   PROJCT,  PROJCT_CD, CONTRACTOR, CONSTR_TRADE, CRAFT_LVL)
            print(f' process grp {seq[rows]}')
            remaining -= 1; rows += 1
    elif grp_name == 'contractor':
        CONTRACTOR = str(df_num[0][row_num]).replace('\n','').capitalize()
        print(f' complete grp {seq[rows]}  {CONTRACTOR}  {remaining} ')
        remaining -= 1; rows += 1
    elif grp_name == 'contr_total':
        print(f' {grp_name} {remaining}')
        while remaining > 0 and len(df_num)-row_num-rows > 0:
            print(f' process grp {seq[rows]}')
            remaining -= 1; rows += 1
    elif grp_name == 'grand_total':
        print(f' {grp_name} {remaining}')
        while remaining > 0 and len(df_num)-row_num-rows > 0:
            print(f' process grp {seq[rows]}')
            remaining -= 1; rows += 1
    else:
        print('DO NOT GO HERE!')
    print(f' complete grp {grp_name}')
    print()
    return rows, remaining, STOREIT, NEWHIRE, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE


def identify_grp(df_num, row_num):

    if len(df_num) == 3 and df_num.values[row_num][0][0:7]=='Project':
        group = 'project'
    elif str(df_num.values[row_num][0]) == 'Total for Contractor' and not pd.isna(df_num.values[row_num][2]):
        group = 'contr_total'
    elif str(df_num.values[row_num][0]) == 'Total  Journey Hours' and not pd.isna(df_num.values[row_num][2]):
        group = 'grand_total'
    elif type(df_num.values[row_num][0]) == str and pd.isna(df_num.values[row_num][2]) and df_num.values[row_num][6] != df_num.values[row_num][6]  :
        group = 'contractor'
    elif str(df_num.values[row_num][0][0:10]) == str(df_num.values[row_num][0][0:10]).upper() and\
            str(df_num.values[row_num][1]) == 'Journey' and \
            not pd.isna(df_num.values[row_num][2]):
        group = 'trade'
    else:
        group = 'none'

    return group


def start_process(df_num):
    COL = first_hdrs(df_num)
    PROJCT,PROJCT_CD = get_project(df_num[0][0])
    print(COL)
    return 3, COL,PROJCT,PROJCT_CD


def main(argv):
    PROJCT = ''
    PROJCT_CD = ''
    CONTRACTOR= ''
    CONSTR_TRADE = ''
    script, filename, outfile, debug = argv
    reader = PyPDF2.PdfFileReader(open(filename, mode='rb'))
    m = reader.getNumPages()
    proc_pages = 1
    beginning = True
    remaining = 0
    grp=''

    # Create the dictionary to capture the rows.
    STOREIT = pd.DataFrame()
    NEWHIRE = pd.DataFrame()
    # Later I will add back this class to speed up the process
    # line = Detail('', '', '', '', '', '', ['', '', '', '', '', '', '', '', '', ''])
    MONTHYR = str(filename)[len(filename) - 11:len(filename) - 4]
    MONTH = str(np.char.zfill(str(get_month(MONTHYR)+1), 2))

    # To test for a smaller number of pages set m to a small number
    while proc_pages <= m:
        print(f'starting page {proc_pages}')
        df0 = tabula.read_pdf(filename, pages=proc_pages, lattice=True, area=(11, 26, 582, 829),
                              pandas_options={'header': None})
        rows = 0
        proc_dfs = 0
        while proc_dfs < len(df0):
            print(f' Processing DF number: {proc_dfs}')
            print(df0[proc_dfs])
            print()
            proc_rows = 0
            while proc_rows < len(df0[proc_dfs]):
                print(f' Processing row number: {proc_rows}')
                if remaining:
                    rows, remaining,STOREIT, NEWHIRE, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE = \
                        process_grp(remaining, df0[proc_dfs],proc_rows,grp, STOREIT, NEWHIRE, COL, MONTH, MONTHYR, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE)
                    # complete_grp(remaining,df0[proc_dfs], proc_rows, grp, line)
                elif beginning:
                    rows,COL,PROJCT,PROJCT_CD= start_process(df0[proc_dfs])
                    beginning = False
                else:
                    grp = identify_grp(df0[proc_dfs],proc_rows)
                    rows, remaining,STOREIT, NEWHIRE, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE = \
                        process_grp(remaining, df0[proc_dfs],proc_rows,grp, STOREIT, NEWHIRE, COL, MONTH, MONTHYR, PROJCT, PROJCT_CD, CONTRACTOR, CONSTR_TRADE)
                proc_rows += rows
            proc_dfs += 1
        proc_pages += 1
        if debug:
            print(STOREIT)
    #         "./data/WorkforceUtilizationSummaryReportApril2019.pdf")
    outfile =  outfile + MONTHYR[3:7] + MONTH + '.csv'
    STOREIT.to_csv(outfile, index=False)
    outfile2 =  outfile + 'NH'+ MONTHYR[3:7] + MONTH + '.csv'
    NEWHIRE.to_csv(outfile2, index=False)


if __name__ == "__main__":
    main(argv)

# use the command below to run the parser:
# python3 src/parsers/pd_parser.py data/WorkforceUtilizationSummaryReportJan2019.pdf data2/WorkforceUtilizationSummaryReportJan20192 true | tee -a  proof.txt

