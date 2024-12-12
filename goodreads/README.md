# Report

## Data Description 
 
The report contains a dataset with 10,000 rows related to books, featuring various attributes such as book IDs, ISBNs, and ratings. It includes counts of ratings across different star levels (2 to 5 stars), as well as links to images of the books. The data is structured in multiple columns to provide insights into book popularity and reader feedback.
 
## Numerical Columns

The maximum correlations is found between columns work_ratings_count and ratings_count with a value of 0.9950949109767664.The minimum correlation is between columns average_rating and ratings_2 with a value of -0.11433083463802127

Outliers found in column {'work_ratings_count': 1143, 'isbn13': 556, 'ratings_3': 1149, 'ratings_4': 1131, 'ratings_count': 1163, 'average_rating': 158, 'ratings_2': 1156, 'ratings_1': 1140, 'ratings_5': 1158, 'books_count': 844, 'work_text_reviews_count': 1005}

The most important features are ratings_4, work_ratings_count and ratings_3 with feature importances of importance    0.503429
Name: ratings_4, dtype: float64, importance    0.328373
Name: work_ratings_count, dtype: float64 and importance    0.048783
Name: ratings_3, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are      Column Name  Number of Unique Words
1  language_code                      25
0           isbn                    9300

## Data Analysis 

The dataset reveals a strong correlation (0.995) between work_ratings_count and ratings_count, while the weakest correlation (-0.114) is between average_rating and ratings_2. Key features include ratings_4, work_ratings_count, and ratings_3. Additionally, several outliers are identified across multiple columns, and the text columns reveal 25 unique language codes and 9,300 unique ISBNs.
 
## Data Insights 

The dataset provides a rich insight into book popularity, evidenced by the strong correlation between work ratings count and ratings count, suggesting that more frequently rated books tend to also be highly rated. However, the low correlation between average rating and 2-star ratings indicates that low ratings may not significantly impact overall book perception. The presence of 9,300 unique ISBNs highlights a diverse range, while the identification of outliers suggests opportunities for further investigation into exceptional books or rating behaviors.
 
## Data Implications 

The dataset comprising 10,000 book entries offers significant insights into reader preferences and ratings dynamics by encapsulating attributes like book IDs, ISBNs, and rating counts. Notably, a strong correlation (0.995) between work ratings count and total ratings hints at a trend where books that accumulate more ratings also achieve higher scores, indicating greater popularity. Conversely, the negligible correlation (-0.114) between average ratings and two-star ratings uncovers a disconnect, suggesting that a subset of poor ratings may not dramatically alter the book's perceived quality. This could reflect a resilience in some works where criticisms do not overshadow overall appreciation. 

The dataset further highlights diversity with 25 language codes and 9,300 unique ISBNs. Identifying several outliers in ratings presents an avenue for deeper analysis into what distinguishes these books, whether due to unique content, thematic resonance, or reader engagement strategies. Such findings are vital for authors and publishers aiming to understand market dynamics and reader behavior, emphasizing the importance of reader ratings in shaping book reputation and sales potential.

## Visualizations

![Cluster_visualization.png](/goodreads/Cluster_visualization.png)

![Column_Visualization_count.png](/goodreads/Column_Visualization_count.png)

![Column_Visualization_mean.png](/goodreads/Column_Visualization_mean.png)

![correlation_graph.png](/goodreads/correlation_graph.png)

![outlier_boxplots.png](/goodreads/outlier_boxplots.png)


