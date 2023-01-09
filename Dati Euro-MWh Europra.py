# %%
import pandas as pd
from tqdm.notebook import tqdm
import datetime
import warnings
from matplotlib import pyplot as plt
warnings.filterwarnings('ignore')

# %%
def data_range(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
    return date_generated

days = data_range('2022-01-01', '2023-01-01')


# %%
cc = pd.DataFrame()

for elem in tqdm(days):
    data = datetime.datetime.strftime(elem, '%Y-%m-%d')
    aa = aa = pd.DataFrame(pd.read_html('https://euenergy.live/?date=' + data)[0]).drop(["Unnamed: 1"], axis=1).rename(columns={"Unnamed: 0": "Country"}).rename(columns={"€/MWh": elem}).set_index("Country", drop=True)
    cc = pd.concat([cc, aa], axis=1)

# %%
cc.T[["🇮🇹 Italy", "🇩🇪 Germany","🇫🇷 France"]].describe().plot(kind='bar', figsize=(20, 10)).figure.savefig('plot_bar.png')

# %%
cc.T[["🇮🇹 Italy", "🇩🇪 Germany", "🇫🇷 France"]].plot(figsize=(20, 10)).figure.savefig('plot.png')

# %%
cc.T.describe().loc['mean'].plot(kind='bar', figsize=(20, 10)).figure.savefig('stats.png')

# %%



