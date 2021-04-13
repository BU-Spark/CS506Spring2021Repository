import pandas as pd

df = pd.read_csv("data/Blake_RPD_Dataset-1_Twins-03-19-21.csv")

totals_coop = []
totals_defect = []
coops_before_defect = []
coops_after_first_defect = []

for i in range(len(df)):
    df_row = df.iloc[i]
    coop_count = 0
    defect_count = 0
    coop_before_defect_count = 0
    coop_after_defect_count = 0
    defected = False
    for j in range(22,df.shape[1],2):
        if df_row[j][0] == 'C':
            coop_count += 1
            if defected:
                coop_after_defect_count += 1
            else:  
                coop_before_defect_count += 1
        else:
            defect_count += 1
            defected = True
    totals_coop.append(coop_count)
    totals_defect.append(defect_count)
    coops_before_defect.append(coop_before_defect_count)
    coops_after_first_defect.append(coop_after_defect_count)

df['total_cooperations'] = totals_coop
df['total_defections']  = totals_defect
df['Number of cooperations before first defection'] = coops_before_defect
df['Number of cooperations after first defection'] = coops_after_first_defect

print(df)

df.to_csv('data/dataset_with_totals.csv',index = False)