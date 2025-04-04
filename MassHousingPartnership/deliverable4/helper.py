import re

from datetime import datetime

#  Output style string - for debug
def compose_string(style_set):
    s = ""
    for style in style_set:
        s += style + " | "
    return style

# Generate popup text for maps
def generate_popup_text(sjoin_df):
    popup_text = []
    for s, ac, uc, ucus in zip(sjoin_df['STYLE'], sjoin_df['ADD_COUNT'], sjoin_df['UNIT_COUNT'], sjoin_df['UNIT_COUNT_USE_CODE']):
        popup_text.append(s + "<br>Address count:" + str(ac) + "<br>Unit count - style: " + str(uc) + "<br>Unit count - use code:" + str(ucus))
    return popup_text

def flter_list(l, pattern="^[019]"):
    res = []
    for e in l:
        if re.search(pattern, e): 
            res.append(True)
            # print(e)
        else: 
            res.append(False)
    return res

def generate_usecode_set(df):
    return set(df["USE_CODE"])

def benchmark(func, args):
    
    
    start_time = datetime.now()
    
    if type(args) is tuple: res = func(*args)
    else : res = func(args)

    run_time = (datetime.now() - start_time).total_seconds()

    print("Run time Cost is : {}ms".format(round(run_time * 1000, 2)))

    return res

def pad_str(s):
    zero_to_pad = 3 - len(s)
    for i in range(zero_to_pad):
        s = "0" + s
    return s

### Count units by style and use code
def generate_residential_usecode_set(usecode_desc_dict):
    res_usecode_set = set()
    for _, v in usecode_desc_dict.items():
        use_code_list = v["USE CODE"]
        for us in use_code_list:
            codes = us.split("-")
            if len(codes) > 1:
                for i in range(int(codes[0]), int(codes[1]) + 1):
                    str_to_append = pad_str(str(i))
                    res_usecode_set.add(str_to_append)
            else:
                res_usecode_set.add(codes[0])
    return res_usecode_set

def filter_out_style_by_keywords(style_set, keywords=["apt"], do_print=False):
    output = set()
    for v in style_set:
        for k in keywords:
            if k in v: 
                output.add(v)
                break
    print(len(output))
    if do_print:
        print(output)
    return output

def delete_from_set(style_set, not_desired_set):
    output = set()
    for v in style_set:
        if v not in not_desired_set: output.add(v)
    print(len(output))
    return output

# Generate residential usecode
def generate_residential_usecode_set():
    res = set()

    mixuse_usecode_set = generate_mixuse_residential_usecode_set()
    res_usecode_set = generate_res_residential_usecode_set()
    tax_exempt_usecode_set = generate_tax_exempt_residential_usecode_set()
    
    for usecode_set in [mixuse_usecode_set, res_usecode_set, tax_exempt_usecode_set]:
        for uc in usecode_set:
            res.add(uc)
    return res

def generate_mixuse_residential_usecode_set():
    res = set()
    for i in range(0, 10):
        res.add(pad_str(str(10 + i)))
        res.add(pad_str(str(i * 10 + 1)))
    return res

def generate_res_residential_usecode_set():
    res = set()
    for i in range(0, 20):
        res.add(pad_str(str(100 + i)))
    return res

def generate_tax_exempt_residential_usecode_set():
    res = set(["945", "959", "970"])
    return res