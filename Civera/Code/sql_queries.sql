--SQL CODE-- 

-- Get Distinct Actions -- 
SELECT distinct (c_a_index.action) 
FROM wp_courtdocs.cdocs_case_action_index as c_a_index 
WHERE c_a_index.action !=  " "

-- Already filled/Trained  -- 
SELECT c_a_index.case_action_id, c_a_index.case_id, c_a_index.actor, c_a_index.action , c_a_index.description
FROM wp_courtdocs.cdocs_case_action_index as c_a_index 
WHERE c_a_index.actor !=  " " and c_a_index.action !=  " "

-- Rows we have to update -- 
SELECT c_a_index.case_action_id, c_a_index.case_id, c_a_index.actor, c_a_index.action , c_a_index.description
FROM wp_courtdocs.cdocs_case_action_index as c_a_index 
WHERE c_a_index.actor =  " " or c_a_index.action =  " "

-- Get Number of Rows Where Action is NULL or Actor is NULL 
SELECT count(cdocs_case_action_index.case_action_id) 
FROM wp_courtdocs.cdocs_case_action_index 
where cdocs_case_action_index.actor = " " or cdocs_case_action_index.action = " " 

-- HOW TO INSERT / EXAMPLE -- 
INSERT INTO wp_courtdocs_NORMALIZED.distinct_case_actions (action, description)
VALUES ('Continuance' , 'continued for payment'),
('Corporate disclosure statement' , 'Corporate disclosure statement filled by'),
('Counterclaim filed' , 'counterclaim filed by')

-- Table to Update later --
INSERT INTO wp_courtdocs_NORMALIZED.cdocs_case_action_index (case_action_id, case_id, actor, action, description, date_time, file_reference_number, last_indexed)


-- ROW NUMBER -- 
SELECT * 
FROM (
    SELECT @curRow := @curRow + 1 AS row_number, wp_courtdocs.cdocs_case_action_index.case_action_id
    FROM wp_courtdocs.cdocs_case_action_index
    JOIN (
        SELECT @curRow := 0
        ) r
	WHERE wp_courtdocs.cdocs_case_action_index.actor = " " or wp_courtdocs.cdocs_case_action_index.action = " " 
    ) sub


-- ROW NUMBER with UNIQUE CASE_ACTION_ID  (Action = NULL or Actor = NULL) --
-- saved data in  table "wp_court_docs_NORMALIZED.case_index_num"  -- 
SELECT row_num, case_action_id 
FROM wp_court_docs_NORMALIZED.case_index_num

-- Total Rows: 38159737 -- 

-- Dividing Work/Chunking -- 
-- example query: let's call this Query1 --
SELECT c_n.row_num, c_i.* 
FROM wp_courtdocs.cdocs_case_action_index as c_i 
INNER JOIN wp_court_docs_NORMALIZED.case_index_num as c_n on c_i.case_action_id = c_n.case_action_id 
WHERE row_num < 50000 


-- Just In case Unsupervised Learning doesn't work -- 
-- Training Set -- 

SELECT c_a_index.actor, c_a_index.action , c_a_index.description, c.description as preprocessed_desc 
FROM wp_courtdocs.cdocs_case_action_index as c_a_index 
INNER JOIN wp_courtdocs_NORMALIZED.distinct_case_actions as c on c_a_index.action = c.action 
WHERE c_a_index.action != " "  and c_a_index.actor != " " and c_a_index.description REGEXP  
          (SELECT GROUP_CONCAT(c.description SEPARATOR '|') 
           FROM wp_courtdocs_NORMALIZED.distinct_case_actions as c) and RAND() LIMIT 50000
 
-- Test Set -- 
SELECT c_a_index.actor, c_a_index.action , c_a_index.description 
FROM wp_courtdocs.cdocs_case_action_index as c_a_index 
WHERE c_a_index.action = " " and c_a_index.description REGEXP  
          (SELECT GROUP_CONCAT(c.description SEPARATOR '|') 
           FROM wp_courtdocs_NORMALIZED.distinct_case_actions as c) LIMIT 100

-- IF We have to USE REGEX / Might be helpful to use this -- 
SELECT c_a_index.action , c_a_index.actor, c_a_index.description
FROM wp_courtdocs.cdocs_case_action_index as c_a_index
where c_a_index.description REGEXP  (SELECT GROUP_CONCAT(description SEPARATOR '|')
FROM wp_courtdocs_NORMALIZED.distinct_case_actions) 


-- EXAMPLE FOR CONNECTING ON PYTHON --
--import mysql.connector--

--mydb = mysql.connector.connect(host='', user='', password='')--

--if (mydb):-
--  print("Connection Successful")--
-- else: -
-- print("Connection Unsuccessful") -- 

-- mycursor = mydb.cursor() -- 

-- query1 = ''' SELECT FROM ''' -- 
-- pd.read_sql_query(query1,mydb)--

-- Dividing Work/Chunking -- 
-- example query: let's call this Query1 --
SELECT c_n.row_num, c_i.* 
FROM wp_courtdocs.cdocs_case_action_index as c_i 
INNER JOIN wp_court_docs_NORMALIZED.case_index_num as c_n on c_i.case_action_id = c_n.case_action_id 
WHERE row_num < 50000 

-- pd.read_sql_query(Query1,mydb)--