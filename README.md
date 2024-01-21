# Predictive Analysis of Real Estate Investment Returns

**Presented by: Jan Cichocki and Bertrand Badinga**  
**Date: [Insert Date]**

## Introduction
In this project, we aim to develop a machine learning model that predicts Return on Investment (ROI) in real estate. Our focus is on using predictive analysis to assist in making informed decisions in the real estate market.

## Objectives
- Explore and preprocess a dataset related to real estate.
- Implement a RandomForestRegressor for ROI prediction in real estate investments.
- Interpret the model's results to provide insights for investment strategies.

## Data Source and Exploration
Our dataset includes various features of real estate properties, such as location, size, age, market conditions, and historical ROI. The initial phase involved understanding variable distributions and identifying potential correlations. We used histograms and scatter plots for visual exploration.

## Data Cleaning and Preprocessing
We prioritized data cleaning, handling missing data and outliers. A key part of our approach was feature engineering, where we created new relevant features, like 'PropertyAge' derived from 'YearBuilt'. We then standardized the features using StandardScaler to prepare them for model training.

## Model Building - RandomForestRegressor
The RandomForestRegressor was selected due to its robustness in handling complex datasets. We carefully trained the model with our dataset, focusing on optimal model parameters such as the number of estimators.

## Model Evaluation
We evaluated our model using Mean Squared Error (MSE) and R-squared (R2). Our evaluation compared the model's predicted ROI values with actual data, using plots for visual representation. We also discussed the accuracy of the model and potential improvements.

## Feature Importance
Our analysis included an examination of which variables significantly predict ROI. We used bar graphs to visually represent feature importance, offering insights into the varying impacts of different features on ROI.

## Implications and Applications
We discussed how our model can be applied in real-world scenarios, particularly for investors, real estate agents, and financial analysts. We also addressed the limitations of our current model and explored potential directions for future research.

## Conclusion
Our project concluded with a recap of key findings and their relevance to real estate investment strategies. We reflected on our learning experience, the challenges we encountered, and future opportunities in this field.
