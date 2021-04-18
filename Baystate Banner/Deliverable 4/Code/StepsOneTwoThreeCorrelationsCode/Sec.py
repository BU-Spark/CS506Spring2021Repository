# Coding
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas import DataFrame
eleven = pd.DataFrame(pd.read_excel("2011_CityCouncil_Results_Race_Turnout.xlsx"))
thirteen = pd.DataFrame(pd.read_excel("2013_CityCouncil_Race_Turnout_Results.xlsx"))
fifteen = pd.DataFrame(pd.read_excel("2015_city_council.xlsx"))
seventeen =  pd.DataFrame(pd.read_excel("2017_CityCouncil_AtLarge_Turnout_Race.xlsx"))
nineteen = pd.DataFrame(pd.read_excel("2019_CityCouncil_Race Turnout.xlsx"))
Turnout = pd.read_csv("CC_turnout_all_years.csv")

    
plt.figure()
x = eleven['Black Percentage']
y = Turnout['Turnout_2011']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Black Percentage','Turnout_2011'])
one = data['Black Percentage']
two = data['Turnout_2011']
sns.regplot(x = one,y= two,data = data)
plt.savefig('BlackX_Turnout2011Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = eleven['White Percentage']
y = Turnout['Turnout_2011']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['White Percentage','Turnout_2011'])
one = data['White Percentage']
two = data['Turnout_2011']
sns.regplot(x = one,y= two,data = data)
plt.savefig('WhiteX_Turnout2011Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = eleven['Hispanic Percentage']
y = Turnout['Turnout_2011']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Hispanic Percentage','Turnout_2011'])
one = data['Hispanic Percentage']
two = data['Turnout_2011']
sns.regplot(x = one,y= two,data = data)
plt.savefig('HispanicX_Turnout2011Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = eleven['Asian Percentage']
y = Turnout['Turnout_2011']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Asian Percentage','Turnout_2011'])
one = data['Asian Percentage']
two = data['Turnout_2011']
sns.regplot(x = one,y= two,data = data)
plt.savefig('AsianX_Turnout2011Y')
plt.show(block = False)
plt.pause(2)
plt.close()


########################

plt.figure()
x = thirteen['Black Percentage']
y = Turnout['Turnout_2013']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Black Percentage','Turnout_2013'])
one = data['Black Percentage']
two = data['Turnout_2013']
sns.regplot(x = one,y= two,data = data)
plt.savefig('BlackX_Turnout2013Y')
plt.show(block = False)
plt.pause(2)
plt.close()



plt.figure()
x = thirteen['White Percentage']
y = Turnout['Turnout_2013']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['White Percentage','Turnout_2013'])
one = data['White Percentage']
two = data['Turnout_2013']
sns.regplot(x = one,y= two,data = data)
plt.savefig('WhiteX_Turnout2013Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = thirteen['Hispanic Percentage']
y = Turnout['Turnout_2013']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Hispanic Percentage','Turnout_2013'])
one = data['Hispanic Percentage']
two = data['Turnout_2013']
sns.regplot(x = one,y= two,data = data)
plt.savefig('HispanicX_Turnout2013Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = thirteen['Asian Percentage']
y = Turnout['Turnout_2013']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Asian Percentage','Turnout_2013'])
one = data['Asian Percentage']
two = data['Turnout_2013']
sns.regplot(x = one,y= two,data = data)
plt.savefig('AsianX_Turnout2013Y')
plt.show(block = False)
plt.pause(2)
plt.close()

########################

plt.figure()
x = fifteen['Black Percentage']
y = Turnout['Turnout_2015']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Black Percentage','Turnout_2015'])
one = data['Black Percentage']
two = data['Turnout_2015']
sns.regplot(x = one,y= two,data = data)
plt.savefig('BlackX_Turnout2015Y')
plt.show(block = False)
plt.pause(2)
plt.close()



plt.figure()
x = fifteen['White Percentage']
y = Turnout['Turnout_2015']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['White Percentage','Turnout_2015'])
one = data['White Percentage']
two = data['Turnout_2015']
sns.regplot(x = one,y= two,data = data)
plt.savefig('WhiteX_Turnout2015Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = fifteen['Hispanic Percentage']
y = Turnout['Turnout_2015']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Hispanic Percentage','Turnout_2015'])
one = data['Hispanic Percentage']
two = data['Turnout_2015']
sns.regplot(x = one,y= two,data = data)
plt.savefig('HispanicX_Turnout2015Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = fifteen['Asian Percentage']
y = Turnout['Turnout_2015']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Asian Percentage','Turnout_2015'])
one = data['Asian Percentage']
two = data['Turnout_2015']
sns.regplot(x = one,y= two,data = data)
plt.savefig('AsianX_Turnout2015Y')
plt.show(block = False)
plt.pause(2)
plt.close()



########################

plt.figure()
x = seventeen['Black Percentage']
y = Turnout['Turnout_2017']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Black Percentage','Turnout_2017'])
one = data['Black Percentage']
two = data['Turnout_2017']
sns.regplot(x = one,y= two,data = data)
plt.savefig('BlackX_Turnout2017Y')
plt.show(block = False)
plt.pause(2)
plt.close()



plt.figure()
x = seventeen['White Percentage']
y = Turnout['Turnout_2017']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['White Percentage','Turnout_2017'])
one = data['White Percentage']
two = data['Turnout_2017']
sns.regplot(x = one,y= two,data = data)
plt.savefig('WhiteX_Turnout2017Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = seventeen['Hispanic Percentage']
y = Turnout['Turnout_2017']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Hispanic Percentage','Turnout_2017'])
one = data['Hispanic Percentage']
two = data['Turnout_2017']
sns.regplot(x = one,y= two,data = data)
plt.savefig('HispanicX_Turnout2017Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = seventeen['Asian Percentage']
y = Turnout['Turnout_2017']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Asian Percentage','Turnout_2017'])
one = data['Asian Percentage']
two = data['Turnout_2017']
sns.regplot(x = one,y= two,data = data)
plt.savefig('AsianX_Turnout2017Y')
plt.show(block = False)
plt.pause(2)
plt.close()

########################

plt.figure()
x = nineteen['Black Percentage']
y = Turnout['Turnout_2019']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Black Percentage','Turnout_2019'])
one = data['Black Percentage']
two = data['Turnout_2019']
sns.regplot(x = one,y= two,data = data)
plt.savefig('BlackX_Turnout2019Y')
plt.show(block = False)
plt.pause(2)
plt.close()



plt.figure()
x = nineteen['White Percentage']
y = Turnout['Turnout_2019']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['White Percentage','Turnout_2019'])
one = data['White Percentage']
two = data['Turnout_2019']
sns.regplot(x = one,y= two,data = data)
plt.savefig('WhiteX_Turnout2019Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = nineteen['Hispanic Percentage']
y = Turnout['Turnout_2019']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Hispanic Percentage','Turnout_2019'])
one = data['Hispanic Percentage']
two = data['Turnout_2019']
sns.regplot(x = one,y= two,data = data)
plt.savefig('HispanicX_Turnout2019Y')
plt.show(block = False)
plt.pause(2)
plt.close()


plt.figure()
x = nineteen['Asian Percentage']
y = Turnout['Turnout_2019']
mydict = dict(sorted(zip(x,y )))
data = pd.DataFrame(list(mydict.items()),columns = ['Asian Percentage','Turnout_2019'])
one = data['Asian Percentage']
two = data['Turnout_2019']
sns.regplot(x = one,y= two,data = data)
plt.savefig('AsianX_Turnout2019Y')
plt.show(block = False)
plt.pause(2)
plt.close()


