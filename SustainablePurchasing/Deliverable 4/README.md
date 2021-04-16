### Project Deliverable 4 (v2 Final Report)

This is a draft of your final report that has been reviewed by your client. It includes all visualizations, results, data, and code up to this point, along with proper documentation on how to reproduce your results, compile and use your codebase, and navigate your dataset. Your team will submit this as a PR.

### Project Description

The goal for the project is to explore the working supplies requests and expenditure from BU staff based on which we analyze the waste volume and GHG emission of the main categories (i.e. Coffee and Ink Cartridge) and their subcategories. According to the analysis, we are expected to provide some insightful suggestions regarding to BU sustainability in the future.


### Analysis Questions

* What is the waste volume of the specified categories?
* what is the weight of the waste to represent the waste volume of the products and use some carbon emission of the main material to represent product emission?
* What are ways the University could ask the vendors to change the options they offer ? e.g. buy less K-cup, more bag coffee
* What is the difference between the weight of each componets for the coffee and creamer waste

### Data description

We have received three batch of data from clients and collected two batch of supplemented data on our own.
* First batch of data is about the toner and coffee purchases from WB Mason including requisition ID, requisitioning date, description (of product), shopper ID and supplier part number. Based on it, we gathered data of waste volume and CO2 emission data for different types of coffee products.
* Second batch of data focuses on the spend of each request including department unit name, total invoice quantity and total paid etc.
* Third batch of data is about paper and toner requests from different departments and their branches including requisition ID, requisitioning date, description, unit name, fc name, etc.

### Deliverable 1

Procedure:
* We removed all data which has "Unclassified" value at the column for "Part - Supplier Part Number".
* We have calculated the number of requests for coffee and toner quarterly, monthly and yearly, and visualized the trends through ploting lines and bars.
* We have plotted pie charts for reavealing the top 20 coffee products and top 20 toner products respectively with the most number of requestes within 5 years and visualized their request numbers through the histogram.
* We found average waste value for plastic K-Cup Pods from online open source and estimated value for Coffee Creamer from Amazon to calculate waste weights for the top 20 coffee products with the most number of requests.

Conclusion: 
* In the recent five years, the total waste weight for the top 18 different types of K-cups with the most total number is 1.512 tons, and the total waste for the top 2 different types of coffee creamer with the most total number is 0.4 kg.

### Deliverable 2

Procedure:

* We have collected the packing type, weight and carbon emissions (if possible) for top 10 ground coffee, top 10 coffee creamer and top 10 K-Cup products in quantity from the categories of our previous analysis.

* We have collected the total weight, size, weight of toner and carbon emissions (if possible) for top 10 ink cartridge in quantity.

* We have received a secondary batch of data about the toner and coffee requests from different BU departments and do some pre-process of the data.

Conclusion:
We answered the following question:
* Total waste weight for top 10 K-Cup Coffee
* Total waste weight for the top two creams

### Deliverable 3

Procedure:
* We calculated carbon emission estimate of top 10 K-Cup, top 10 consumed ground coffee and top 10 consumed coffee creamer
* We calculated the cost that different departments spent on K-cups and Bagged Coffee, and the top 10 departments that requested Toner and Coffee most in the last 5 years respectively. 
* We analyzed the order frequency of coffee, toner and paper, represented the top ten items in the order times in these two categories, and drew a line chart of the order frequency of that 20 most frequently used items

Conclusion: 
* The carbon emissions of a K-Cup is 26.4g.
* The carbon emission of top 10 consumed ground coffee is about 233.52616kg carbon dioxide.
* The carbon emission of the top 10 consumed coffee creamer is about 14021.788kg carbon dioxide.
* School of Medicine and School of Public Health behold one place in top 3 among the rank of ordering numbers and ordering spends from different departments of BU.
* K-Cup coffee pods is ordered every 0.7 days on average, toner cartridge is ordered every 5.1 days on average and paper is ordered every 1.12 days on average. 