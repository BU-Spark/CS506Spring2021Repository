"""last modified: 04/18/202115-minute area finding code"""#%% packagesimport pandas as pdimport geopandas as gpdimport numpy as npimport networkx as nximport osimport foliumfrom shapely.geometry import Pointfrom shapely.ops import nearest_pointsraise Exception("don't run this file unless you have 5 hours")#%% importing data# path to dataamenities_path = '../datasets_clean/merged.csv'parcels_path = '../datasets_clean/parcels_latlon.csv'# note: amenities has lat, lon, category# note: parcels has lat, lon, zip# pulling data from csv fileif os.path.exists(amenities_path):    print('acquiring data (amenities))...')    amenities = pd.read_csv(amenities_path, usecols = [3,4,5])    # rejects if path has been changedelse:    raise FileNotFoundError('invalid path to merge')    # pulling data from csv file (parcels)if os.path.exists(parcels_path):    print('acquiring data (parcels)...')    parcels = pd.read_csv(parcels_path, usecols = [2,3,4])# rejects if path has been changedelse:    raise FileNotFoundError('invalid path to parcels')    # pulling data from online (streets)print('acquiring data (streets))...')raw_streets = gpd.read_file('http://bostonopendata-boston.opendata' \                            '.arcgis.com/datasets/cfd1740c2e4b4938' \                            '9f47a9ce2dd236cc_8.zip?outSR=%7B%22la' \                            'testWkid%22%3A2249%2C%22wkid%22%3A102686%7D')streets = raw_streets.to_crs(epsg = 4326                             )[['OBJECTID', 'ST_NAME', 'ST_TYPE', 'geometry']]streets.columns = ['id', 'name', 'type', 'geometry']        #%% reducing redundant amenities, separating into categoriesprint('snapping amenities to streets...')do_commercial = 0if do_commercial == 1:    num_am = 6else:    num_am = 5# amenities closer than 0.00001 are essentially atop each otherreduced = amenities.round({'lat':5, 'lon':5})# separationcommercial = reduced[reduced['category'] == 'commercial']education = reduced[reduced['category'] == 'education']food = reduced[reduced['category'] == 'food']health = reduced[reduced['category'] == 'health']recreation = reduced[reduced['category'] == 'recreation']social = reduced[reduced['category'] == 'social']categories = [commercial, education, food, health, recreation, social]# removing equivalent data points    commercial = commercial[~commercial.duplicated(subset = ['lat', 'lon'])]education = education[~education.duplicated(subset = ['lat', 'lon'])]food = food[~food.duplicated(subset = ['lat', 'lon'])]health = health[~health.duplicated(subset = ['lat', 'lon'])]recreation = recreation[~recreation.duplicated(subset = ['lat', 'lon'])]social = social[~social.duplicated(subset = ['lat', 'lon'])]# reset indexcommercial = commercial.reset_index()education = education.reset_index()food = food.reset_index()health = health.reset_index()recreation = recreation.reset_index()social = social.reset_index()amenity_list = [education, food, health, recreation, social, commercial]name_list = ['education', 'food', 'health', 'recreation', 'social', 'commercial']# find closest street and point to each amenityfor j in range(num_am):    print('finding closeness for:', name_list[j])    latitudes = amenity_list[j].lat.tolist()    longitudes = amenity_list[j].lon.tolist()    lines = streets.geometry.tolist()        points = [Point(longitudes[x], latitudes[x]) for x in range(len(latitudes))]    nearest = []    near_id = []        for k in range(len(points)):        distance = 10        for i in range(streets.shape[0]):            if points[k].distance(lines[i]) < distance:                distance = points[k].distance(lines[i])                close_line = i        nearest.append(nearest_points(points[k], lines[close_line])[1])        near_id.append(close_line + 1)                if k%1000 == 0:            print(k//1000, end = '.')            amenity_list[j]['nearest'] = nearest    amenity_list[j]['near_street'] = near_id    print()#%% also snapping parcels# find closest street and point to each parcellatitudes = parcels.lat.tolist()longitudes = parcels.lon.tolist()lines = streets.geometry.tolist()points = [Point(longitudes[x], latitudes[x]) for x in range(len(latitudes))]nearest = []near_id = []for k in range(len(points)):    distance = 10    for i in range(streets.shape[0]):        if points[k].distance(lines[i]) < distance:            distance = points[k].distance(lines[i])            close_line = i    nearest.append(nearest_points(points[k], lines[close_line])[1])    near_id.append(close_line + 1)        if k%1000 == 0:        print(k//1000, end = '.')    parcels['nearest'] = nearestparcels['near_street'] = near_id# save with different nameparcels_nearest = parcels.copy(deep = True) #%% base mapprint('generating map of amenities...')base_path = 'maps/base_map.html'# function to generate base mapdef generate_base(default_location = [42.3150,-71.0700]):    base_map = folium.Map(location = default_location,                          zoom_start = 12,                          tiles = 'CartoDB positron')    return base_map# generating map with amenitiesbase = generate_base()# amenities and colorsamenity_list = [commercial, education, food, health, recreation, social]color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred']# iterating over each amenityfor i in range(6):        # latitudes and longitudes as lists    latitudes = list(amenity_list[i].lat)    longitudes = list(amenity_list[i].lon)        color = color_list[i]        for lat, lon in zip(latitudes, longitudes):        folium.Circle(            location = [lat,lon],            radius = 10,            color = color,            fill = True,            weight = 1.5            ).add_to(base)    print('saving base map...')base.save(base_path)#%% fixing streets with start/endprint('transforming streets to network...')# start and end pointsstreets['a'] = [Point(np.array(x)[0]) for x in streets.geometry.tolist()]streets['b'] = [Point(np.array(x)[-1]) for x in streets.geometry.tolist()]# weights for netx graphstreets['length'] = [x.length for x in streets.geometry.tolist()]streets['id_name'] = [str(x) for x in streets.id.tolist()]streets['node1'] = [str(np.array(x).round(6).tolist()) for \                    x in streets.a.tolist()]streets['node2'] = [str(np.array(x).round(6).tolist()) for \                    x in streets.b.tolist()]# netxnx_inters = nx.from_pandas_edgelist(streets, 'node1', 'node2',                                    edge_attr = ['length', 'id_name'])nx_streets = nx_inters.to_undirected()# finding ego maps for nodesall_nodes = list(set(streets.node1.tolist() + streets.node2.tolist()))egos = {}print('creating ego maps...')for i in range(len(all_nodes)):    close_graph = nx.ego_graph(nx_streets,                               all_nodes[i],                               radius = 0.007,                               distance = 'length')    egos[all_nodes[i]] = close_graph    if i%1000 == 0:        print(i//1000, end='.')#%% using crawl algorithm to find close-by parcelsprint('finding close-by parcels...')do_commercial = 0if do_commercial == 1:    num_am = 6else:    num_am = 5# amenities and names; columns to useamenity_list = [education, food, health, recreation, social, commercial]name_list = ['education', 'food', 'health', 'recreation', 'social', 'commercial']cols = ['lat','lon']served = list(range(num_am))underserved = list(range(num_am))# function for closest parcelsdef close_parcels(node, parcels, egos, streets, over = 0.01, limit = 0.007):    '''    takes:        node, a street/edge to compare to        parcels, parcels to detect closeness        egos, egos graphs in dictionary        streets, streets        over, distance to search large range        limit, distance to search for small range            returns: list of close parcel ids    '''        graph = egos[node]    close_list = list(graph.edges)    close_locations = []        for x in close_list:        name = int(graph[x[0]][x[1]]['id_name'])        close_locations.append(name)            close_parcels = parcels[parcels.near_street.isin(close_locations)]        return close_parcels.index.tolist()# iterate over amenitiesfor i in range(num_am):        print('finding closeness for:', name_list[i])        # for each amenity, find parcels within distance    near_parcels = []    for street_id in amenity_list[i].near_street.to_list():        first_node = streets.node1[street_id - 1]        second_node = streets.node2[street_id - 1]        nearby_parcels1 = close_parcels(first_node, parcels, egos, streets)        nearby_parcels2 = close_parcels(second_node, parcels, egos, streets)        near_parcels += nearby_parcels1        near_parcels += nearby_parcels2            near_parcels = list(set(near_parcels))            underserved[i] = parcels.loc[~parcels.index.isin(near_parcels)]    served[i] = parcels.loc[near_parcels]        parcels[[name_list[i]]] = parcels.index.isin(near_parcels)        served_map = generate_base()            for lat, lon in zip(underserved[i].lat.tolist(), underserved[i].lon.tolist()):        folium.Circle(            location = [lat,lon],            radius = 50,            color = 'red',            fill = True,            weight = 0,            fill_opacity = 0.7            ).add_to(served_map)            for lat, lon in zip(served[i].lat.tolist(), served[i].lon.tolist()):        folium.Circle(            location = [lat,lon],            radius = 50,            color = 'blue',            fill = True,            weight = 0,            fill_opacity = 0.7            ).add_to(served_map)            filename = 'maps/d4/' + name_list[i] + '_map.html'        print('saving map for:', name_list[i])    served_map.save(filename)#%% overall mapprint('creating overall map...')# note: disincludes commercial since all are presentall_served = parcels.education & parcels.food & parcels.health & \    parcels.recreation & parcels.social    over_underserved = parcels[~all_served]over_served = parcels[all_served]for lat, lon in zip(over_underserved.lat.tolist(), over_underserved.lon.tolist()):    folium.Circle(        location = [lat,lon],        radius = 50,        color = 'red',        fill = True,        weight = 0,        fill_opacity = 0.7        ).add_to(served_map)    for lat, lon in zip(over_served.lat.tolist(), over_served.lon.tolist()):    folium.Circle(        location = [lat,lon],        radius = 50,        color = 'blue',        fill = True,        weight = 0,        fill_opacity = 0.7        ).add_to(served_map)    filename = 'maps/d4/overall_map.html'print('saving overall map...')served_map.save(filename)#%%underserved.append(parcels[~parcels.index.isin(parcels.index)])served.append(parcels.loc[parcels.index])parcels[[name_list[5]]] = parcels.index.isin(parcels.index)served_map = generate_base()    for lat, lon in zip(underserved[5].lat.tolist(), underserved[5].lon.tolist()):    folium.Circle(        location = [lat,lon],        radius = 50,        color = 'red',        fill = True,        weight = 0,        fill_opacity = 0.7        ).add_to(served_map)    for lat, lon in zip(served[5].lat.tolist(), served[5].lon.tolist()):    folium.Circle(        location = [lat,lon],        radius = 50,        color = 'blue',        fill = True,        weight = 0,        fill_opacity = 0.7        ).add_to(served_map)    filename = 'maps/d4/' + name_list[5] + '_map.html'print('saving map for:', name_list[5])served_map.save(filename)#%% outputprint('outputting data...')output_path = '../datasets_clean/results_crawl.csv'parcels.to_csv(output_path)print('done.')