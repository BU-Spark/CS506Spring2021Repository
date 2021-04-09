# Deliverable 3: Introduction

This document summarizes the work done for Deliverable 3, for the BU Spark! project, Spring 2021, MAPC Broadband Digital Equity in MA. This document is split into two parts:

1. This section, which acts as an overview to this deliverable
2. The section titled "Deliverable 3: Final Report Draft," which assumes the role of an initial draft for our final report in this project.

Date: 04/09/21

## Student Team

This project has two different teams, denoted MAPC team 1 and MAPC team 2. We represent team 2. There are five students, and one project manager for team 2:

- Adam Streich
- Jenny Li
- Nathan Lauer
- Yutong Shen
- Zhixing Zhao

The project manager is Kamran Arif.

## Contact

- Ryan Kelly, [RKelly@mapc.org](mailto:RKelly@mapc.org) Digital Services lead at the MAPC

- Matt Zagaja, [mzagaja@mapc.org](mailto:mzagaja@mapc.org) , Lead civic web developer at the MAPC


## Organization

The Metropolitan Area Planning Council - MAPC

## Purpose

In this deliverable, we present our continuing work with the MLAB and Ookla datasets. Notably, we also introduce a new dataset -- 2014-2018 census income data -- and correlate broadbands speeds against this data. As with previous deliverables, there are two primary outcomes of this deliverable.

The first outcome is a continuing analysis of the datasets, with a particular focus on the following:

- Broadband speed measurement density in the Ookla dataset
- Understanding download and upload speeds per municipality in the Ookla dataset
- Correlating MLAB broadband speed against median household income, per municipality 
- Correlating Ookla download speed against median household income, per municipality.

The second outcome of this deliverable is an initial draft of our final report for this project. As such, the remaining sections will flow slightly differently than in previous deliverables; the following are a draft of our initial report. Note that we have included work from both previous deliverables and this deliverable in the upcoming sections. Each section is demarcated with the deliverable the associated work was completed in, so our progress towards this deliverable should be clear.

<div class="page-break"></div>

# Deliverable 3: Final Draft Report 

We present the work completed towards the BU, Spark! project, Spring 2021, MAPC Broadband Digital Equity in MA. 

##### Student Team

This project has two different teams, denoted MAPC team 1 and MAPC team 2. We represent team 2. There are five students, and one project manager for team 2: Adam Streich, Jenny Li, Nathan Lauer, Yutong Shen, and Zhixing Zhao. The project manager is Kamran Arif.

## Abstract

In this work, we construct datasets of measured internet speeds from two different organizations, MLAB and Ookla, in the year 2020. MLAB measures speed when someone quires google along the lines of "how fast is my internet," and measures a simulated network request as if it propagated across a significant portion of the larger internet network. Ookla, on the other hand, measures speed at speedtest.net, and presents a measerument of someone's local ISP server's speed. We further analyze this data on a per municipality basis, and the MLAB data on a per provider basis [note: some of this work remains to be done for deliverable 4]. We present descriptive statistics of internet speeds during 2020, and maps of upload and download speeds for each municipality in the state of Massachusetts. We also present this data as correlated against household income data from the 2014-2018 census. Finally, we discuss a number of key findings in the analysis of these datasets. First, there is a significant difference between measured Ookla speeds and measured MLAB speeds. Second, there exists an upwards correlation between MLAB broadband speeds and median household income; as median household income increases, average broadband speed increases as well. Third, the vast majority of municipalities are significantly under the desired 100/100 download/upload speeds in mega-bits-per-second (Mbps), with many not even reaching 50 Mbps. Fourth, there exists significant disparity in broadband coverage across the state. [note: some of this work remains to be done for deliverable 4]

## Motivation

The Metropolitan Area Planning Council (MAPC) provides planning capacity to municipalities within Massachusetts in a number of different capicities. Recently, they have turned their attention towards broadband, by trying to help municipalities better understand the available internet broadband within their region. Our team joined the MAPC in this endeavor, to collect and analyze broadband data from MLAB and Ookla.

While it may seem trivial, it is actually not so easy to answer questions about internet broadband such as:

- How fast is my internet?
- Is my internet fast enough?
- What providers are available to me, and are there differences in their broadband speeds?

For example, measuring internet speed might amount to a simple measure of the speed of a local ISP server, or be as complex as measuring a real-time observed speed of a fetch request from some geographically distant server. Further, while many ISPs may claim to be able to provide certain speeds, it may not be so clear that the observed speed match the marketed speeds.

Thus, we are working with the MAPC to try and build a dataset that can answer some of these questions, and provide a basis for answering questions that may inform public policy, such as:

- Is there a correlation between median household income and broadband speed?
- Are there municipalities where the available broadband options do not meet requirements for nominal modern internet usage -- say for example, with large zoom calls being nearly ubiquitous for remote schooling and work -- and how limited are they?
- Can we observe differences in broadband access among different providers in different areas of the state?

To answer these questions, we built datasets from Ookla and MLAB of internet speed measurements throughout the 2020 calendar year. We also pulled household income data from the 2014-2018 census. Aside from the aggregation of data, we also provide analyses of the data, which are sufficient starting points for informing policy decisions.

## Ookla Dataset



## MLAB Dataset



## Results



## Conclusion and Discussion

