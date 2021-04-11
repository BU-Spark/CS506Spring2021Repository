import PyPDF2
# convert all PDFs in a directory
import pandas as pd
import tabula
from sys import argv

def print_the_df(line, outfile):
    df5 = pd.DataFrame(line.get_rows())
    df6 = pd.DataFrame(line.get_ajr())
    df7 = pd.DataFrame(line.get_newh())
    df8 = pd.DataFrame(line.get_sub())
    df9 = pd.DataFrame(line.get_tot())
    df10 = pd.DataFrame(line.get_gtot())
    print(df5)
    print(df6)
    print(df7)
    print(df8)
    print(df9)
    print(df10)
    cnt = 0
    outfile1 = outfile + str(cnt) + '.csv'
    df5.to_csv(outfile1, index=False)
    cnt += 1
    outfile1 = outfile + str(cnt) + '.csv'
    df6.to_csv(outfile1, index=False)
    cnt += 1
    outfile1 = outfile + str(cnt) + '.csv'
    df7.to_csv(outfile1, index=False)
    cnt += 1
    outfile1 = outfile + str(cnt) + '.csv'
    df8.to_csv(outfile1, index=False)
    cnt += 1
    outfile1 = outfile + str(cnt) + '.csv'
    df9.to_csv(outfile1, index=False)
    cnt += 1
    outfile1 = outfile + str(cnt) + '.csv'
    df10.to_csv(outfile1, index=False)

class SubLedgerParser(object):
    def __init__(self,df):
        self.input = df
        self.state = StateMgr()
        self.hdrs = []


    def first_hdrs(self):
        # clean_df = df[0].replace('\r', ' ', regex=True)
        # clean_df[0].map('{:,d}'.=format)
        # df2['PROJECT'] = df2['PROJECT'].str.replace(',', '').str.replace('$', '').astype(int)
        # clean_df = df2[0].replace({'\r', ' '}, regex=True)
        self.hdrs = ['MONTHYEAR', 'PROJECT', 'PROJECT_CODE', 'CONTRACTOR', 'CONSTRUCTION_TRADE']
        self.hdrs.append(str(self.input[0].values[2][0]).replace(' ', '_',).replace('\r', ' ').upper())
        stats = []
        for k in range(1, len(self.input[0].values[2])):
            stats.append(str(self.input[0].values[2][k]).replace('\r', '_').upper())
        self.hdrs.append(stats)
        self.hdrs.append(str(self.input[0].values[1][1]).replace(' ', '_').upper()+'_PER_MONTH')
        return self.hdrs


    def set_hdrs(self,l):
        self.hdrs = l


    def get_hdrs(self):
        return self.hdrs


    def get_first_prj(self):
        self.state.next_one()
        prj_strings = str(self.input[0][0][0]).split('\r')
        return prj_strings[1], prj_strings[3]


    def get_prj(self):
        self.state.next_one()
        # return self.input[0].columns.values[0][0:7]
        prj_strings = str(self.input[0][0][0]).split('\r')
        return prj_strings[1], prj_strings[3]


    def get_1stcontractor(self):
        self.state.next_one()
        # return self.input[1].columns.values[0]
        return self.input[1][0][0]


    def get_contractor(self,row):
        self.state.next_one()
        # return self.input[1].columns.values[0]
        return self.input[1][row][0]


    def get_trade(self,row):
        self.state.next_one()
        return (str(self.input[1].values[row][0]))


    def get_level(self,row):
        self.state.next_one()
        return str(self.input[1].values[row][1]).replace('Journey', 'Journeyman').capitalize()


    def get_dtls(self,row):
        dict1={}
        for k in range(0, len(self.input[1].values[0]) - 2):
            dict1[self.hdrs[6][k]] \
                = self.input[1].values[row][k + 2]
        return dict1


class StateMgr(object):
    def __init__(self):
        self.state = 'start'
        self.state_branch = ''
        self.state_order = []
        self.state_addtl = ['a_j_ratio', 'new_hire']
        self.state_tots = ['trd_sub', ['cont_sub','trade'],['prj_tot','contractor'],'end']
        self.state_order = ['start', 'prj','contractor','trade', 'level', 'journey',
                            'apprent']+self.state_addtl+ self.state_tots


    def get_state(self):
            return self.state


    def choose(self,signature):

        if signature == 'Total f':
            self.state_branch = 'cont_sub'
            return self.state_branch

        if signature == 'Total  ':
            self.state_branch = 'prj_tot'
            return self.state_branch

        self.state_branch = self.state[1]
        return self.state_branch


    def next_one(self):
        for i in range(len(self.state_order)):
            if self.state_order[i] == self.state:
                if self.state == self.state_order[len(self.state_order)-1]:
                    self.state = self.state_order[0]
                else:
                    self.state = self.state_order[i+1]
                return self.state
        return self.state == 'Broken'


    def back_one(self):
        for i in range(0,len(self.state_order),-1):
            if self.state_order[i] == self.state:
                if self.state == self.state_order[0]:
                    self.state = self.state_order[len(self.state_order)-1]
                else:
                    self.state = self.state_order[i-1]
                return self.state
        return self.state == 'Broken'


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


