# Report

## Data Description 
 
The report contains a dataset with 2,363 rows that includes various socio-economic indicators for different countries across multiple years. Key variables tracked include the Life Ladder score, Log GDP per capita, social support, health indicators, and perceptions of freedom, generosity, and corruption. This data aims to provide insights into the overall well-being and quality of life in various nations.
 
## Numerical Columns

The maximum correlations is found between columns Healthy life expectancy at birth and Log GDP per capita with a value of 0.8321419946722857.The minimum correlation is between columns Freedom to make life choices and Perceptions of corruption with a value of -0.4741100714440944

Outliers found in column {'Healthy life expectancy at birth': 20, 'Freedom to make life choices': 16, 'Positive affect': 9, 'Negative affect': 31, 'Perceptions of corruption': 194, 'Life Ladder': 2, 'Generosity': 39, 'Log GDP per capita': 1, 'Social support': 48}

The most important features are Life Ladder, Log GDP per capita and Perceptions of corruption with feature importances of importance    0.55445
Name: Life Ladder, dtype: float64, importance    0.118726
Name: Log GDP per capita, dtype: float64 and importance    0.105856
Name: Perceptions of corruption, dtype: float64 respectively

## Text Columns

No Text Columns Found

## Data Analysis 

The dataset shows a strong positive correlation (0.83) between Healthy life expectancy at birth and Log GDP per capita, while the weakest negative correlation (-0.47) is between Freedom to make life choices and Perceptions of corruption. Key features impacting the data include Life Ladder, Log GDP per capita, and Perceptions of corruption. Outliers were identified in several columns, with notable values in Healthy life expectancy and Perceptions of corruption.
 
## Data Insights 

The dataset illustrates a strong link between economic prosperity and health, suggesting that higher GDP per capita correlates with better health outcomes. Interestingly, while freedom in life choices appears to be compromised by perceptions of corruption, the outliers in health and corruption metrics indicate potential areas for targeted policy interventions to enhance societal well-being.
 
## Data Implications 

The dataset analyzed reveals crucial socio-economic insights across 2,363 countries, spotlighting the intricate relationship between economic prosperity and quality of life indicators. With a significant positive correlation of 0.83 between Healthy life expectancy at birth and Log GDP per capita, it underscores the vital role of economic conditions in influencing health outcomes. Conversely, the negative correlation of -0.47 between Freedom to make life choices and Perceptions of corruption suggests a troubling trend where citizens’ autonomy might be undermined by high corruption levels. The identification of outliers in healthy life expectancy and perceptions of corruption points to specific areas where targeted policy interventions could effectively improve societal well-being, highlighting the need for tailored strategies in governance and health initiatives. Overall, the implications of this dataset suggest a call to action for policymakers to address economic disparities and corruption to foster both health and freedom, thereby enhancing the overall quality of life in diverse nations.

## Visualizations

![Cluster_visualization.png](/happiness/Cluster_visualization.png)

![correlation_graph.png](/happiness/correlation_graph.png)

![outlier_boxplots.png](/happiness/outlier_boxplots.png)


