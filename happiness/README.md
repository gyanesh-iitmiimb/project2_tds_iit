# Report

## Data Description 
 
The report contains data on various well-being indicators across different countries, encompassing 2,363 rows. Each entry includes metrics such as the Life Ladder score, Log GDP per capita, social support, healthy life expectancy, freedom to make life choices, generosity, perceptions of corruption, and positive and negative affect, all categorized by country and year. This data is useful for analyzing the correlation between economic, social, and subjective well-being indicators globally.
 
## Numerical Columns

The maximum correlations is found between columns Log GDP per capita and Healthy life expectancy at birth with a value of 0.8321419946722857.The minimum correlation is between columns Perceptions of corruption and Freedom to make life choices with a value of -0.4741100714440944

Outliers found in column {'Negative affect': 31, 'Social support': 48, 'Healthy life expectancy at birth': 20, 'Life Ladder': 2, 'Freedom to make life choices': 16, 'Log GDP per capita': 1, 'Positive affect': 9, 'Perceptions of corruption': 194, 'Generosity': 39}

The most important features are Life Ladder, Log GDP per capita and Perceptions of corruption with feature importances of importance    0.558361
Name: Life Ladder, dtype: float64, importance    0.123434
Name: Log GDP per capita, dtype: float64 and importance    0.09385
Name: Perceptions of corruption, dtype: float64 respectively

## Text Columns

No Text Columns Found

## Data Analysis 

The dataset shows a strong positive correlation (0.83) between Log GDP per capita and Healthy life expectancy at birth, while a negative correlation (-0.47) exists between Perceptions of corruption and Freedom to make life choices. Key features include Life Ladder, Log GDP per capita, and Perceptions of corruption, with respective importances of 56%, 12%, and 10%. Additionally, several outliers were identified across various columns.
 
## Data Insights 

The dataset reveals a compelling link between economic prosperity and health, with higher GDP per capita significantly correlating to better life expectancy, showcasing the profound impact of wealth on well-being. Conversely, the negative correlation between perceptions of corruption and personal freedom highlights the detrimental effects of corruption on individual autonomy, suggesting that enhancing governance could improve societal well-being. Outlier analysis may uncover unique country experiences, prompting deeper investigation into their distinct socio-economic dynamics.
 
## Data Implications 

The report presents a comprehensive analysis of well-being indicators across 2,363 countries, revealing critical insights into the complex interplay between economic prosperity and individual well-being. Notably, the strong positive correlation (0.83) between Log GDP per capita and healthy life expectancy indicates that wealthier nations tend to foster better health outcomes for their citizens, underscoring the crucial role of economic resources in enhancing life quality. In contrast, the negative correlation (-0.47) between perceptions of corruption and the freedom to make life choices suggests that high levels of corruption can severely restrict individual autonomy, ultimately harming societal well-being. The primary indicators, including the Life Ladder score, Log GDP per capita, and perceptions of corruption, play significant roles in shaping overall life satisfaction, with life ladder importance at 56%. Outlier analysis may provide further insights into unique socio-economic conditions in specific countries, prompting targeted strategies for intervention. Consequently, the data emphasizes the necessity for improved governance and economic strategies to foster overall well-being, highlighting that tackling corruption could significantly enhance personal freedoms and health outcomes.

## Visualizations

![Cluster_visualization.png](/happiness/Cluster_visualization.png)

![correlation_graph.png](/happiness/correlation_graph.png)

![outlier_boxplots.png](/happiness/outlier_boxplots.png)


