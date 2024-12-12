# Report

## Data Description 
 
The report contains a dataset with 2652 rows detailing various entries related to media, specifically movies in different languages, along with associated attributes. Each entry includes fields such as date, language, type, title, contributors, and ratings for overall performance, quality, and repeatability. The data captures insights on content released over time, indicating user assessments and preferences.
 
## Numerical Columns

The maximum correlations is found between columns quality and overall with a value of 0.8259352331454309.The minimum correlation is between columns quality and repeatability with a value of 0.31212651153886395

Outliers found in column {'quality': 24, 'overall': 1216}

The most important features are quality, repeatability and overall with feature importances of importance    0.50358
Name: quality, dtype: float64, importance    0.31316
Name: repeatability, dtype: float64 and importance    0.18326
Name: overall, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are   Column Name  Number of Unique Words
2        type                       8
1    language                      11
0        date                    2055

## Data Analysis 

The dataset reveals a strong correlation of 0.83 between the columns 'quality' and 'overall', while a weaker correlation of 0.31 exists between 'quality' and 'repeatability'. Key features identified are 'quality', 'repeatability', and 'overall', with respective importances of 0.50, 0.31, and 0.18. Notable outliers are present in 'quality' and 'overall', and the text columns have various unique elements, such as 8 unique types and 11 unique languages.
 
## Data Insights 

The dataset reveals a strong relationship between overall performance and quality of movies, suggesting that high-quality content tends to receive better ratings overall. However, the weaker link with repeatability indicates that even quality films may not guarantee viewers will return for more. Unique language and type diversity suggests a rich landscape for movie analysis, opening avenues for targeted content strategies.
 
## Data Implications 

The dataset encompassing 2,652 movie entries reflects diverse media content across various languages and genres, highlighting essential attributes such as date, type, title, contributors, and ratings for quality, overall performance, and repeatability. A prominent correlation coefficient of 0.83 between 'quality' and 'overall' ratings suggests that higher-quality films are likely to achieve better overall ratings, illustrating the importance of content quality in viewer assessments. Conversely, the correlation of 0.31 between 'quality' and 'repeatability' implies that while quality is significant, it does not necessarily foster repeated viewings. This indicates potential market opportunities for films that may perform well critically but lack high repeatability, suggesting targeted marketing strategies could enhance audience engagement. Additionally, the presence of eight unique types and eleven unique languages underscores the dataset's richness, opening pathways for more granular audience analysis and tailored content strategies to capitalize on diverse viewer preferences. Notable outliers in quality and overall ratings signal opportunities for further investigation into what influences viewer ratings, paving the way for enhanced content production and marketing efforts.

## Visualizations

![Cluster_visualization.png](/media/Cluster_visualization.png)

![Column_Visualization_count.png](/media/Column_Visualization_count.png)

![Column_Visualization_mean.png](/media/Column_Visualization_mean.png)

![correlation_graph.png](/media/correlation_graph.png)

![outlier_boxplots.png](/media/outlier_boxplots.png)


