# %%
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

sns.set_theme()

# %%
matplotlib.rcParams["axes.labelsize"] = 14
matplotlib.rcParams["xtick.labelsize"] = 12
matplotlib.rcParams["ytick.labelsize"] = 12
matplotlib.rcParams["text.color"] = "k"
matplotlib.rcParams["figure.dpi"] = 200
# %%
IMAGES = "images"
if not os.path.exists("images"):
    os.mkdir(IMAGES)
# %%
housing = pd.read_csv('housing.csv')
# %%
housing.columns
# %%
housing.head()
# %%
housing.info()
# %%
housing["ocean_proximity"].value_counts()
# %%
# %% Create new features
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]
# %%
housing[housing.population_per_household > 20] = np.nan
#%%
housing.describe()
# %%
variables = ["median_house_value", "median_income", "housing_median_age"]
for x in variables:
    sns.histplot(housing, x=x)
    plt.savefig(f"{IMAGES}/{x}.png")
    plt.clf()
# %%
sns.scatterplot(data=housing, x="longitude", y="latitude", hue="median_house_value")
plt.savefig(f"{IMAGES}/scatter_lon_lat.png")
plt.clf()
# %%
sns.relplot(
    data=housing,
    x="longitude",
    y="latitude",
    hue="median_house_value",
    size="population",
    col="ocean_proximity",
    kind="scatter",
    col_wrap=2,
)
plt.savefig(f"{IMAGES}/scatter_lon_lat_pop.png")
plt.clf()
