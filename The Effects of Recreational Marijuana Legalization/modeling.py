import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
from sklearn.linear_model import LinearRegression

# DRUG DEATHS
df = pd.read_csv("./data/drugdeaths.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Drug Deaths before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Drug Deaths after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado Drug Deaths between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Drug Deaths between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Drug Deaths between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Drug Deaths before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Drug Deaths after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes in Colorado before and after 2012 was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[14:])
print("The average percentage increase of drug deaths each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of drug deaths each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of drug deaths each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of drug deaths each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Drug Death Rate in Colorado')
plt.xlabel('Year')
plt.ylabel('Drug Death Rate')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Drug Death Rate')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# GDP PER CAPITA
df = pd.read_csv("./data/gdp.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado GDP/Capita before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado GDP/Capita after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado GDP/Capita between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado GDP/Capita between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado GDP/Capita between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL GDP/Capita before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL GDP/Capita after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of GDP/Capita each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of GDP/Capita each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of GDP/Capita each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of GDP/Capita each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of GDP/Capita in Colorado')
plt.xlabel('Year')
plt.ylabel('GDP/Capita')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('GDP/Capita')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# TAX REVENUE PER CAPITA
df = pd.read_csv("./data/tax.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Tax Revenue/Capita before legalization:')
preyears = years[:9]
prevals = col[:9]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Tax Revenue/Capita after legalization:')
postyears = years[8:]
postvals = col[8:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 2004-2008
print('Linear Regression for Colorado Tax Revenue/Capita between 2004-2008:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Tax Revenue/Capita between 2008-2012:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Tax Revenue/Capita before legalization:')
preyears = years[:9]
prevals = usa[:9]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Tax Revenue/Capita after legalization:')
postyears = years[8:]
postvals = usa[8:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:9])
postchange = np.mean(percentchange[8:])
prechangeusa = np.mean(percentchangeusa[1:9])
postchangeusa = np.mean(percentchangeusa[8:])
print("The average percentage increase of Tax Revenue/Capita each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of Tax Revenue/Capita each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of Tax Revenue/Capita each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of Tax Revenue/Capita each year in the US after 2012 legalization was ", postchangeusa, "percent")
# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Tax Revenue/Capita in Colorado')
plt.xlabel('Year')
plt.ylabel('Tax Revenue/Capita')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[8:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Tax Revenue/Capita')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()


# UNEMPLOYMENT RATE
df = pd.read_csv("./data/unemployment.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Unemployment Rate before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Unemployment Rate after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado Unemployment Rate between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Unemployment Rate between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Unemployment Rate between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Unemployment Rate before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Unemployment Rate after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of the UE rate each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of the UE rate each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of the UE rate each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of the UE rate each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Unemployment Rate in Colorado')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# CIGARETTE SALES
df = pd.read_csv("./data/cig.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Cigarette Sales before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Cigarette Sales after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado Cigarette Sales between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Cigarette Sales between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Cigarette Sales between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Cigarette Sales before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Cigarette Sales after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of cigarette sales each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of cigarette sales each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of cigarette sales each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of cigarette sales each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Cigarette Sales in Colorado')
plt.xlabel('Year')
plt.ylabel('Cigarette Sales')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Cigarette Sales')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()


# ALCOHOL CONSUMPTION
df = pd.read_csv("./data/alccons.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Alcohol Consumption before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Alcohol Consumption after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado Alcohol Consumption between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Alcohol Consumption between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Alcohol Consumption between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Alcohol Consumption before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Alcohol Consumption after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of alcohol consumption each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of alcohol consumption each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of alcohol consumption each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of alcohol consumption each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Alcohol Consumption in Colorado')
plt.xlabel('Year')
plt.ylabel('Alcohol Consumption')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Alcohol Consumption')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# ADMISSION TO REHAB
df = pd.read_csv("./data/rehab.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado admission to rehab before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado admission to rehab after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado admission to rehab between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado admission to rehab between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado admission to rehab between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL admission to rehab before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL admission to rehab after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of rehab admissions each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of rehab admissions each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of rehab admissions each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of rehab admissions each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Rehab Admissions in Colorado')
plt.xlabel('Year')
plt.ylabel('Rehab Admissions')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Rehab Admissions')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# SUICIDE RATES
df = pd.read_csv("./data/suicide.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Suicide Rates before legalization:')
preyears = years[:9]
prevals = col[:9]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Suicide Rates after legalization:')
postyears = years[8:]
postvals = col[8:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 2004-2008
print('Linear Regression for Colorado Suicide Rates between 2004-2008:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Suicide Rates between 2008-2012:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL suicide rates before legalization:')
preyears = years[:9]
prevals = usa[:9]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL suicide rates after legalization:')
postyears = years[8:]
postvals = usa[8:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:9])
postchange = np.mean(percentchange[8:])
prechangeusa = np.mean(percentchangeusa[1:9])
postchangeusa = np.mean(percentchangeusa[8:])
print("The average percentage increase of suicide rates each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of suicide rates each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of suicide rates each year in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of suicide rates each year in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Suicide Rates in Colorado')
plt.xlabel('Year')
plt.ylabel('Suicide Rates')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[8:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Suicide Rates')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()

# Alcohol-Related Driving Fatalities
df = pd.read_csv("./data/alc.csv")

years = df.iloc[:,0].values
years = years.reshape(-1,1)
col = df.iloc[:,1].values
percentchange = df.iloc[:,3].values
usa = df.iloc[:,2].values
percentchangeusa = df.iloc[:,4].values

# Fitting a model for the data before legalization
print('Linear Regression for Colorado Alcohol-Related Driving Fatalities before legalization:')
preyears = years[:14]
prevals = col[:14]
preyears = preyears.reshape(-1, 1)
reg = LinearRegression().fit(preyears, prevals)
pre_int = reg.intercept_
pre_slope = reg.coef_
print("Intercept is:", pre_int)
print("Slope is:", pre_slope[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for Colorado Alcohol-Related Driving Fatalities after legalization:')
postyears = years[13:]
postvals = col[13:]
postyears = postyears.reshape(-1, 1)
reg1 = LinearRegression().fit(postyears, postvals)
post_int = reg1.intercept_
post_slope = reg1.coef_
print("Intercept is:", post_int)
print("Slope is:", post_slope[0])
print()

# Fitting a model for years 1999-2005
print('Linear Regression for Colorado Alcohol-Related Driving Fatalities between 1999-2003:')
firstyears = years[:4]
firstvals = col[:4]
firstyears = firstyears.reshape(-1,1)
reg2 = LinearRegression().fit(firstyears, firstvals)
f_int = reg2.intercept_
f_slope = reg2.coef_
print("Intercept is:", f_int)
print("Slope is:", f_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Alcohol-Related Driving Fatalities between 2004-2008:')
secyears = years[4:9]
secvals = col[4:9]
secyears = secyears.reshape(-1,1)
reg3 = LinearRegression().fit(secyears, secvals)
s_int = reg3.intercept_
s_slope = reg3.coef_
print("Intercept is:", s_int)
print("Slope is:", s_slope[0])
print()

# Fitting a model for years 2006-2012
print('Linear Regression for Colorado Alcohol-Related Driving Fatalities between 2009-2012:')
thirdyears = years[9:14]
thirdvals = col[9:14]
thirdyears = thirdyears.reshape(-1,1)
reg4 = LinearRegression().fit(thirdyears, thirdvals)
t_int = reg4.intercept_
t_slope = reg4.coef_
print("Intercept is:", t_int)
print("Slope is:", t_slope[0])
print()

# Fitting a model for USA
# Fitting a model for the data before legalization
print('Linear Regression for NATIONAL Alcohol-Related Driving Fatalities before legalization:')
preyears = years[:14]
prevals = usa[:14]
preyears = preyears.reshape(-1, 1)
reg5 = LinearRegression().fit(preyears, prevals)
pre_int_us = reg5.intercept_
pre_slope_us = reg5.coef_
print("Intercept is:", pre_int_us)
print("Slope is:", pre_slope_us[0]) 
print()

# Fitting a model for the data after legalization
print('Linear Regression for NATIONAL Alcohol-Related Driving Fatalities after legalization:')
postyears = years[13:]
postvals = usa[13:]
postyears = postyears.reshape(-1, 1)
reg6 = LinearRegression().fit(postyears, postvals)
post_int_us = reg6.intercept_
post_slope_us = reg6.coef_
print("Intercept is:", post_int_us)
print("Slope is:", post_slope_us[0])
print()

# Basic analysis
change = (post_slope[0]-pre_slope[0])/(pre_slope[0])*100
print("The percent change in slopes was ", change, "percent")
prechange = np.mean(percentchange[1:14])
postchange = np.mean(percentchange[13:])
prechangeusa = np.mean(percentchangeusa[1:14])
postchangeusa = np.mean(percentchangeusa[13:])
print("The average percentage increase of alcohol-related driving fatalities each year in Colorado before 2012 legalization was ", prechange, "percent")
print("The average percentage increase of alcohol-related driving fatalities each year in Colorado after 2012 legalization was ", postchange, "percent")
print("The average percentage increase of alcohol-related driving fatalities in the US before 2012 legalization was ", prechangeusa, "percent")
print("The average percentage increase of alcohol-related driving fatalities in the US after 2012 legalization was ", postchangeusa, "percent")

# Plotting the linear regression model
plt.xticks(years[::2])
plt.title('Linear Regression of Alcohol-Related Driving Fatalities in Colorado')
plt.xlabel('Year')
plt.ylabel('Alcohol-Related Driving Fatalities')
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization')
plt.plot(firstyears, reg2.predict(firstyears), color='magenta', label='Short-term trends')
plt.plot(secyears, reg3.predict(secyears), color='magenta')
plt.plot(thirdyears, reg4.predict(thirdyears), color='magenta')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
# Plotting the difference between what we expected (assuming no legalization) and what we found with legalization
coords = []
postpredictions = reg1.predict(postyears)
prepredictions = reg.predict(years[13:])
for i in range(len(postpredictions)):
    coords.append((prepredictions[i], postpredictions[i]))
predyears = []
for j in range(len(postyears)):
    predyears.append(postyears[j][0])
plt.plot((predyears,predyears),([i for (i,j) in coords], [j for (i,j) in coords]),c='green')
plt.legend()
plt.show()
# Plotting national trendline
plt.xticks(years[::2])
plt.title('Comparing Colorado with National Trend')
plt.xlabel('Year')
plt.ylabel('Alcohol-Related Driving Fatalities')
plt.scatter(years, usa, color='orange', s=5)
plt.scatter(years, col, color='red', s=5)
plt.plot(years, reg.predict(years),color='red', label='Long-term trend before legalization (Colorado)')
plt.plot(postyears, reg1.predict(postyears),color='blue', label='Trend after legalization (Colorado)')
plt.plot(years, reg5.predict(years),color='orange', label='Long-term trend before legalization (USA)')
plt.plot(postyears, reg6.predict(postyears),color='purple', label='Trend after legalization (USA)')
plt.axvline(x=2012, color='black', label='2012 (Legalization Year)')
plt.legend()
plt.show()