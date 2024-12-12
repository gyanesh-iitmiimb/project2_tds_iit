# Report

## Data Description 
 
The report presents a dataset containing 2,363 rows of information related to various countries. It includes indicators such as the Life Ladder, GDP per capita (logged), social support, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption, and levels of positive and negative affect, with data spanning multiple years. This information is aimed at assessing overall well-being and quality of life across different nations.
 
## Numerical Columns

The maximum correlations is found between columns Healthy life expectancy at birth and Log GDP per capita with a value of 0.832141994672286.The minimum correlation is between columns Perceptions of corruption and Freedom to make life choices with a value of -0.4741100714440944

Outliers found in column {'Negative affect': 31, 'Log GDP per capita': 1, 'Social support': 48, 'Generosity': 39, 'Life Ladder': 2, 'Freedom to make life choices': 16, 'Healthy life expectancy at birth': 20, 'Perceptions of corruption': 194, 'Positive affect': 9}

The most important features are Life Ladder, Log GDP per capita and Social support with feature importances of importance    0.563421
Name: Life Ladder, dtype: float64, importance    0.133942
Name: Log GDP per capita, dtype: float64 and importance    0.09267
Name: Social support, dtype: float64 respectively

## Text Columns

No Text Columns Found

## Data Analysis 

The dataset reveals a strong correlation (0.83) between Healthy life expectancy at birth and Log GDP per capita, while a weaker negative correlation (-0.47) exists between Perceptions of corruption and Freedom to make life choices. Key features identified include Life Ladder, Log GDP per capita, and Social support, with notable outliers detected in various columns, particularly Perceptions of corruption.
 
## Data Insights 

The dataset underscores the critical relationship between economic prosperity and well-being, as evidenced by the strong correlation between Healthy life expectancy and Log GDP per capita. Conversely, the negative correlation between Perceptions of corruption and Freedom to make life choices highlights the potential social impact of corruption on individual freedoms. Identifying outliers in Perceptions of corruption could provide valuable insights for targeted interventions in improving quality of life across countries.
 
## Data Implications 

The dataset, encompassing 2,363 entries from various countries, provides critical insights into the interplay between economic factors and overall well-being. A strong positive correlation (0.83) between healthy life expectancy at birth and logged GDP per capita highlights that economic prosperity significantly influences quality of life. Additionally, the weaker negative correlation (-0.47) between perceptions of corruption and freedom to make life choices suggests that higher corruption levels can restrict personal liberties, potentially diminishing overall well-being. Identifying outliers in corruption perceptions might unveil specific nations that could benefit from targeted interventions to enhance quality of life. The report emphasizes the importance of economic and social indicators—like the Life Ladder and social support—in assessing well-being, suggesting that policy-makers should focus on addressing corruption to promote freedom and improve health outcomes.

## Visualizations

![Cluster_visualization.png](/happiness/Cluster_visualization.png)

![correlation_graph.png](/happiness/correlation_graph.png)

![outlier_boxplots.png](/happiness/outlier_boxplots.png)


