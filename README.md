# NBA-Projections
Simple linear regression for predicting final rankings of NBA teams at the end of the season

## Overview
This project provides an introductory sample for those who are trying to get into the sports analytics field.
I have tried to keep the code base very simple and straight forward so that it is easily ingestible.

### Process
Takes previous 2 years of NBA team data and uses a regression model to predict how teams should have done in the past season.
More specifically, we use data from the 2019-2020 and 2020-2021 season to train the models and predict using the 2021-2022 season's data.

#### Data Gathering
All data was gathered from basketball-reference.com. By going to the season overview, I was able to download csv-formatted data containing team summary statistics.

#### Feature Selection
I utilized a backward-selection variable selection process to select the 5 best features from all of the data provided.
Backward-selection in a general sense takes an input dataset of many features and slowly reduces the number of features until the desired number is left.
The criteria for determining which feature to exclude can be different based on which method you are using. In this sample, I am using the base scikit-learn RFE package.

#### Model Training
Once the features are selected, the remaining data columns are passed through the regression object and the model is fitted. By taking the input data and output values, the model is able to generate weights for each feature to determine how important they are in predicting the final ranking of the team at the end of the season. I used a very general linear regression model, but this can be substituted for many other types of models with more complex algorithms.

#### Prediction
After the model is fitted, a prediction dataset can be passed into the same model object to generate predictions on how each team will perform at the end of the season.

#### Outputs
Actual                Team    Pred_Rk  Predicted
10          Denver Nuggets   7.629915       1
9                Utah Jazz   8.382894       2
3    Golden State Warriors   9.128107       3
1             Phoenix Suns  10.075724       4
4               Miami Heat  10.160835       5
13           Chicago Bulls  10.361998       6
7          Milwaukee Bucks  11.011512       7
16           Atlanta Hawks  11.511770       8
6           Boston Celtics  12.849274       9
17       Charlotte Hornets  12.945803      10
15           Brooklyn Nets  13.062967      11
14     Cleveland Cavaliers  14.022040      12
23      Los Angeles Lakers  14.612989      13
8       Philadelphia 76ers  14.646198      14
12  Minnesota Timberwolves  15.093464      15
5         Dallas Mavericks  16.112054      16
21      Washington Wizards  16.212764      17
22       San Antonio Spurs  16.443903      18
30         Houston Rockets  16.668570      19
26          Indiana Pacers  16.773675      20
18    Los Angeles Clippers  16.797029      21
24        Sacramento Kings  18.866869      22
2        Memphis Grizzlies  18.878966      23
20    New Orleans Pelicans  22.312055      24
11         Toronto Raptors  22.640707      25
25  Portland Trail Blazers  23.557492      26
19         New York Knicks  24.962204      27
29           Orlando Magic  27.849930      28
27   Oklahoma City Thunder  29.784343      29
28         Detroit Pistons  31.098710      30