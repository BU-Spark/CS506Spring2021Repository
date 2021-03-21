#This can get the input to get pandas dataframe with columns project code, project name, contractor, construction trade
#Needs output from pdf_parser_sa

import pandas as pd


num_projects = len(projects)
list_for_df = []
current_project = 0
i = 0


while i < len(my_data):
    
    if my_data[i][0] == projects[current_project]:
        
        current_project_code = my_data[i][0]
        current_project_name = my_data[i-2][0][len(current_project_code)+1:]
            
        i += 1
            
        current_contractor = 2
        num_contractors = len(new_data[current_project])-2
            
        while i < len(my_data):
                
            if current_contractor-2 != num_contractors-1:
                
#                 print("Current Project Code:",new_data[current_project],"|| Current Project:",current_project)
#                 print()
#                 print("Num Contractors:",num_contractors)
#                 print()
#                 print("Current Contractor:",current_contractor)                
                
                    
                if my_data[i][0] == new_data[current_project][current_contractor]:
                        
                    i += 1
                    
#                     print("Current Project Code:",new_data[current_project],"|| Current Project:",current_project)
#                     print()
#                     print("Num Contractors:",num_contractors)
#                     print()
#                     print("Current Contractor:",current_contractor)
                    
                    while my_data[i][0] != new_data[current_project][current_contractor + 1]:
                        
                        if type(my_data[i][0]) != str:
                        
                            i += 1
                        
                        elif my_data[i][0].isupper() and my_data[i][0] != projects[current_project]:
                                
                            current_construction_trade = my_data[i][0]
                                
                            list_for_df.append([current_project_code,current_project_name,\
                                                new_data[current_project][current_contractor],\
                                                current_construction_trade])
                            i += 1
                        else:
                            i += 1
                        
                    current_contractor += 1
                
                else:
                    i+=1
                                
            elif current_project != num_projects-1:
                    
                if my_data[i][0] == new_data[current_project][current_contractor]:
                        
                    i += 1
                        
                    while my_data[i][0] != projects[current_project+1]:
                            
                        if type(my_data[i][0]) != str:
                            
                            i += 1
                        
                        elif my_data[i][0].isupper() and my_data[i][0] != projects[current_project]:
                                
                            current_construction_trade = my_data[i][0]
                                
                            list_for_df.append([current_project_code,current_project_name,\
                                                new_data[current_project][current_contractor],\
                                                current_construction_trade])
                            i += 1
                        else:
                            i += 1
                    break
                    
                else:
                    i += 1
                       
            else:
                    
                if my_data[i][0] == new_data[current_project][current_contractor]:
                        
                    i += 1
                        
                    while i < len(my_data):
                            
                        if type(my_data[i][0]) != str:
                            
                            i += 1
                        
                        elif my_data[i][0].isupper() and my_data[i][0] != projects[current_project]:
                                
                            current_construction_trade = my_data[i][0]
                                
                            list_for_df.append([projects[current_project],new_data[current_project][0],\
                                                new_data[current_project][current_contractor],\
                                                current_construction_trade])
                            i += 1
                        else:
                            i+=1
                    break
                else:
                    i+=1
                    
        current_project +=1

    else:
        i += 1  
                    
                
                    

            
                
list_for_df



df = pd.DataFrame(list_for_df, columns = [ 'Project_Code', 'Project_Name', 'Contractor_Name', 'Construction_Trade' ]) 