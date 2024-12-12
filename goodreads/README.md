# Report

## Data Description 
 
The report contains a dataset with information on books, including fields such as book IDs, ISBN numbers, ratings, and image URLs. It consists of 10,000 rows, encompassing various attributes related to each book's identity and popularity, including metrics for user ratings. This data can be used for analysis of book trends, reader preferences, and overall book popularity.
 
## Numerical Columns

The maximum correlations is found between columns ratings_count and work_ratings_count with a value of 0.9950949109767664.The minimum correlation is between columns ratings_2 and average_rating with a value of -0.11433083463802127

Outliers found in column {'ratings_2': 1156, 'work_text_reviews_count': 1005, 'ratings_count': 1163, 'average_rating': 158, 'ratings_1': 1140, 'ratings_3': 1149, 'ratings_4': 1131, 'books_count': 844, 'ratings_5': 1158, 'isbn13': 556, 'work_ratings_count': 1143}

The most important features are ratings_4, work_ratings_count and ratings_3 with feature importances of importance    0.494741
Name: ratings_4, dtype: float64, importance    0.339257
Name: work_ratings_count, dtype: float64 and importance    0.053983
Name: ratings_3, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are      Column Name  Number of Unique Words
1  language_code                      25
0           isbn                    9300

## Data Analysis 

The dataset exhibits a strong correlation (0.995) between the columns ratings_count and work_ratings_count, while the weakest correlation (-0.114) occurs between ratings_2 and average_rating. Key features impacting the dataset include ratings_4, work_ratings_count, and ratings_3, with respective importances of 0.472, 0.332, and 0.079. Additionally, several outliers were identified across multiple rating-related columns, and the text column language_code contains 25 unique elements, while the isbn column has 9,300 unique values.
 
## Data Insights 

The dataset reveals a powerful correlation between ratings_count and work_ratings_count, suggesting that these metrics are indicative of each other in assessing book popularity. Notably, while ratings_4 significantly influences overall ratings, the presence of outliers and diverse language codes underscore the complexity of reader preferences and market trends, signaling opportunities for targeted marketing strategies.
 
## Data Implications 

The dataset on books reveals significant insights into reader preferences and market trends. With 10,000 entries, the strong correlation (0.995) between ratings_count and work_ratings_count indicates that these metrics are key indicators of a book's popularity, suggesting that higher user engagement correlates with higher ratings. Key features influencing ratings include ratings_4, work_ratings_count, and ratings_3, with ratings_4 being the most impactful. However, the presence of outliers in rating-related columns hints at inconsistencies in reader assessments, indicating a need for further investigation into these anomalies. Moreover, the diversity in language codes (25 unique elements) and ISBN numbers (9,300 unique values) highlights the global reach and multifaceted nature of book readership. This complexity offers an opportunity for targeted marketing strategies based on specific reader demographics and preferences, allowing publishers and marketers to tailor their approaches effectively to enhance engagement and sales.

## Visualizations

![Cluster_visualization.png](/goodreads/Cluster_visualization.png)

![Column_Visualization_count.png](/goodreads/Column_Visualization_count.png)

![Column_Visualization_mean.png](/goodreads/Column_Visualization_mean.png)

![correlation_graph.png](/goodreads/correlation_graph.png)

![outlier_boxplots.png](/goodreads/outlier_boxplots.png)


