# Report

## Data Description 
 
The data in this report comprises a dataset with 10,000 rows, detailing various attributes of books, including identifiers such as book_id and goodreads_book_id, as well as physical details like ISBN and book counts. It also includes user ratings across different scales (1 to 5 stars) and URL links to book images, providing a comprehensive overview for analysis within a book collection or a reading platform.
 
## Numerical Columns

The maximum correlations is found between columns ratings_count and work_ratings_count with a value of 0.9950949109767664.The minimum correlation is between columns average_rating and ratings_2 with a value of -0.11433083463802127

Outliers found in column {'ratings_5': 1158, 'ratings_count': 1163, 'books_count': 844, 'isbn13': 556, 'ratings_1': 1140, 'ratings_3': 1149, 'work_ratings_count': 1143, 'ratings_2': 1156, 'ratings_4': 1131, 'work_text_reviews_count': 1005, 'average_rating': 158}

The most important features are ratings_4, work_ratings_count and books_count with feature importances of importance    0.471013
Name: ratings_4, dtype: float64, importance    0.391355
Name: work_ratings_count, dtype: float64 and importance    0.045832
Name: books_count, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are      Column Name  Number of Unique Words
1  language_code                      25
0           isbn                    9300

## Data Analysis 

The dataset shows a strong correlation of 0.995 between ratings_count and work_ratings_count, while the weakest correlation is -0.114 between average_rating and ratings_2. Key features identified include ratings_4, work_ratings_count, and ratings_3, with respective importances of 0.419, 0.397, and 0.068. Additionally, several outliers are present in columns like ratings_5 and average_rating, and the text columns have varying unique element counts, with 25 unique language codes and 9300 unique ISBNs.
 
## Data Insights 

The dataset offers a rich landscape for exploring book popularity, with ratings_4 and work_ratings_count being key indicators of a book's reception. The strong correlation between ratings_count and work_ratings_count suggests that a higher count of reviews directly enhances a book's visibility and perceived quality. However, the presence of outliers in ratings_5 may indicate that some books are exceptionally well-received, warranting further investigation into what distinguishes them from the rest.
 
## Data Implications 

The dataset under analysis represents a broad collection of books, totaling 10,000 entries, featuring attributes such as identifiers, user ratings, and physical details. Notably, a strong correlation of 0.995 between ratings_count and work_ratings_count indicates that a higher volume of reviews correlates strongly with increased visibility and improved perceived quality of a book. The analysis identifies key features, with ratings_4 and work_ratings_count emerging as significant factors in determining a book's reception, reflected in their respective importances of 0.419 and 0.397. However, outliers observed in the ratings_5 column suggest a subset of books that are exceptionally well-received, prompting a need to explore what specifically contributes to their distinction from other works. Furthermore, with 9300 unique ISBNs and a varied distribution of language codes, the dataset provides ample opportunity for deeper exploration into trends in book popularity and user engagement across different demographics. Overall, the findings point towards a complex interplay of factors influencing book ratings, emphasizing the importance of high review counts and the intriguing outliers that merit further qualitative examination.

## Visualizations

![Cluster_visualization.png](/goodreads/Cluster_visualization.png)

![Column_Visualization_count.png](/goodreads/Column_Visualization_count.png)

![Column_Visualization_mean.png](/goodreads/Column_Visualization_mean.png)

![correlation_graph.png](/goodreads/correlation_graph.png)

![outlier_boxplots.png](/goodreads/outlier_boxplots.png)


