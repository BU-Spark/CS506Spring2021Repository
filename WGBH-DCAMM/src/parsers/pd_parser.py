import PyPDF2
# convert all PDFs in a directory
import pandas as pd
import tabula
from sys import argv

import numpy as np


MONTH = ''
MONTHYR = ''
PROJCT = ''
PROJCT_CD = ''
CONTRACTOR = ''
TRAD = ''
LEVL = ''
COL=''

class Detail(object):
    def __init__(self,  monthYear, project, projectCode, contractor, trade, level, columndata):
        self.monthyr = monthYear
        self.prj = project
        self.prjcd = projectCode
        self.contr = contractor
        self.trd = trade
        self.lvl = level
        self.columns = columndata
        self.rows = []
        self.ajr = []
        self.newh = []
        self.sub = []
        self.tot = []
        self.gtot = []

    def set_dict(self, dict2):
        # dict2['TOTAL_EMPLOYEE'] = columndata[0]
        # dict2['CAUCASIAN'] = columndata[1]
        # dict2['AFRICAN_AMERICAN']= columndata[2]
        # dict2['HISPANIC'] = columndata[3]
        # dict2['ASIAN'] = columndata[4]
        # dict2['NATIVE_AMERICAN']= columndata[5]
        # dict2['OTHER'] = columndata[6]
        # dict2['NOT_SPECIFIED'] = columndata[7]
        # dict2['TOTAL_FEMALE'] = columndata[8]
        # dict2['TOTAL_MALE'] = columndata[9]
        dict = {}
        dict['MONTHYEAR']=self.monthyr
        dict['PROJECT']= self.prj
        dict['PROJECT_CODE'] = self.prjcd
        dict['CONTRACTOR'] = self.contr
        dict['CONSTRUCTION_TRADE'] = self.trd
        dict['CRAFT_LEVEL'] = self.lvl
        dict.update(dict2)
        if self.lvl == 'New hire':
            self.newh.append(dict)
        elif self.lvl == 'A/j ratio':
            self.ajr.append(dict)
        elif self.lvl == 'Subtotal':
            self.sub.append(dict)
        elif self.lvl == 'Total for Contractor':
            self.contr.append(dict)
        elif self.lvl == 'Total':
            self.prj.append(dict)
        else:
            self.rows.append(dict)


    def get_rows(self):
        return self.rows


    def get_ajr(self):
        return self.ajr


    def get_newh(self):
        return self.newh


    def get_sub(self):
        return self.sub


    def get_tot(self):
        return self.tot


    def get_gtot(self):
        return self.gtot


    def set_monthyr(self,monthYear):
        self.monthyr = monthYear


    def get_monthyr(self):
        return self.monthyr


    def set_prj(self,project, projectCode):
        self.prj = project
        self.prjcd = projectCode


    def set_contr(self, contractor):
        self.contr = contractor


    def set_contr(self):
        return self.contr


    def set_trd(self, trade):
        self.trd = trade


    def set_lvl(self, lvl):
        self.lvl = lvl


    def print_rows(self):
        print(self.rows)



    def print_arj(self):
        print(self.ajr)


    def print_newh(self):
        print(self.newh)


    def print_sub(self):
        print(self.sub)


    def print_tot(self):
        print(self.tot)


    def print_gtot(self):
        print(self.gtot)


class A_J_ratio(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)


class New_hire(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)


class Subtotal(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)


class Total(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)


class Grand_Total(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)


class Report_Total(Detail):
    def __init__(self, monthYear, project, projectCode, contractor, trade, level, columndata):
        super().__init__(monthYear, project, projectCode, contractor, trade, level, columndata)

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
    string = 'MONTHYEAR ' + up_underscore(d[0][0:7]) +' '+ up_underscore(d[2][0:12]) +' '+ \
          up_underscore(df_num[0][1]) +' '+ up_underscore(df_num[0][2])
    for k in range(1, df_num.shape[1]):
        string += ' '+ up_underscore(df_num[k][2])
    string += ' '+ up_underscore(df_num[1][1]) + '_PER_MONTH'
    return string.split()


def process_grp(remaining,df_num, row_num, grp_name, CONTRACTOR, PROJCT,PROJCT_CD):
    # if remaining > 0 : raise("err")
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
            if rows == 0:
                pass
            if rows == 1:
                pass
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
    return rows, remaining, CONTRACTOR, PROJCT,PROJCT_CD


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


def complete_grp(remaining_num, df_num, row_num, grp_name,CONTRACTOR, PROJCT,PROJCT_CD):
    rows = 0
    seq = ['j','a','aj', 'nh', 'sub']
    if grp_name == 'none':
        print(f' {grp_name} {remaining_num}')
        while remaining_num > 0 and len(df_num) - row_num - rows > 0:
            remaining_num -= 1
            rows += 1
            print(f' process grp {seq[rows]}')

        print(f' complete grp {grp_name}')
        print()
        return rows, remaining_num


def start_process(df_num):
    COL = first_hdrs(df_num)
    PROJCT,PROJCT_CD = get_project(df_num[0][0])
    print(COL)
    return 3, COL,PROJCT,PROJCT_CD


def main(argv):
    MONTH = ''
    MONTHYR = ''
    PROJCT = ''
    PROJCT_CD = ''
    CONTRACTOR= ''
    TRAD = ''
    LEVL = ''
    script, filename, outfile, debug = argv
    reader = PyPDF2.PdfFileReader(open(filename, mode='rb'))
    m = reader.getNumPages()
    proc_pages = 1
    proc_dfs = 0
    beginning = True
    remaining = 0
    grp=''

    # Create the dictionary to capture the rows.

    line = Detail('', '', '', '', '', '', ['', '', '', '', '', '', '', '', '', ''])
    MONTHYR = str(filename)[len(filename) - 11:len(filename) - 4]
    MONTH = str(np.char.zfill(str(get_month(MONTHYR)), 2))

    while proc_pages <= m:
        print(f'starting page {proc_pages}')
        df0 = tabula.read_pdf(filename, pages=proc_pages, lattice=True, area=(11, 26, 582, 829),
                              pandas_options={'header': None})
        rows = 0
        proc_dfs = 0
        ct=''
        prj_name = ''
        prj_cd = ''
        while proc_dfs < len(df0):
            print(f' Processing DF number: {proc_dfs}')
            print(df0[proc_dfs])
            print()
            proc_rows = 0
            while proc_rows < len(df0[proc_dfs]):
                print(f' Processing row number: {proc_rows}')
                if remaining:
                    rows, remaining, CONTRACTOR, PROJCT,PROJCT_CD = process_grp(remaining, df0[proc_dfs], proc_rows, grp, CONTRACTOR, PROJCT,PROJCT_CD)
                    # complete_grp(remaining,df0[proc_dfs], proc_rows, grp, line)
                elif beginning:
                    rows,COL,PROJCT,PROJCT_CD= start_process(df0[proc_dfs])
                    beginning = False
                else:
                    grp = identify_grp(df0[proc_dfs],proc_rows)
                    rows, remaining,CONTRACTOR,PROJCT,PROJCT_CD= process_grp(remaining, df0[proc_dfs],proc_rows,grp, CONTRACTOR, PROJCT,PROJCT_CD)
                proc_rows += rows
            proc_dfs += 1
        proc_pages += 1


if __name__ == "__main__":
    main(argv)

# use the command below to run the parser:
# python3 src/parsers/pd_parser.py data/WorkforceUtilizationSummaryReportJan2019.pdf data2/WorkforceUtilizationSummaryReportJan20192 true | tee -a  proof.txt