def process_line_group(l, line, parse_df):
    line.set_contr(parse_df.get_1stcontractor())
    a, b = parse_df.get_first_prj()
    line.set_prj(a, b)
    line.set_trd(parse_df.get_trade(l))
    dline = 1
    while l < parse_df.input[1].shape[0] - 1 and dline <= 5:
        line.set_lvl(parse_df.get_level(l))
        print(f'line {l} of type {parse_df.state.get_state()}')
        line.set_dict(parse_df.get_dtls(l))
        parse_df.state.next_one()
        l += 1;
        dline += 1
    return l


def main(argv):
    script, filename, outfile = argv
    reader = PyPDF2.PdfFileReader(open(filename, mode='rb'))
    m = reader.getNumPages()
    # print(reader)
    print(m)
    template = False
    for i in range(3):
    # for i in range(m):
        n = i + 1
        df2 = tabula.read_pdf(filename, pages=n, lattice=True, area=(11, 26, 582, 829), pandas_options={'header': None})
        if not template:
            parse_df = SubLedgerParser(df2)
            line = Detail('', '', '', '', '', '', ['', '', '', '', '', '', '', '', '', ''])
            line.set_monthyr(str(filename)[len(filename) - 13:len(filename) - 4])
            if len(parse_df.input[0]) > 0:
                parse_df.first_hdrs()
            template = True
        if n >= 1 and n < 3:
            if len(df2) > 1:
                l = 1
                # ALL Trades are in all upper case
                # if str(df2[1].values[0][0]) == str(df2[1].values[0][0]).upper():  # 'trd'
                print(f'line {l} of type {parse_df.state.get_state()}')

                while l < df2[1].shape[0]:
                    l = process_line_group(l, line, parse_df)
                    if l == df2[1].shape[0]-1 : break
                    #
                    # if len(parse_df.state.get_state()) == 2:
                    #     twin = 'cont_sub'  #parse_df.state.choose(str(df2[1][l][0])[0:7])
                    # if twin == 'cont_sub':
                    #     sline = 1
                    #     while l < df2[1].shape[0] - 1 and sline < 6:
                    #         line.set_lvl(parse_df.get_level(l))
                    #         print(f'line {l} of type {parse_df.state.get_state()}')
                    #         line.set_dict(parse_df.get_dtls(l))
                    #         parse_df.state.next_one()
                    #         l += 1; sline += 1
                    # else:  # Trade
                    #     line.set_trd(parse_df.get_trade(l))
                    #
                    # if len(parse_df.state.get_state()) == 2: parse_df.state.choose(str(df2[1][l][0]))
                    # if str(df2[1][0][0]).lower() == 'Total':
                    #     if twin == 'prj_tot':
                    #         pline = 1
                    #         while l < df2[1].shape[0] - 1 and pline < 5:
                    #             line.set_lvl(parse_df.get_level(l))
                    #             print(f'line {l} of type {parse_df.state.get_state()}')
                    #             line.set_dict(parse_df.get_dtls(l))
                    #             parse_df.state.next_one()
                    #             l += 1; pline += 1
                    #     else:  # contractor
                    #         pass
                    #
                    # if str(df2[1][0][0]).lower() == 'end of data for project:':
                    #     proj_desc = str(df2[0][0][1]).lower()
                    #     print(proj_desc)
                    #     a, b = parse_df.get_first_prj()
                    #     line.set_prj(a, b)
                    # l += 1

    print_the_df(line, outfile)


if __name__ == "__main__":
    main(argv)

    # detail1 = Detail( 'April2019', 'AEP1802E UT1 C Utility Simple Fix','AEP1802E UT1 C',
    #            'Batallas Electric Inc.', 'Electrician', 'Journeyman',
    #            [17.5 , 0.0 , 0.0 , 0.0, 0.0 , 0.0 , 0.0, 0.0, 0.0, 17.5])
    # detail1.print_c()
    # df4.loc[len(df4.columns.tolist())] = contractor_hdr
    # df['CONTRACTOR_HDR'] = df['CONTRACTOR_HDR'].replace(['old value'], 'new value')