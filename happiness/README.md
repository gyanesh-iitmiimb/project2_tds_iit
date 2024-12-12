# Report

## Data Description 
 
The report includes a dataset comprising 2,363 rows of information from various countries, detailing factors related to well-being and quality of life over multiple years. Key metrics include the Life Ladder score, Log GDP per capita, social support levels, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption, and measures of positive and negative affect. This data provides insights into the socio-economic and psychological factors influencing life satisfaction across different nations.
 
## Numerical Columns

The maximum correlations is found between columns Log GDP per capita and Healthy life expectancy at birth with a value of 0.8321419946722857.The minimum correlation is between columns Perceptions of corruption and Freedom to make life choices with a value of -0.47411007144409434

Outliers found in column {'Perceptions of corruption': 194, 'Life Ladder': 2, 'Healthy life expectancy at birth': 20, 'Positive affect': 9, 'Social support': 48, 'Freedom to make life choices': 16, 'Log GDP per capita': 1, 'Generosity': 39, 'Negative affect': 31}

The most important features are Life Ladder, Log GDP per capita and Social support with feature importances of importance    0.557888
Name: Life Ladder, dtype: float64, importance    0.123072
Name: Log GDP per capita, dtype: float64 and importance    0.09531
Name: Social support, dtype: float64 respectively

## Text Columns

No Text Columns Found

## Data Analysis 

The dataset reveals a strong positive correlation (0.83) between Log GDP per capita and Healthy life expectancy at birth, while a negative correlation (-0.47) exists between Perceptions of corruption and Freedom to make life choices. Key features include Life Ladder, Log GDP per capita, and Perceptions of corruption, with Life Ladder being the most significant. Several outliers were identified across various columns.
 
## Data Insights 

The analysis highlights the pivotal role of economic factors in well-being, with a striking correlation between GDP and healthy life expectancy suggesting that economic prosperity directly enhances life quality. Furthermore, the inverse relationship between perceptions of corruption and freedom emphasizes the importance of transparent governance in fostering personal well-being and autonomy. Overall, the dataset provides a comprehensive view of how socio-economic variables interact to impact life satisfaction across different countries.
 
## Data Implications 

The report's dataset sheds light on critical socio-economic and psychological factors that shape well-being and quality of life across nations. With 2,363 entries, it underscores strong positive correlations, especially notable is the 0.83 correlation between Log GDP per capita and Healthy life expectancy, suggesting that higher economic output significantly enhances life quality. Conversely, a concerning -0.47 correlation between Perceptions of corruption and Freedom to make life choices indicates that poor governance can diminish personal autonomy and, consequently, overall well-being. The prominence of the Life Ladder score as the most significant feature highlights the subjective nature of life satisfaction, which is heavily influenced by economic stability and governance transparency. The identification of outliers suggests unique or exceptional cases that may warrant further investigation. Overall, the analysis emphasizes that economic prosperity and transparent governance are pivotal for improving citizens’ quality of life, revealing pathways for policymakers to enhance life satisfaction through targeted socio-economic strategies.

## Visualizations

![Cluster_visualization.png](/happiness/Cluster_visualization.png)

![correlation_graph.png](/happiness/correlation_graph.png)

![outlier_boxplots.png](/happiness/outlier_boxplots.png)


