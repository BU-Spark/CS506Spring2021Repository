## Project Deliverable 1

Sufficient data should have been collected to perform a preliminary analysis of the data and attempt to answer one question relevant to your project proposal which you will submit as a pull request. If data has already been collected for your project you must answer two questions.

### Checklist

- [x] Collect and pre-process a preliminary batch of data
- [x] Perform a preliminary analysis of the data
- [x] Answer one key question
- [x] Refine project scope and list of limitations with data and potential risks of achieving project goal
- [x] Submit a PR with the above report and modifications to original proposal

### Refine project scope

For coffees and toners, clarify the concept of  “waste footprint” by replacing it with the notion of “waste volume”.

### Procedure

1. We removed all data which has "Unclassified" value at the column for "Part - Supplier Part Number".
2. We have calculated the number of requests for coffee and toner quarterly, monthly and yearly, and visualized the trends through ploting lines and bars.
3. We have plotted pie charts for reavealing the top 20 coffee products and top 20 toner products respectively with the most number of requestes within 5 years and visualized their request numbers through the histogram.
4. We found average waste value for plastic K-Cup Pods from [online open source](https://www.nature.com/articles/s41598-020-65058-1/tables/3) and estimated value for Coffee Creamer from [Amazon](https://www.amazon.com/International-Delight-102042-Coffee-Inspirations/dp/B0081V0BRM) to calculate waste weights for the top 20 coffee products with the most number of requests.

### Results
1. After classifying the data, we found out the top 10 Coffee products with the most request numbers within five years are:

- PR14470 WB Mason Company Breakfast Blend Coffee K-Cup Pods, 24/BX SMCREAG GMT6520 Coffee

- PR6450  WB Mason Company Dark Magic Extra Bold Coffee K-Cup Pods, 24/BX HALLOCK GMT4061 Coffee

- PR14045 WB Mason Company Nantucket Blend Coffee K-Cup Pods, 24/BX EGUIDER GMT6663 Coffee

- PR37974 WB Mason Company French Vanilla Coffee K-Cup Pods, 24/BX MARISM GMT6732 Coffee

- PR41358 WB Mason Company Half AND Half Liquid Coffee Creamer, 0.3 oz. Single-Serve Cups, 180/CS TONYWU ITD102042 Coffee

- PR6450  WB Mason Company	Hazelnut Coffee K-Cup Pods, 24/BX	HALLOCK	GMT6792	Coffee

- PR10034 WB Mason Company	French Roast Coffee K-Cup Pods, 24/BX	RSHEP	GMT6694	Coffee

- PR37943 WB Mason Company	Pike Place Roast Coffee K-Cup Pods, 24/BX	CHIPPIE	GMT9572	Coffee

- PR28300 WB Mason Company	Original Blend K-Cup Pods, 24/BX	JODITSUI	GMT0845	Coffee

- PR14382 WB Mason Company	Veranda Blend Coffee K-Cups Pods, 24/BX	YRODRIGU	GMT9577	Coffee

2. Answer one key questions: 

- What is the waste volume of the specified categories? 

- In the recent five years, the total waste weight for the top 18 different types of K-cups with the most total number is 1.512 tons, and the total waste for the top 2 different types of coffee creamer with the most total number is 0.4 kg.

### Refine limitations with data and potential risks of achieving project goals.

- For each product, the package measurements are different, such as “pod”, “box”, or “cups”. Products have different contents such as 10 pods, 24 pods, 40 cups or 70cups. Also, different packages have different weights. Analyzing each of them puts a heavy workload on us. Since there are a variety of  products, a careful standardization process shall be done.

- We do not have access to information about each product’s components and specific GHG emission and waste footprint value for each product.

- Since we need to analyze the data based on coffee types, but the information to identify a coffee is on the “description” column, it’s hard to directly obtain the coffee type to do any calculation or analysis so far. We might need a significant amount of time to categorize the types manually.

- It’s hard to identify a coffee type of some products based on its description.

### Follow-ups

We have sent email to our clients regarding to some potential questions about GHG emission for K-Cup Pods we want to ask Keurig company:

- We have scanned over [Keurig's 2019 Corporate Responsibility Report](https://www.keurigdrpepper.com/content/dam/keurig-brand-sites/kdp/files/KDP-CR-Report-2019.pdf) and it mentioned GHG emission regarding to its K-Cup Pods Product in their [report to CDP Climate Change Questionnaire 2019](https://www.keurigdrpepper.com/content/dam/keurig-brand-sites/kdp/files/KDP-CDP_Climate_Change_Questionnaire_2019-Final.pdf?a=bcd), it mentioned that "to meet our 2020 target of 100% of our K-Cup® pods being recyclable, we are changing the plastic material of the cup portion of the pod to be made from polypropylene vs. a multi-layered polystyrene material. Polypropylene as a material has a 27% lower emissions factor. We use GaBi data to quantify this." Could they specify the exact GHG emissions for Polypropylene as a material for K-Cup Pods in recent 5 years or could they provide the detailed Gabi emission factor for that like (kgCO2e/1kg PP material)? It may be better if they can provide us with some other Gabi emission factors other than considering CO2e they included in the calculation.  Could they specify the methodology they use like what parameters they considered in using Gabi to get GHG emission for manufacturing different types of Coffee products and give us a detailed number for Gabi emission factor for that (kgCO2e/1 kg coffee bean) in recent 5 years?

- Could they provide a list of the sizes for different types of K-Cup Pods Product they produce so that we could estimate the waste volume much easier?


### 3/4 2nd client meeting 

#### Questions from team 
1. We have done some rough processing to "WB Mason Toner and Coffee Purchase_no pricing data" and found out the most requests for coffee and toner cartridge within 5 years are Green Mountain Coffee: Breakfast Blend Coffee K-Cup Pods and HP 05A (CE505A) Toner Cartridge, Black respectively. To analyze their GHG emission from waste, we need to find out the material for packing them. We end up with #5 plastic polypropylene(PP) for K-cup Coffee and can't find the main composite for HP Toner Cartridge.

2. Then for Coffee Pods, we want to learn some reliable methods to find out its GHG emissions and end up with an article about Life Cycle Assessment of Compostable Coffee Pods: they have some insightful measure about the package of plastic coffee pod. I wonder if we want to achieve the goal for our project, do we need to go through some similar procedure? We have roughly gone through the EPA's WARM model and we find out the model requires some additional data like weight for the product in tons and landfill characteristics and we do not know how to get the exact weight for the product in our data; for HP Toner Cartridge Products, we end up with their website about ink cartridge recycling, which does not provide data about the ink cartridge waste that we can explore. We wonder if you can get access to some data about the waste weight for coffee and toner products in BU, that will help us a lot.

#### Project Updates
1. Calculate number of requests quarterly, yearly
2. Key questions to answer: 
a. What is the waste footprint of the specified categories?
b. What is the GHG footprint of the specified categories?
- Polypropylene #5 plastic(Keurig Green Mountain)
- HP Toner Cartridge


#### Suggestions:
- Finding one source of coffee that’s most utilized - use that for every other coffee product 
- Make assumption for average k-cup weights
- Want to know the weight of the waste 

- Waste volume from all of the coffee that we are consuming 
- Get GHG emissions 

##### BU’s three methods of toner waste
- Take back program with WB mason (driver pick up the toner waste)
- Every toner comes with a shipping return label, which goes back to the manufacturer 
- Send them to electronic local recycling company 


#### Follow-ups
- Send an email with all the questions that the team wants to ask to Keurig to Lisa
- Need information of how the product is transported to BU
- New questions: 
- What is the waste volume of the specified categories? (answer this first for deliverable 1!)
- Rescheduling the meeting on 3/18 because of wellness day
