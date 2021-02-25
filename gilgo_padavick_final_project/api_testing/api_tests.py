import json
# Import keys (kept locally)
with open('keys.json') as config_file:
    config = json.load(config_file)
# Alpha Vantage 
api_key = config['alpha_vantage']

# Test code
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

starting_stocks = ['XSPA', 'GNUS', 'IBIO', 'GME']
ts = TimeSeries(key=api_key, output_format='pandas')

def plot_intraday(symbol):
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='full')
    data['4. close'].plot()
    plt.title('Intraday Times Series for the {} stock (1 min)'.format(symbol))
    plt.show()

for stock in starting_stocks:
    plot_intraday(stock)

