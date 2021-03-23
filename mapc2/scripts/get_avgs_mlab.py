import pandas as pd 

def run():
	data = pd.read_csv('../data/mlab_2020.csv')
	# print(data.size)
	# print(data.head)
	# print(data.columns)
	#.drop(columns=['TestTime',"IP","Latitude",'Longitude','ProviderNumber','ProviderName'])
	avgs = data.groupby(['City','ProviderName']).mean().drop(columns=['Latitude'  ,'Longitude' ,'ProviderNumber'])
	# print(avgs.head)
	# print(avgs[:5])
	avgs.to_csv('../data/mlab_avg_groupings_2020.csv')
run()