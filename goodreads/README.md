# Report

## Data Description 
 
The data in this report includes a subset of a larger dataset containing information about books, specifically focusing on attributes such as book IDs, ISBNs, ratings, and image URLs. It comprises 10,000 rows of data, capturing various metrics related to each book's performance and accessibility on platforms like Goodreads, including the count of ratings at different levels.
 
## Numerical Columns

The maximum correlations is found between columns ratings_count and work_ratings_count with a value of 0.9950949109767664.The minimum correlation is between columns average_rating and ratings_2 with a value of -0.11433083463802127

Outliers found in column {'isbn13': 556, 'average_rating': 158, 'ratings_5': 1158, 'work_text_reviews_count': 1005, 'ratings_2': 1156, 'ratings_1': 1140, 'ratings_3': 1149, 'work_ratings_count': 1143, 'ratings_count': 1163, 'books_count': 844, 'ratings_4': 1131}

The most important features are ratings_4, work_ratings_count and ratings_3 with feature importances of importance    0.450084
Name: ratings_4, dtype: float64, importance    0.384857
Name: work_ratings_count, dtype: float64 and importance    0.051947
Name: ratings_3, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are      Column Name  Number of Unique Words
1  language_code                      25
0           isbn                    9300

## Data Analysis 

The dataset reveals a strong correlation (0.995) between ratings_count and work_ratings_count, while the lowest correlation (-0.114) is between average_rating and ratings_2. The key features identified are ratings_4, work_ratings_count, and ratings_3, with importances of 0.44006, 0.326958, and 0.119436 respectively. Additionally, there are notable outliers in various rating columns, and the text columns have a limited number of unique entries, specifically with 25 unique language codes and 9300 ISBNs.
 
## Data Insights 

The dataset highlights a significant dependency between overall ratings and work-specific ratings, suggesting that a high volume of ratings typically mirrors a book's popularity. However, the weak correlation between average ratings and lower ratings indicates that while many books might receive numerous reviews, they don’t always achieve high average satisfaction. The identified key features for performance metrics can guide targeted marketing strategies to enhance reader engagement.
 
## Data Implications 

The dataset analyzed consists of information on approximately 10,000 books, focusing on various performance metrics like ratings and accessibility on platforms such as Goodreads. It exhibits a strong positive correlation (0.995) between the total number of ratings and work-specific ratings, suggesting that books receiving more ratings tend to achieve greater popularity. Conversely, the weak negative correlation (-0.114) between average rating and the number of lower ratings indicates that high volume does not necessarily equate to high average satisfaction. Key features affecting performance include ratings at the four-star level, total work ratings, and three-star ratings, with respective importances highlighting their influence on a book’s success. The presence of notable outliers and a limited number of unique entries in some text columns, such as language codes and ISBNs, also signify the need for focused marketing strategies. In summary, while the correlation data and key features provide insights into reader engagement and book performance, the dataset also highlights potential areas for improvement in average satisfaction. This analysis suggests that while popularity (as indicated by ratings count) is essential, ensuring quality ratings is crucial for overall success in the competitive book market.

## Visualizations

![Cluster_visualization.png](/goodreads/Cluster_visualization.png)

![Column_Visualization_count.png](/goodreads/Column_Visualization_count.png)

![Column_Visualization_mean.png](/goodreads/Column_Visualization_mean.png)

![correlation_graph.png](/goodreads/correlation_graph.png)

![outlier_boxplots.png](/goodreads/outlier_boxplots.png)


