# Kickoff Meeting

First time meeting with the client, as well as the PM.

Date: 02/19/21

Started with student introductions.

Some context: they work at MAPC metropolitan area planning council, strange form of gov, state employees, work for independent state agencies, board working on municipal efforst - try to provide capacity on planning projects for municipalities. Matt and Ryan are on the software/data side. Most of their job are like trailmap, or mass bill, provide capacity to municipalities where they don't have it. 

Broadband work is new. MAPC has lots of different groups, haven't really had group work on infrastructure, especially with broadband. Municipalities want to better understand their role in broadband - Everett chelsea and revere, eventually going to Boston. Over last few months, trying to understand what data is available, what needs to be collected, what leverage municipalities have to affect broadband investment. 

Lots of different data sets, in different states of cleanless. Not yet ready to be explored from a policy perspective.

Matt: MLAB - data source - lead web developer at MAPC, self taught web dev :) 

Measurement lab - non profit, collaborate with google, in the open science foundation. Developed a speed test tool, when type what is my internet speed on google. They do this to near real-world condition, which is different than speediest.net from ookla. This says how fast internet actually is. Have millions of rows of data, with geospatial information, also over dates and times and IP addresses. He's been diving in using python and pandas, but ultimately want to see what kind of things can be learned from this data. How can we use this data in relation to other things we can find? 

Digital redlining - who's getting better/worse service based on socio-economic factors. May not have time to really look at the geography.

Broadband primer: complicated world, there are 12 or so municipalities that have municipal run on broadband - that is, they run it, not comcast/verizon, etc. Broadband is the coverage in that market that is comcast, rcn, century link - what happens to your data after it leaves your router?

Municipalities have ability to permit building - 5g towers, cable placements. Want to understand impact on user. Eastern MA is highly connected and dense and competitive space. Not necessarily true in western MA. Probably more focused in Eastern MA - are we really fast enough? Trying to tease out how that is different - what is considered good?

FCC: federal communications commission - good is defined as 25 MB/s download, and 3MB/s upload. Goal is to get to at least 100 MB/s. Some want a gig - how do we incentivize competition, how do we get there?

Data sets: making data sets available - MLAB - not a dataset that can be just downloaded into a csv file, very large data set. Initial thing that would be helpful - want a smaller state file available of this data. That initial work will provide dividends. This isn't necessarily a high bar, but very important - basically, want a csv that they can then use for various apis. 

Ookla is also interesting.

Other sets of data - the FCC produces data, mostly from form77, where they ask the ISP to fill out information every quarter. See if we can join that with speed data.

4th is the census data - census.gov, and some apis available. Data ferret, or fact finder.

Lot's of other things that would be interesting in terms of data sets for exploration. Looking to our ideas for what would be interesting. Work will continue pass this class. Breaking down large datasets into smaller sets, and then ask some questions about it. run some descriptive statistics. 

Want to answer two sets of questions: replicating tow studies elsewhere - digital redlining, 

- how is speed distributed?
- does data back up conventional notion of how we think it's distributed?

FCC state of the state broadband report - charts at a national scale - kinda want to see this at the state level, not just the national level.

Our opportunities here are that willing to help by drawing from this, especially on digital equity inclusion. 

Their first class project - how to work on this? Pretty head down into local reports, want to have a structured way of doing this. What is our perspective on the data itself? Might be different than an analyst.

Kamran question: since there are two teams, how can we divide project into parts? Answer: open to ideas, think there's a lot of us here - maybe just breaking it up into different data sets, one group works on FCC and ookla, the other MLAB, etc. How has MLAB changed from year to year? 

MLAB: google big query to get that data, and then storing it in postgres tables to make csvs. Ookla data is available on amazon warehouse storage - moving it and pulling out MA. FCC is just a download of a zip file, many methods for download.

Succesful outcome - want statewide charts, based on speed, inclusion, and coverage. They had done one for thier area on median speed - want that statewide, weighted by FCC data. Replicate the map in cincinnati and Dallas - maps national digital inclusion alliance. NDIA report. 

Not only avialability, but also affordability.

Question: entire state vs specific area: there may be benefits to smaller geography, to queries can run faster. In everett, chelsea, and revere, doesn't have to be any specific areas, some digital redlining areas

They have an MAPC aws account, could possibly run some stuff on the cloud.

Not fully clear how to split up the work.

We'll be meeting bi-weekly at this same time with both teams.

Question: any existing repos, documents, that can be sent over? Answer: some links in initial pitch, but they have a hub - datacommon. It's their open repos, they load data sets there after processing. They haven't uploaded some of their processed broadband data. Also use airtable a lot - it's basically a web spreadsheet of reference spreadsheets, terms and definitions, and Matt has structured pulled data. They also use github - he'll put those things in a github readme.

One team: ookla and mlab, other team NDIA and FCC.

First step: what can be said about the data sets? How big are they? Are there data sets that are missed? Start by exploring the data sets, understanding it, and describing them.

FCC data - two different sets of form 77: one is fixed, one is wireless. Not clear how 5g is categorized in that. Homeland security has an open repo of towers that are fixed assets. Where are the 5g cell towers? Can't really build a map of that - they're not asking of it.

Scrape verizon site for 5g coverage.

Links:

https://datacommon.mapc.org/

https://www.verizon.com/coverage-map/

https://airtable.com/shrv7Uv7LMWkKDW1b

https://airtable.com/shrZkjM3DUASjEVmk

https://airtable.com/shrML6GmsFUwwRQpo

https://datacommon.mapc.org/calendar/2020/december

https://datacommon.mapc.org/calendar/2020/april

https://www.measurementlab.net/data/

https://www.speedtest.net/insights/blog/announcing-ookla-open-datasets/
https://www.fcc.gov/document/fcc-annual-broadband-report-shows-digital-divide-rapidly-closing

