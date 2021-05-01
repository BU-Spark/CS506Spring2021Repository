import pandas as pd
header = [
     'DATE OPENED',
     'DATE CLOSED',
     'COURT NAME',
     'COUNTY',
     'COUNTY NAME',
     'YEAR',
     'OFFICE_ID',
     'NAME',
     'charge_grid_level',
]


# -----------multiprocessing
def f(row):
    return sum(row)+a
 
def apply_f(func, part_case_ids, data, group):
    tmp_data = pd.DataFrame(columns=data.columns)
    for case_id in part_case_ids[:]:
        case_charges = group.get_group(case_id)['charge_grid_level']
#         case_charges = group.get_group(case_id)[header].fillna(method='ffill')['charge_grid_level']
        row = func(data, case_charges)
        tmp_data = tmp_data.append(row, ignore_index=True)
        
    return tmp_data
 
    
def init_process(global_vars):
    if global_vars:
        global data, group
        data = global_vars[0]
        group = global_vars[1]
# -----------multiprocessing


def merge_cases(data, case_charges):
    charge = -1
    max_charge = -1
    index = -1
    for i in case_charges.index:
        charge_grid_level = case_charges[i]
        if type(charge_grid_level) == int:
            charge = charge_grid_level

        # like '2,3,4'
        elif type(charge_grid_level) == str and len(charge_grid_level) > 2:
            charge = max(int(x) for x in charge_grid_level.split(','))

        if max_charge < charge:
            max_charge = charge
            index = i

    if index > -1:
        row = data.loc[index].copy()
        row.loc['charge_grid_level'] = max_charge
        return row
    
    else:
        return None