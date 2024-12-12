# Report

## Data Description 
 
The report contains a dataset with 2,652 entries detailing information about various media types, specifically focusing on movies in the Tamil language. Each entry includes fields such as date, language, type, title, contributors, and ratings across several criteria including overall rating, quality, and repeatability. The data is organized to provide insights into specific media attributes and user feedback.
 
## Numerical Columns

The maximum correlations is found between columns quality and overall with a value of 0.8259352331454309.The minimum correlation is between columns repeatability and quality with a value of 0.312126511538864

Outliers found in column {'overall': 1216, 'quality': 24}

The most important features are quality, repeatability and overall with feature importances of importance    0.507573
Name: quality, dtype: float64, importance    0.311036
Name: repeatability, dtype: float64 and importance    0.181391
Name: overall, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are   Column Name  Number of Unique Words
2        type                       8
1    language                      11
0        date                    2055

## Data Analysis 

The dataset reveals a strong correlation (0.83) between the 'quality' and 'overall' columns, while the weakest correlation (0.31) is between 'repeatability' and 'quality.' Key features identified include 'quality,' 'repeatability,' and 'overall' with respective importances of 0.50, 0.31, and 0.18. Outliers were detected in 'overall' (1216) and 'quality' (24), while the text columns display various unique elements: 8 for 'type,' 11 for 'language,' and 2055 for 'date.'
 
## Data Insights 

The analysis highlights a strong positive correlation between the quality and overall ratings of Tamil movies, suggesting that higher quality typically leads to better audience reception. Conversely, the low correlation between repeatability and quality indicates that well-rated films may not necessarily encourage repeat viewings. The dataset's diversity in dates and types showcases a rich variety of content, yet the presence of notable outliers in overall ratings suggests potential anomalies or standout performances in certain films.
 
## Data Implications 

The analysis of the dataset containing 2,652 entries about Tamil movies reveals insightful trends and relationships among various media attributes. A significant positive correlation of 0.83 between 'quality' and 'overall' ratings suggests that higher quality movies generally receive better audience reception. However, the weak correlation (0.31) between 'repeatability' and 'quality' indicates that even well-rated films might not encourage repeat viewings, implying factors beyond quality influencing audience loyalty. The dataset also indicates a diverse range of content with notable outliers in both 'overall' (1216) and 'quality' (24) ratings, highlighting exceptional films that may skew average ratings. Unique elements are abundant with 8 recognized types, 11 languages, and substantial variability in release dates (2055). The findings underline the importance of quality in determining overall reception while also noting potential anomalies that deserve further investigation to understand viewer engagement comprehensively.

## Visualizations

![Cluster_visualization.png](/media/Cluster_visualization.png)

![Column_Visualization_count.png](/media/Column_Visualization_count.png)

![Column_Visualization_mean.png](/media/Column_Visualization_mean.png)

![correlation_graph.png](/media/correlation_graph.png)

![outlier_boxplots.png](/media/outlier_boxplots.png)


