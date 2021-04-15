import re

txt = "The judge stands on the side of justice in this matter and trial"

regex = "account|alowed|claimed|country|court|courthouse|Counsel|date|depart|documents|entry|filed|full|given|heard|held|hours|impanelled|interrogatories|judge|justice|list|litigated|matter|merits|NPP|of|officer|OK|order|outcome|papers|paperwork|party|per|plaintiff|pltf|possession|prejudice|present|removed|repairs|reporter|review|reviewed|rights|served|show|stamp|stands|statement|taken|telephone|to|transfer|trial|vacated|waived|website|with|withdrawn"

x = re.findall(regex, txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")