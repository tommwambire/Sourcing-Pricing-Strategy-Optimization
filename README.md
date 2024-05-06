# Project Overview: Optimizing Sourcing and Pricing Strategies for GlobeHarvest Co. in Kenya

## Introduction
GlobeHarvest Co. is an emerging import-export company poised to enter the Kenyan agricultural market. With a commitment to leveraging data-driven strategies, GlobeHarvest aims to optimize its sourcing and pricing strategies to establish a competitive presence in Kenya's agricultural sector. By harnessing the power of data analytics, GlobeHarvest seeks to gain valuable insights into market dynamics, consumer preferences, and pricing trends to drive informed decision-making and maximize profitability.

## Business Understanding
Kenya's agricultural market offers immense potential for GlobeHarvest Co., characterized by diverse regions with varying agricultural capabilities and consumer demands. However, navigating this complex landscape presents several challenges, including identifying cost-effective sourcing locations, strategically timing purchases, and ensuring competitive pricing amid price variabilities across regions. To succeed in the Kenyan market, GlobeHarvest must develop a deep understanding of market dynamics, consumer behavior, and competitive factors to optimize its procurement processes and pricing strategies effectively.

## Problem Statement
GlobeHarvest Co. faces the following key challenges in entering the Kenyan agricultural market:

- **Identifying Optimal Sourcing Locations:** The company needs to identify the most cost-effective sourcing locations across different Kenyan counties to minimize procurement costs and ensure a reliable supply chain.
- **Timing Purchases Strategically:** GlobeHarvest requires insights into the optimal timing for purchasing various commodities, considering seasonal fluctuations, market trends, and price dynamics.
- **Navigating Price Variabilities:** Significant price discrepancies exist across different regions in Kenya, necessitating a systematic approach to ensure competitive pricing and optimize profitability.

## Objectives
The primary objectives of GlobeHarvest Co. in optimizing its sourcing and pricing strategies for the Kenyan market are as follows:

1. **Identify Cost-Effective Sourcing Locations:** Analyze data to identify regions in Kenya that offer the most cost-effective sourcing opportunities for various food commodities.
2. **Strategically Time Purchases:** Utilize historical data and market insights to determine the optimal timing for purchasing specific commodities, considering seasonal trends and market dynamics.
3. **Navigate Price Variabilities:** Develop strategies to navigate price variabilities across different regions in Kenya, ensuring competitive pricing and maximizing profitability.

## Data Understanding
The dataset obtained from WFP Kaggle consists of food price data collected in Kenya, providing valuable insights into the pricing dynamics of various food commodities across different regions and markets.
The dataset contains 10,767 rows, each representing a unique observation of food prices in a specific market on a particular date. This dataset provides a comprehensive view of food pricing trends and variations across different regions and market types in Kenya, offering valuable insights for analysis and decision-making in the agricultural sector.

## Modelling
### Model Selection
In this section, various machine learning models are evaluated and compared to select the most suitable one for predicting future prices of wholesale commodities.

### Linear Regression Model
The linear regression model was the first one attempted. Here are the results:

Mean Squared Error (MSE): 202.87
Coefficient of Determination (R^2 Score): 0.7943

### Random Forest Regressor
Next, a Random Forest Regressor was trained and evaluated:

Mean Squared Error (MSE): 96.62
Coefficient of Determination (R^2 Score): 0.9020

### Gradient Boosting Regressor
A Gradient Boosting Regressor was also tested:

Mean Squared Error (MSE): 96.62
Coefficient of Determination (R^2 Score): 0.9020

### Decision Tree Regressor
Lastly, a Decision Tree Regressor was included:

Mean Squared Error (MSE): 211.58
Coefficient of Determination (R^2 Score): 0.7855

### Model Evaluation
Comparing the models, the Random Forest Regressor outperformed the others in terms of both MSE and R^2 Score.

Random Forest Regressor: MSE = 96.62, R^2 = 0.9020
Gradient Boosting Regressor: MSE = 96.62, R^2 = 0.9020
Linear Regression: MSE = 202.87, R^2 = 0.7943
Decision Tree Regressor: MSE = 211.58, R^2 = 0.7855
Therefore, the Random Forest Regressor was chosen as the final model.

### Hyperparameter Tuning
To optimize the Random Forest model further, a grid search was performed to find the best hyperparameters:

Best Hyperparameters: {'max_depth': None, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 100}

### Final Model
After tuning, the Random Forest Regressor with the best hyperparameters was evaluated on the test set:

Mean Squared Error (MSE): 27.31
Coefficient of Determination (R^2 Score): 0.9723
The significantly reduced MSE and improved R^2 score demonstrate the effectiveness of the tuned Random Forest model in predicting future wholesale commodity prices.






