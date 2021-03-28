import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='', user='', password='')

if (mydb):
    print("Connection Successful")

else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)

# cdocs_party_assignment_index 
party_assignment_table = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_party_assignment_index WHERE CASE_ID != ' ' LIMIT 0,1000;", con = mydb)
print(party_assignment_table)

# cdocs_case_action_index / action = null 
action_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action = ' ' and c_a_index.actor != ' ' LIMIT 0, 1000;", con = mydb)
print(action_null)

# cdocs_case_action_index / actor = null
actor_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action != ' ' and c_a_index.actor = ' ' LIMIT 0, 1000;", con = mydb)
print(actor_null)

# cdocs_case_action_index / actor != null and action != null 
case_index_not_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action != ' ' and c_a_index.actor != ' ' LIMIT 0, 1000;", con = mydb)
print(case_index_not_null)

# cdocs_case_action_index / action = null and actor = null 
case_index_null = pd.read_sql("SELECT * FROM wp_courtdocs.cdocs_case_action_index as c_a_index WHERE c_a_index.action = ' ' and c_a_index.actor = ' ' LIMIT 0, 1000;", con = mydb)
print(case_index_null)

