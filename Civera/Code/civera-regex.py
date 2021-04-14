import re

txt = "Application filed, Magistrate John H. Smith Jr. \n waived, Hon. Robert J. Sawyer II"
txt2 = "Smith Jr., Hon. John H."
test = "( Judge Hon. John Julian )"

judge_pattern = "\( ?[jJ]udge [a-zA-Z \-\.\',]{2,40} ?\)"

word_pattern = "( account| alowed| claimed| country| court| courthouse| Counsel| date| depart| documents| entry| filed| full| given| heard| held| hours| impanelled| interrogatories| judge| justice| list| litigated| matter| merits| NPP| of| officer| OK| order| outcome| papers| paperwork| party| per| plaintiff| pltf| possession| prejudice| present| removed| repairs| reporter| review| reviewed| rights| served| show| stamp| stands| statement| taken| telephone| to| transfer| trial| vacated| waived| website| with| withdrawn)"

word_pattern += ", ?(Hon\.?|A?C-?M|Clerk-? ?Magistrate|Magistrate)"

word_pattern += " ([A-Z.]{1,20} ?[A-Z.]{0,16} [A-Z\'\-]{2,30}(,? Jr.?|,? II|,? III|,? IV)?)"

# print(word_pattern)

# x = re.findall(word_pattern, txt, re.IGNORECASE)
# y = re.findall(word_pattern, txt2, re.IGNORECASE)
# z = re.findall(judge_pattern, test, re.IGNORECASE)

# print(x)
# print(y)

def match(pattern, str):
  matches = re.findall(pattern, str, re.IGNORECASE)
  isMatch = len(matches) > 0
  if isMatch:
    print("Yes, there is at least one match!")
  else:
    print("No match")
  return matches
  

def name_match(pattern, str):
  matches = match(pattern, str)
  isMatch = len(matches) > 0
  if isMatch:
    print(matches)
    for i in range(len(matches)):
      print('parsed judge name: ', matches[i][2])
  else:
    new_pattern = "([A-Z\'\-]{2,30})(,? Jr.?|,? II|,? III|,? IV)?, ?(Hon\.?|A?C-?M|Clerk-? ?Magistrate|Magistrate) ([A-Z.]{1,20} ?[A-Z.]{0,16})"
    names = re.findall(new_pattern, str, re.IGNORECASE)
    print(names)
    if names:
      for name in names:
        cur_name = name[2] + " " + name[3] + " " + name[0] + name[1]
        print('parsed judge name: ', cur_name)


name_match(word_pattern, txt)
name_match(word_pattern, txt2)
match(judge_pattern, test)




# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# if x[0][2]:
#   print('parsed judge name: ', x[0][2])
# else:
#   word_pattern = "[A-Z\'\-]{2,30}(,? Jr.?|,? II|,? III|,? IV)?, ?(Hon\.?|A?C-?M|Clerk-? ?Magistrate|Magistrate) [A-Z.]{1,20} ?[A-Z.]{0,16}"
#   name = re.findall(word_pattern, txt, re.IGNORECASE)
#   if name[0]:
#     print('parsed judge name: ', name[0])


# if y:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")