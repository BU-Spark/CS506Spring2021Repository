"""
Generate plot for project data

Project Started: April.25.2021
Project Concluded: April.28.2021
"""

###Import Lib
import pandas as pd
import matplotlib.pyplot as plt
import progressbar

###Global Settings
datadir = "E:/Personal Sync/Academic/Spring 2021/CS 506/Homework/project/covid-project/data/"
outdir = "E:/Personal Sync/Academic/Spring 2021/CS 506/Homework/project/covid-project/output/"

##Uncomment and comment to switch dataset
#dfname = "raw_concatenated.csv"
dfname = "israeli/corona_tested_individuals_ver_006.english.csv"

#round to X decimal for float
roundn = 6

#whitelist some values to avoid type conversion
wlist = ["covid19_test_results", "swab_type", "age"]


######Begin Functions
###Load data from file
def getdata(dataloc):
    return pd.read_csv(dataloc)

#get nan for all data
def getnan(rdata):
    nan = rdata.isna().any(axis=1).sum()
    print(nan)
    
#write a specific file to a system location with content
def writefile(filename, content):
    res = open(filename, "w")
    lenf1 = len(content)
    bar = progressbar.ProgressBar(maxval=lenf1, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    cnt = 0
    for i in content:
        res.write(str(i))
        res.write("\n")
        cnt += 1
        bar.update(cnt)
    bar.finish()
    res.close()

#get histo plot for specific column
def get_histo(rdata, cname):
    if (cname in wlist):
        pass
    else:
        rdata = rdata.applymap(str)
    testr = rdata[cname]
    plt.hist(testr)
    plt.title(cname)
    plt.ylabel('Number of Cases')
    plt.savefig(outdir + cname + "_histogram.png")
    plt.show()
    return

#get bar chart
def get_bar(rdata, cname):
    #rdata = rdata.applymap(str)
    testr = rdata[cname]
    plt.bar(testr)
    plt.title(cname)
    plt.ylabel('Number of Cases')
    plt.savefig(outdir + cname + "_barchart.png")
    plt.show()
    return    

#get number of nan in a series
def get_nan(rdata):
    return rdata.isna().sum()

#main function
def main():
    dloc = datadir + dfname
    rawd = getdata(dloc)
    #getnan(rawd)
    
    #get histogram
    for col in rawd.columns:
        get_histo(rawd, col)
    
    #count nan values
    res = []
    #get row length
    rlen = len(rawd.index)
    res.append("Number of NaN values and its percentage in each column")
    for col in rawd.columns:
        n = get_nan(rawd[col])
        #get percentage
        perc = (n/rlen)*100
        r = col + " : " + str(n) + "   Percentage: " + str(round(perc, roundn)) + "%"
        res.append(r)    
    writefile(outdir + "number_of_nan.txt", res)
    #write to file
    
    return
#invoke the main function
if __name__== "__main__":
    main()
