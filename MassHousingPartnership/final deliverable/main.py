import geopandas as gpd
from geofeather import from_geofeather
from geofeather import to_geofeather

from datetime import datetime

from sklearn.linear_model import LinearRegression

from .helper import *
from .draw_maps import *
from .main_logic import *
from .debug import *
from .loc_dict import *

# TODO: Need to debug. Simple copy paste for now.
def main():
    # Read data
    print("\nStart reading data......\n")
    start_time = datetime.now()

    parcel_whole = from_geofeather("data/ParcelData/statewide_parcel_data.feather")
    address_whole = from_geofeather("data/AddressData/statewide_address_data.feather")
    state_use_code = gpd.read_file("data/state_use_codes_lookup_table/")

    end_time = datetime.now()
    print("Time cost: %.2fms" %((end_time - start_time).total_seconds() * 1000))

    # Clean addresses data
    print("\nClean addresses data......\n")
    address_whole_afterdrop = benchmark(clean_addresses, (address_whole))

    # Filter out residential parcels
    print("\nClean parcels data......\n")
    residential_usecode = generate_residential_usecode_set()
    parcel_whole_residential = benchmark(filter_out_residential_parcels, (parcel_whole, residential_usecode))

    # Count by usecode
    print("\nCount by usecodes......\n")
    parcel_whole_count = benchmark(count_parcels, (parcel_whole_residential, usecode_dict))
    parcel_whole_aftercount = benchmark(generate_gpd_dataframe, (parcel_whole_count, ["LOC_ID", "CITY", "STYLE_DESC", "COUNT_USECODE", "USE_CODE", "AREA_SQFEET"]))

    # Perform sjoin
    print("\nPerform sjoin......\n")
    address_whole_loc = gpd.GeoDataFrame(address_whole_afterdrop['geometry'])
    sjoin_whole = benchmark(join_two_dataset, (address_whole_loc, parcel_whole_aftercount))

    # TODO: maybe there is a better way - we should be able to merge the following two steps
    # Make assumption and mark anomalies
    print("\nMake assumptions......\n")
    assumption_whole, anomalies_whole = benchmark(do_assumption, (sjoin_whole, parcel_confidence, countable_usecode))
    sjoin_whole['ASSUMPTION'] = assumption_whole
    sjoin_whole['IS_ANOMALY'] =  sjoin_whole['ASSUMPTION'] == -1
    print("Anomalies rate: {}%".format(round(len(anomalies_whole) * 100 / len(assumption_whole), 2)))

    # Create assumptions for anomalies
    anomalies_list = list(zip(*anomalies_whole))
    reg = LinearRegression().fit([[x] for x in anomalies_list[0]], [[y] for y in anomalies_list[1]])
    update_anomaly(sjoin_whole, anomalies_whole, reg)

    # Calculate density
    sjoin_whole['DENSITY_SQFEET'] = sjoin_whole['AREA_SQFEET'] / sjoin_whole['ASSUMPTION']
    sjoin_whole['DENSITY_SQMETER'] = sjoin_whole['DENSITY_SQFEET'] * 0.092903
    sjoin_whole['DENSITY_ACRE'] = sjoin_whole['DENSITY_SQFEET'] / 43560


    # Save final data
    print("\nSave final data......\n")
    to_geofeather(sjoin_whole, "./data/state_data/sjoin_whole.feather")

    # Draw debug map
    print("\nDraw debug map......\n")
    benchmark(draw_validation_map, (sjoin_whole, "BOSTON", "./maps/whole_state_"))


if __name__ == "__main__":
    main()