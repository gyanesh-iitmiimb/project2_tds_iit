# Report

## Data Description 
 
The report consists of a dataset with 2,652 entries detailing various media content, including movies in different languages. Each entry includes attributes such as the date of release, language, type of media, title, contributors (such as actors), and ratings in overall, quality, and repeatability categories. The data appears to be structured for analysis of media performance and audience engagement.
 
## Numerical Columns

The maximum correlations is found between columns overall and quality with a value of 0.8259352331454309.The minimum correlation is between columns repeatability and quality with a value of 0.312126511538864

Outliers found in column {'overall': 1216, 'quality': 24}

The most important features are quality, repeatability and overall with feature importances of importance    0.508897
Name: quality, dtype: float64, importance    0.310696
Name: repeatability, dtype: float64 and importance    0.180407
Name: overall, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are   Column Name  Number of Unique Words
2        type                       8
1    language                      11
0        date                    2055

## Data Analysis 

The dataset reveals a strong correlation between the "overall" and "quality" columns (0.83), while the weakest correlation is between "repeatability" and "quality" (0.31). Key features identified are "quality," "repeatability," and "overall," with importances of 0.51, 0.31, and 0.18 respectively. Outliers were detected in both "overall" (1216) and "quality" (24), and the text columns have varying unique elements.
 
## Data Insights 

The dataset's strong correlation between "overall" and "quality" suggests that improving content quality can significantly enhance audience ratings. However, the weak link between "repeatability" and "quality" indicates that high-quality content doesn't always lead to frequent re-watching, pointing to potential insights into viewer preferences and engagement strategies. Outlier detection may reveal unique media entries that could inform targeted marketing efforts or content recommendations.
 
## Data Implications 

The dataset comprising 2,652 entries concerning diverse media content highlights significant insights into the relationship between different attributes affecting audience engagement. Key findings reveal a strong correlation (0.83) between "overall" ratings and "quality," indicating that higher quality often translates to better overall audience ratings. Conversely, the weak correlation (0.31) between "repeatability" and "quality" suggests that even high-quality content may not incentivize viewers to re-watch, reflecting complex viewer preferences. Feature importance analysis shows "quality" as the most crucial factor (0.51), followed by "repeatability" (0.31) and "overall" ratings (0.18). Outliers in both "overall" (1216) and "quality" (24) ratings could be targeted for tailored marketing strategies. The varied unique text elements within the dataset open avenues for deeper qualitative analyses. Overall, these insights underscore the importance of prioritizing content quality to optimize viewer ratings and highlight opportunities for leveraging outliers in targeted engagement tactics.

## Visualizations

![Cluster_visualization.png](/media/Cluster_visualization.png)

![Column_Visualization_count.png](/media/Column_Visualization_count.png)

![Column_Visualization_mean.png](/media/Column_Visualization_mean.png)

![correlation_graph.png](/media/correlation_graph.png)

![outlier_boxplots.png](/media/outlier_boxplots.png)


