# BU Sustainable Purchasing Program
## Problem Statement
Boston University strives to be an industry leader in reducing greenhouse gas emissions and achieving Zero Waste as outlined in Boston University’s Climate Action Plan by embracing best practices for sustainable sourcing and procurement of goods and services. This project will begin to measure BU's Scope 3 emissions as related to its procurement. 


## Meeting Schedule

Weekly Meeting with the PM, Lin, Anqi, in Thurs 8:00 AM - 9:30 AM,  
With BU Sustainability, Lisa Tornatore and Meghan Mcdonough - biweekly in Thurs 8:00 AM - 9:30 AM,   
Second meeting with the client on Thurs March 4th,  
Spark Liason - Greta Bruce  

## Contact List

Client: Tornatore, Lisa Marie <lisamt@bu.edu>,  
Client: Mcdonough, Meghan J <meghanjm@bu.edu>,  
Spark Liason: Greta Bruce <gretab@bu.edu>,     
PM: Lin, Anqi <anqilin@bu.edu>,  
Zeng, Xiongxin <zeng459@bu.edu>,  
Dong, Meichen <jazzmyn@bu.edu>,  
Cui, Tinghe <jamescui@bu.edu>,  
Li, Zhi <mikelili@bu.edu>,  
Yu, Tian <yutian12@bu.edu>  

Github accounts  
milesway, jazzmynd, Tinghecui, XiongxinZ, tianjzjz

## Data Sources
The data is collected by BU Sustainability. They sort it by time and keep in a Excel file. The file included BU office toner and coffee purchases from WB Mason.  
We have also be provided BU Sustainability annul report as reference.  
http://www.bu.edu/sustainability/files/2020/04/BU-Sustainability-2019AnnualReport-pages-20-04-17.pdf  

## Project Scope
Query on recent five-year BU staff’s demands on toner and coffee.  
GHG emission on producing tonor and coffee.  


## Questions to be Answered in Analysis
The client is seeking to understand the most impactful categories of BU spend as it relates to its Scope 3 greenhouse gas emissions so we can make effective policy determinations and/or limit categories/products available for purchase by the BU community.  
What are ways the University could influence purchasing on behalf of its departments as a result of the data analysis toward waste and GHG?  
What is the waste footprint of the specified categories?  
What is the GHG footprint of the specified categories?  
How could BU track its Scope 3 emissions on a long-term basis as it relates to its procurement, given the breadth of products, services, and suppliers available? What data is missing from the supplier that would help answer the above questions?  

## Methods
For scraping:  Selenium webdriver is utilized to find the greenhouse gas emissions of coffee and Toner/the price of toner and coffee.   
For cleaning and preprocessing: use Pandas to organize the dataset into dataframes for faster computation. Data visualization libraries: use Matplotlib to create static, animated, and interactive visualizations in python EPA Sustainable Materials Management Tool  
For data visualization libraries such as Matplotlib, Seaborn, and Bokeh (interactive web-integratable visualizations). 


## Discussion and Limitations
We only focus on tonor and coffee consumption for investigating sustainable purchasing, not so much freedom.  
It may be challenging to trace the GHG footprint of tonor since we need to scrape some information from the merchants, not sure if they publish the details online.  
Right now we only have “WB Mason Toner and Coffee Purchases_no pricing” data at hand and the valuable attributes are “date”, “ERP Supplier”, “Product Description” and “Category”. There’s not many numeric attributes to work on and we need to find a way to separate and classify the non-numeric attributes.  
Note: The client is also interested in the information the project needs when collecting data, especially the data that need to start collection from now. And how could BU track its Scope 3 emissions on a long-term basis as it relates to its procurement, given the breadth of products, services, and suppliers available? 
