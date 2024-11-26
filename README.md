Exploratory Data Analysis and Cleaning of Smartphone Dataset
Overview:
This project involves extensive data cleaning and exploratory data analysis (EDA) performed on a smartphone dataset. The dataset was initially very unclean, requiring significant preprocessing before meaningful analysis could be conducted. After cleaning, EDA techniques were applied to uncover insights and understand the structure of the data.

Project Objectives:
Clean the raw and unstructured smartphone dataset to make it ready for analysis.
Perform EDA to explore relationships, trends, and patterns within the data.
Visualize the key findings using various graphs and plots.
Dataset
The dataset contains various attributes of smartphones, including brand, operating system (OS), features like 5G support, NFC, and IR blaster availability, and other technical specifications.
The raw dataset was highly unstructured, with issues such as missing values, inconsistent formatting, redundant columns, and invalid entries.
Steps in the Project
1. Data Cleaning
The cleaning process involved:

Handling Missing Values: Filled missing entries based on logical imputation or removed rows/columns with excessive missing data.
Renaming Columns: Ensured consistent and meaningful column names for better readability.
Data Type Conversion: Converted numerical, categorical, and datetime data into appropriate formats.
Removing Redundancies: Removed duplicate rows and irrelevant features (e.g., columns like has_IR_Blaster dropped after analysis).
Outlier Detection: Handled outliers to ensure reliable analysis.
Feature Standardization: Reformatted categorical and numerical data to a unified structure.
Note: The cleaning process was time-consuming due to the highly unclean nature of the dataset.

2. Exploratory Data Analysis (EDA)
Univariate Analysis:
Countplots, bar charts, and pie charts to analyze individual categorical variables like smartphone brands, operating systems, and feature availability (e.g., 5G, NFC).
Bivariate Analysis:
Boxplots and scatter plots to explore relationships between numeric features (e.g., price and specifications).
Multivariate Analysis:
Correlation heatmaps and pairplots to identify relationships among multiple features.
Insights Derived:
Identified the top smartphone brands in the dataset.
Observed trends in feature adoption (e.g., the percentage of phones supporting 5G and NFC).
Analyzed feature preferences across brands and operating systems.
