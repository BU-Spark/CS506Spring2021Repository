## Use Code
- 0 - Mix use
- 1 - Residential
- 2 - Open space
- 3 - Commercial
- 4 - Industrial
- 5 - Personal porperty
- 6 - Forest Land
- 7 - Agricultural
- 8 - Recreation
- 9 - Tax exempt

## 1. Mix use buildings - USE CODE starts with 0
### Mix Use Code
- 0 - stands for Mix use class
- Second digit - Primarily use
- Third digit - Partially use
- Example [USE CODE: 013] - Mix use, primarily residential, partially commercial

Claim 1. All mix used buildings have only one record in parcel dataset. Verified by function: check_mix_usecode
- How to count? Use Code matching is not accurate:
- - 0113 - Apt 9 units and up, 0111 - apt 4 units
- - 0104 - Two family, 0105 - Three fam
- Thoughts
- - Using style to classify first
- - Record[LOC_ID = "F_791080_2916264"], the style of it is apartments. We should use address count.
- - - Problem: Although the style of it is apartments. It can also contain commercial addresses. (If the number of residential addresses is much greater than the number of commercial addresses, the bias should be small)
- - Record[LOC_ID = "F_797389_2920601"], the style of it is 2 Fam Conver. We should use style to count
- May not be accurate. Need to pay more attention.
- - Colonial, Conventional, Cape cod - how many units?
- - Thoughts: Mark these as anomalies. Use data analysis later.
- Summary:
- - Two way to process mix use buildings.
- - - Using use code description:
- - - - Drawback: Time consuming. Hard to process.
- - - - Potential risk: One use code may have different use descriptions. They might have different ideas.
- - - Using style:
- - - - Process: Classify style as address_confidence (use address count directly: apt), style_confidence (use style to count: 2 fam, 3 fam), parcel_confidence (use parcel count: condo), and unclear(Colonial, Cape Cod, Conventional)
- - - - How to process "unclear" style: 1. data analysis.

## 2. Residential buildings - USE CODE starts with 1
UKN - don't understand

> ### 101 - Single Family
- - Special cases:
- - - 1017 - single Family with in-law (UKN)
- - - 101V - Single Family - Vacant (Count or not?)
> ### 102 - Residential Condominum
- - Special cases:
- - - 102A - Condo - Affordable
- - - 102V - Condo - Vacant
> ### 103 - Mobile Home
> ### 104 - Two-Family Residential
> ### 105 - Three-Family Residential
> ### 106, 107, 108 - Land (SKIP)
> ### 109 - Multiple Houses on one parcel
- Special cases:
- - 1094 Multiple houses on one parcel - Two family
- - 1095 Multiple houses on one parcel - Three family
- - 1098 Multiple houses on one parcel - 4 - 8 Appartments
- Should use address count here.

> ### 110 - Trailer Park (UNK)
> ### Apartments
- - 111 - Apartments with Four to Eight Units
- - 112 - Apartments with More than Eight Units
- - 113 - Apartment with over 100 units
- - 114 - Affordable Housing Units (UNK)
- - 111, 112, 113, (maybe 114) should use addresses count

> ### 116 - 119, 126 - 129, 152, 160, 170 Imputed residential - classify as "unclear"
> ### 121 - Rooming and Boarding Houses (UNK)
> ### 122 - Fraternity and Sorority Houses (Count or not?)
> ### 123 - Residence Halls or Dromitories - Use addresses
> ### 167, 178 - Mixed use residential - Why mix use here?
> ### 180 - 181 predom res (UNK)

### How to process residential parcels
- Classify use code as "Address_confidence (use address directly: 111, 112)", "parcel_confidence (use parcel count: 102)", "style_confidence (use style to count: all mix use buildings)", "Normal", "unclear"
- For address confidence usecode, address count = approximation.
- For normal usecode, perform data analysis.
- For unclear data, filter out and observe first. How to process: Not sure yet.

## 3. Tax exempt buildings - USE CODE starts with 9 
> ### 959 - Housing
> ### 970 - Housing Authority
> ### 996 - Other, Non-Taxable Condominium Common Land

- It's unclear how to count units using use code only.
- However, I checked the dataset. There are styles attached to these buildings.
- For exmaple
- - Record[LOC_ID = F_792862_2914578], the style of it is apartments.
- - Record[LOC_ID = F_794684_2916023], the style of it is two fam flat.
- Maybe we should use style here too.


