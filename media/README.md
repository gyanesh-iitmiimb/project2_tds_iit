# Report

## Data Description 
 
The report contains a dataset with 2,652 entries that catalog information about various media titles, including their release date, language, type (e.g., movie), title, contributors, and ratings based on overall quality and repeatability. The data is structured to facilitate analysis of trends and preferences in different media within specified categories.
 
## Numerical Columns

The maximum correlations is found between columns overall and quality with a value of 0.8259352331454309.The minimum correlation is between columns repeatability and quality with a value of 0.312126511538864

Outliers found in column {'overall': 1216, 'quality': 24}

The most important features are quality, repeatability and overall with feature importances of importance    0.5066
Name: quality, dtype: float64, importance    0.310879
Name: repeatability, dtype: float64 and importance    0.182521
Name: overall, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are   Column Name  Number of Unique Words
2        type                       8
1    language                      11
0        date                    2055

## Data Analysis 

The dataset reveals a strong correlation (0.83) between the columns "overall" and "quality," while a weaker correlation (0.31) exists between "repeatability" and "quality." Key features include "quality," "repeatability," and "overall." Outliers were identified in the "overall" and "quality" columns, along with unique elements in text columns: "type" (8 unique words), "language" (11 unique words), and "date" (2055 unique entries).
 
## Data Insights 

The dataset showcases a robust relationship between overall ratings and quality, suggesting that higher quality media tends to receive better overall ratings. However, the modest correlation between repeatability and quality indicates that a title’s quality may not directly translate to it being rewatched. The diversity in languages and types also points to a rich variety of media, which could influence audience preferences and trends over time.
 
## Data Implications 

The analysis of the dataset comprising 2,652 media entries uncovers critical insights into audience engagement and quality perception in media content. A high correlation (0.83) between overall ratings and quality suggests that productions perceived as high-quality are more likely to receive favorable overall ratings, reinforcing the importance of quality in media creation. However, the weaker correlation (0.31) between repeatability and quality indicates that high-quality titles aren't necessarily revisited, implying that factors such as genre, storytelling, and viewer fatigue might influence rewatchability independently of quality. The dataset's diversity, reflected in the 11 unique languages and 8 media types, highlights the breadth of content available, which could cater to varied audience preferences and encourage niche viewership. Such diversity in release dates (2055 unique entries) suggests evolving trends in media consumption over time. Overall, the findings emphasize the critical role of quality in establishing a title's reception while pointing to the necessity for deeper exploration into the elements driving repeat engagement. These implications are vital for media producers aiming to enhance both the quality and the repeatability of their projects to maximize audience retention.

## Visualizations

![Cluster_visualization.png](/media/Cluster_visualization.png)

![Column_Visualization_count.png](/media/Column_Visualization_count.png)

![Column_Visualization_mean.png](/media/Column_Visualization_mean.png)

![correlation_graph.png](/media/correlation_graph.png)

![outlier_boxplots.png](/media/outlier_boxplots.png)


