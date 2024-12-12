# Report

## Data Description 
 
The report presents a dataset featuring various quality of life metrics across different countries over multiple years. Key indicators include the Life Ladder score, which reflects subjective well-being, as well as measures like GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption, and levels of positive and negative affect. This dataset comprises 2,363 rows, capturing diverse aspects of human well-being across nations.
 
## Numerical Columns

The maximum correlations is found between columns Healthy life expectancy at birth and Log GDP per capita with a value of 0.832141994672286.The minimum correlation is between columns Perceptions of corruption and Freedom to make life choices with a value of -0.47411007144409434

Outliers found in column {'Positive affect': 9, 'Log GDP per capita': 1, 'Perceptions of corruption': 194, 'Life Ladder': 2, 'Freedom to make life choices': 16, 'Generosity': 39, 'Negative affect': 31, 'Social support': 48, 'Healthy life expectancy at birth': 20}

The most important features are Life Ladder, Log GDP per capita and Social support with feature importances of importance    0.557982
Name: Life Ladder, dtype: float64, importance    0.128114
Name: Log GDP per capita, dtype: float64 and importance    0.095067
Name: Social support, dtype: float64 respectively

## Text Columns

No Text Columns Found

## Data Analysis 

The dataset shows a strong correlation of 0.83 between Healthy life expectancy at birth and Log GDP per capita, while the weakest correlation of -0.47 is between Perceptions of corruption and Freedom to make life choices. Key features include Life Ladder, Log GDP per capita, and Perceptions of corruption, with respective importances of 0.56, 0.12, and 0.10. Additionally, several outliers were identified across various columns.
 
## Data Insights 

The dataset highlights the critical interplay between economic factors and health, evident in the strong correlation (0.83) between Healthy life expectancy and GDP per capita. Interestingly, perceptions of corruption seem to negatively influence the freedom people feel in their life choices, suggesting potential societal constraints that impact overall well-being. The identified outliers may warrant further investigation to better understand unique situations that deviate from established patterns.
 
## Data Implications 

The dataset analyzed reveals significant insights into the interplay of economic and health factors influencing quality of life across countries. A robust correlation of 0.83 between Healthy life expectancy at birth and Log GDP per capita underscores the critical role economic prosperity plays in enhancing people's health and overall well-being. Conversely, the negative correlation (-0.47) between Perceptions of corruption and Freedom to make life choices highlights how societal trust issues may undermine personal autonomy and satisfaction. This suggests that countries with high corruption perceptions may restrict individuals' freedoms, adversely affecting their quality of life. The feature Importance scores show that while the Life Ladder score is central to measuring well-being, economic and governance indicators also significantly contribute to understanding diverse outcomes. The presence of outliers in the dataset indicates that some nations exhibit unique circumstances deviating from general trends, which warrants further investigation. Understanding these anomalies could provide deeper insights into the complex factors influencing well-being and help tailor policies to enhance quality of life in varying contexts.

## Visualizations

![Cluster_visualization.png](/happiness\Cluster_visualization.png)

![correlation_graph.png](/happiness\correlation_graph.png)

![outlier_boxplots.png](/happiness\outlier_boxplots.png)


