# Report

## Data Description 
 
The report contains a dataset of book-related information, encompassing 10,000 rows with various attributes such as book IDs, ratings, and image URLs. Each entry provides details about individual books, including their Goodreads IDs, ISBN numbers, total ratings across different score levels, and corresponding image links for both small and large formats. The dataset appears to be structured to facilitate analysis of book popularity and reader ratings.
 
## Numerical Columns

The maximum correlations is found between columns ratings_count and work_ratings_count with a value of 0.9950949109767664.The minimum correlation is between columns ratings_2 and average_rating with a value of -0.11433083463802127

Outliers found in column {'isbn13': 556, 'work_text_reviews_count': 1005, 'work_ratings_count': 1143, 'ratings_2': 1156, 'ratings_count': 1163, 'books_count': 844, 'ratings_1': 1140, 'ratings_4': 1131, 'ratings_3': 1149, 'ratings_5': 1158, 'average_rating': 158}

The most important features are work_ratings_count, ratings_4 and ratings_3 with feature importances of importance    0.460323
Name: work_ratings_count, dtype: float64, importance    0.364784
Name: ratings_4, dtype: float64 and importance    0.059092
Name: ratings_3, dtype: float64 respectively

## Text Columns

The number of unique elements in text columns are      Column Name  Number of Unique Words
1  language_code                      25
0           isbn                    9300

## Data Analysis 

The dataset shows a high correlation (0.995) between ratings_count and work_ratings_count, while the lowest correlation (-0.114) is between ratings_2 and average_rating. Key features identified include work_ratings_count and ratings_4, with significant importances of 0.4288 and 0.4257, respectively. Additionally, outliers were detected in multiple columns, and the text columns have 25 unique language codes and 9,300 unique ISBNs.
 
## Data Insights 

This dataset presents a rich avenue for exploring book popularity, particularly through its high correlation between ratings_count and work_ratings_count, indicating that books with more ratings tend to receive higher overall ratings. The notable outliers may suggest a need for quality checks or highlight particularly exceptional or poorly received titles, while the uniqueness of languages and ISBNs offers potential for further segmentation and market analysis.
 
## Data Implications 

The provided dataset of 10,000 books includes key attributes such as book IDs, ratings, and images, allowing for insights into book popularity and reader engagement. The high correlation (0.995) between ratings_count and work_ratings_count suggests that books receiving numerous ratings generally attain higher overall ratings, indicating community validation. Conversely, the negative correlation (-0.114) between ratings_2 and average_rating points to potential distinctions in reader experiences or preferences that could warrant further investigation. Significant features like work_ratings_count and ratings_4 highlight trends in reader feedback. Additionally, the presence of 25 unique language codes and 9,300 unique ISBNs implies potential for in-depth market segmentation. Outliers in ratings could either indicate data quality issues or signify exceptional works. Overall, this dataset offers extensive opportunities for analysis, which could enhance understanding of consumer behavior in the book market.

## Visualizations

![Cluster_visualization.png](/goodreads\Cluster_visualization.png)

![Column_Visualization_count.png](/goodreads\Column_Visualization_count.png)

![Column_Visualization_mean.png](/goodreads\Column_Visualization_mean.png)

![correlation_graph.png](/goodreads\correlation_graph.png)

![outlier_boxplots.png](/goodreads\outlier_boxplots.png)


