# %%
import pandas as pd
from tqdm.notebook import tqdm
import datetime
import warnings
from matplotlib import pyplot as plt
import requests
warnings.filterwarnings('ignore')

# %%
def data_range(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    return date_generated


day = data_range('2021-06-01', datetime.datetime.now().strftime('%Y-%m-%d'))
days = [d for d in reversed(day)]

cc = pd.DataFrame()

for elem in tqdm(days):
    try:
        data = datetime.datetime.strftime(elem, '%Y-%m-%d')
        aa = pd.DataFrame(pd.read_html(requests.get('https://euenergy.live/?date=' + data).text)[0]).drop(["Unnamed: 1"], axis=1).rename(columns={"Date:": "Country"}).rename(columns={"€/MWh": elem}).set_index("Country", drop=True)
        aa = aa.groupby('Country').mean()
        
        cc = pd.concat([cc, aa], axis=1, join='outer')
    except Exception as e:
        print(e)
        continue

#cc.dropna(axis=1, inplace=True)

# %%
cc.T[["🇮🇹 Italy", "🇩🇪 Germany","🇫🇷 France"]].describe().plot(kind='bar', figsize=(20, 10)).figure.savefig('plot_bar.png')

# %%
cc.T[["🇮🇹 Italy", "🇩🇪 Germany", "🇫🇷 France"]].plot(figsize=(20, 10)).figure.savefig('plot.png')

# %%
cc.T.describe().loc['mean'][:-1].plot(kind='bar', figsize=(20, 10)).figure.savefig('stats.png')


