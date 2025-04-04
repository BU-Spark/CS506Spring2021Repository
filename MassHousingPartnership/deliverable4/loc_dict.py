# USE for now. Update to json file later.

style_dict = {
    "2 Fam Conver": 2,
    "2 Fam Flat": 2,
    "3 Fam Conv": 3,
    "3 Fam Flat": 3,
    "4 Fam": 4,
    "Apartments": 1,
    "Bungalow": 1,
    "Boarding House": 1,
    "Colonial": 1,
    "Condo GR": 1,
    "Condo TH": 1,
    "Conventional": 1,
    "Dormitory": 1,
    "Family Duplex": 2,
    "Gambrel": 1,
    "High Rise Apt": 1,
    "Indust Condo": 1,
    "Industrial": 1,
    "Raised Ranch": 1,
    "Retail Condo": 1,
    "Split Level": 1,
    "Cape Cod": 1
}

usecode_dict = {
    "0101": 1,
    "0102": 1,
    "0104": 2,
    "0105": 3,
    "010E": 2,
    "010G": 3,
    "010H": 2,
    "010I": 1,
    "010M": 1,
    "101": 1,
    "102": 1,
    "104": 2,
    "105": 3
}

parcel_confidence = {"0102", "102"}
countable_usecode = {"0101", "0102", "0104", "0105", "010E", "010G", "010H", "010I", "010M", "101", "102", "104", "105"}

usecode_desc = {
    "Address confidence": {
        "_comments": [
            "031 is a really weird one, it should represent mainly commercial. However, it includes apartments and High rise apt"
        ],
        "USE CODE": ["109", "111", "112", "113", "114"]
    },
    "Parcel confidence": {
        "USE CODE": ["102"]
    },
    "Style confidence": {
        "_comments": [
            "Mainly for mix used buildings",
            "Use dictionary, faster. Regular expression is more time consuming."
        ],
        "USE CODE" : ["010-019", "021", "031", "041", "051", "061", "071", "081", "091", "167", "178", "959", "970", "996"]
    },
    "Normal": {
        "USE CODE": ["101", "103", "104", "105"]
    },
    "Special cases": {
        "USE CODE": ["101V", "102V"]
    },
    "Unclear": {
        "_comments": [
            "It seems to be ok since there aren't may data with these use codes"
        ],
        "USE CODE": ["110", "116-119", "126-129", "152", "160", "170", "180-181"]
    }
}