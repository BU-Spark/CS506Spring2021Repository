# Deliverable 2

This document summarizes the work done for Deliverable 2, for the BU Spark! project, Spring 2021, MAPC Broadband Digital Equity in MA.

Date: 03/04/21

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

The primary objective of the previous deliverable was simply to obtain the data; included within deliverable 1 were usable csv files of publicly available broadband data from both Ookla and MLAB for the 2020 calendar year. The purpose of this deliverable is to begin analysis of this 



Some of my thoughts:

- We should try and filter out undesired providers (like Whole Foods and maybe BU? Ask Kamran) - I think MAPC has a list of providers, try to filter so we use only those ones
- It would be helpful to simplify the Providers in the MLAB data: for example, “UUNET - MCI Communications Services, Inc. d/b/a Verizon Business” -> “Verizon”
- When averaging, try to use only provider/city combos that have at least x measurements - that is, filter out single measurements (less than x, not sure what a good value for x is. Maybe 10, 100?) which are likely outliers.
- If we can successfully filter out unwanted providers and providers/city combos with < x measurements (prev bullet), then produce a csv of overall mean broadband speed per city. Sine there are 101 MAPC regions, this file would have 101 data points.
- No point in having two MLAB primary files - merge into one, and remove accidental index (I forgot to set index=False in [df.to](http://df.to/)_csv when I added provider name to the MLAB data)
- Unclear if we should try and “merge” Ookla and MLAB datasets, or if we should simply produce charts (the scatter plot Ryan was talking about) for each of them independently. I’m leaning towards keeping them separate, since they measure different things. Ask Kamran.

- For Ookla, we also have upload speed, so it would definitely make sense to have an independent scatter plot correlating Ookla upload speeds with median income

- Some other random things that I think are easy to produce, and would be nice to have for this deliverable: (kind of similar to what the Professor was doing as the initial exploration of the dataset in the midterm).
  - What are the top 25 max broadband speed in MLAB data? For Ookla, what is max download and upload speed?
  - What are the bottom 25 min broadband speed in MLAB data? For Ookla, what is min download and upload speed?
  - What is the overall average speed in MLAB data (across the entire dataset)? For Ookla, overall average download and upload?
  - Who are the 3 fastest Providers in MLAB data, across the entire dataset?
  - Who are the 3 slowest Providers in MLAB data, across the entire dataset?
  - Count of number of measurements in each city, for both Ookla and MLAB
  - Count of number of measurements of each provider in MLAB data