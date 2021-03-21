#parser_sa
#Right now, just able to extract project name, project code, and contractors per project

#Call Jena's code to read csv
my_data = read_csv('hello','hello')

new_data = []
projects = []

ignore_list1 = [['', '', '', '', '', '', '', '', '', '', '', '', ''], 'Total for Contractor',['Project Name:'],\
          'Journey',['Journey'], 'Journey', ['Total for Contractor'] ]
ignore_list2 = ['Journey','Total for Contractor','Project Name:','Total  Journey Hours',\
               'Apprentice','Total Journey Hours']

i = 0

while i < len(my_data):
    
    new_entry = []
    
    if i == len(my_data):
        break
        
    elif my_data[i][0] == 'Project Name:':
        
        if my_data[i+3][0] not in projects:
            
            projects.append(my_data[i+3][0])

            current_project_code = my_data[i+3][0]

            new_entry = [my_data[i+1][0][len(current_project_code)+1:], current_project_code]
            
            i += 4
            
            while i < len(my_data):
                
                if my_data[i][0] == 'Male' and my_data[i+1] not in ignore_list1 and my_data[i+1][0] not in ignore_list2:
                    if not my_data[i+1][0].isupper():
                        new_entry.append(my_data[i+1][0])                    

                        
                elif my_data[i][0] == 'Subtotal' and my_data[i+1][0] not in ignore_list2: 
                    if not my_data[i+1][0].isupper() and not my_data[i+1][0][0].isnumeric():
                        new_entry.append(my_data[i+1][0])
                    
                elif my_data[i] == ['', '', '', '', '', '', '', '', '', '', '', '', ''\
                                   ] and my_data[i+1] not in ignore_list1 and my_data[i+1][0] not in ignore_list2:
                    if not my_data[i+1][0].isupper():
                        new_entry.append(my_data[i+1][0])
                    
                elif my_data[i][0] == 'Project Name:':
                    if my_data[i+3][0] not in projects:
                        i -= 2
                        break
                
                elif len(my_data[i]) > 1:
                    if my_data[i][1] == 'Subtotal' and my_data[i+1][0] not in ignore_list2:
                        if not my_data[i+1][0].isupper():
                            new_entry.append(my_data[i+1][0])
                        
                    
                i += 1
                
            new_data.append(new_entry)
    
    i += 1    
               
         
        
        
new_data