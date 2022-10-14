import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
import numpy as np

# import data
files = ["2019","2020"]
df = pd.DataFrame()
for file in files:
    test = pd.read_csv(file+"_season_stats.csv")
    df = pd.concat([df,test])

# remove asterisks from team names
df["Team"] = df["Team"].apply(lambda x: x.replace("*",""))

y = df.loc[:, "Rk"]
x = df.drop(["Team","Rk","G"],axis=1).reset_index().drop("index",axis=1)
# feature selection and fit model
model = LinearRegression()
selector = RFE(model, n_features_to_select=5, step=1)
xnew = selector.fit_transform(x,y)

# import prediction data
pred_data = pd.read_csv("2021_season_stats.csv")
teams = pred_data["Team"].apply(lambda x: x.replace("*",""))
xpred = pred_data.drop(["Team","Rk","G"],axis=1)

# get preds
ypred = selector.predict(xpred)

# build pred df
new_df = pd.DataFrame(data={"Rk":pred_data["Rk"],"Team":pred_data["Team"].apply(lambda x: x.replace("*","")), "Pred_Rk":ypred})
new_df = new_df.sort_values("Pred_Rk",ascending=True)
new_df["Predicted"] = np.arange(1, len(new_df)+1)
print(new_df)

# Actual                Team    Pred_Rk  Predicted
# 10          Denver Nuggets   7.629915       1
# 9                Utah Jazz   8.382894       2
# 3    Golden State Warriors   9.128107       3
# 1             Phoenix Suns  10.075724       4
# 4               Miami Heat  10.160835       5
# 13           Chicago Bulls  10.361998       6
# 7          Milwaukee Bucks  11.011512       7
# 16           Atlanta Hawks  11.511770       8
# 6           Boston Celtics  12.849274       9
# 17       Charlotte Hornets  12.945803      10
# 15           Brooklyn Nets  13.062967      11
# 14     Cleveland Cavaliers  14.022040      12
# 23      Los Angeles Lakers  14.612989      13
# 8       Philadelphia 76ers  14.646198      14
# 12  Minnesota Timberwolves  15.093464      15
# 5         Dallas Mavericks  16.112054      16
# 21      Washington Wizards  16.212764      17
# 22       San Antonio Spurs  16.443903      18
# 30         Houston Rockets  16.668570      19
# 26          Indiana Pacers  16.773675      20
# 18    Los Angeles Clippers  16.797029      21
# 24        Sacramento Kings  18.866869      22
# 2        Memphis Grizzlies  18.878966      23
# 20    New Orleans Pelicans  22.312055      24
# 11         Toronto Raptors  22.640707      25
# 25  Portland Trail Blazers  23.557492      26
# 19         New York Knicks  24.962204      27
# 29           Orlando Magic  27.849930      28
# 27   Oklahoma City Thunder  29.784343      29
# 28         Detroit Pistons  31.098710      30