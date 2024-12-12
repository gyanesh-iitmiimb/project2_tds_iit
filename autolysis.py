# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "pandas",
#   "seaborn",
#   "python-dotenv",
#   "openai",
#   "matplotlib",
#   "numpy",
#   "scikit-learn",
#   "regex"
# ]
# ///
import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from dotenv import load_dotenv, find_dotenv
import os
from datetime import datetime, timedelta
import sys
load_dotenv(find_dotenv())
endpoint = "https://aiproxy.sanand.workers.dev/openai/"
api_key = os.getenv("OPENAI_API_KEY")
api_base = endpoint + "v1/chat/completions"
def get_flight_info(loc_origin, loc_destination):
    """Get flight information between two locations."""

    # Example output returned from an API or database
    flight_info = {
        "loc_origin": loc_origin,
        "loc_destination": loc_destination,
        "datetime": str(datetime.now() + timedelta(hours=2)),
        "airline": "KLM",
        "flight": "KL643",
    }

    return json.dumps(flight_info)


function_descriptions = [
    {
        "name": "get_flight_info",
        "description": "Get flight information between two locations",
        "parameters": {
            "type": "object",
            "properties": {
                "loc_origin": {
                    "type": "string",
                    "description": "The departure airport, e.g. DUS",
                },
                "loc_destination": {
                    "type": "string",
                    "description": "The destination airport, e.g. HAM",
                },
            },
            "required": ["loc_origin", "loc_destination"],
        },
    }
]
"""def chat_completion(api_key,api_base):
    headers = {"Content-Type": "application/json","Authorization": f"Bearer {api_key}"}
    response = requests.post(api_base, headers=headers, data=json.dumps({"model": "gpt-4o-mini",
                                                                         "messages": [{"role": "user", "content": "When's the next flight from Amsterdam to New York?"}],
                                                                         "functions": function_descriptions,
                                                                         "function_call": "auto"}))
    response.raise_for_status()
    return response.json()

completion = chat_completion(api_key,api_base)
output = completion.choices[0].message
chosen_function = eval(output.function_call.name)
flight = chosen_function(**params)
print(completion)"""
if len(sys.argv) != 2:
    print("Usage: python autolysis.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]


class DataAnalyzer:
    def __init__(self, dataframe_path=None):
        """
        Initialize a DataAnalyzer instance.

        Parameters
        ----------
        dataframe_path : str
            The path to the CSV file to be analyzed.

        Attributes
        ----------
        dataframe_path : str
            The path to the CSV file to be analyzed.
        date_cols : List[str]
            The columns that contain date data.
        link_cols : List[str]
            The columns that contain links.
        word_cols : List[str]
            The columns that contain word data.
        numeric_cols : List[str]
            The columns that contain numeric data.
        text_cols : List[str]
            The columns that contain text data.
        df : pandas.DataFrame
            The DataFrame object of the CSV file.
        """
        self.dataframe_path = dataframe_path
        self.date_cols = None
        self.link_cols = None
        self.sentence_cols = None
        self.numeric_cols = None
        self.text_cols = None
        self.filename = dataframe_path.split(".")[0]
        self.df = pd.read_csv(dataframe_path, encoding='utf-8', encoding_errors='ignore')

    def identify_link_or_word_columns(self):
        """
        Identify columns that contain links or words.

        Columns that contain links are identified by the presence of URLs.
        Columns that contain words are identified by the presence of at least one word
        with more than 4 letters.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This function updates the following instance variables:

        - link_cols: a list of column names that contain links
        - sentence_cols: a list of column names that contain sentences
        - text_cols: a list of column names that contain text data
        """
        link_cols = []
        sentence_cols = []
        text_cols = []
        col_list = self.df.select_dtypes(include=['object']).columns
        for col in col_list:
            if pd.api.types.is_object_dtype(self.df[col]):
                if self.df[col].astype(str).str.contains(r'https?://\S+|www\.\S+', regex=True, na=False).any():
                    link_cols.append(col)
                else:
                    word_counts = self.df[col].astype(str).apply(lambda x: len(re.findall(r'\b\w+\b', x)))
                    if (word_counts > 4).any():
                        sentence_cols.append(col)
                    else:
                        text_cols.append(col)

        self.link_cols = link_cols
        self.sentence_cols = sentence_cols
        self.text_cols = text_cols


    def identify_date_columns_and_create_timestamp(self):
        """
        Identify date columns and create a timestamp column.

        Columns that contain date information are identified by the presence of
        datetime objects in the column or by the presence of certain keywords in
        the column name.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This function updates the following instance variables:

        - date_cols: a list of column names that contain date information
        - timestamp: a datetime column created from the date columns
        """
        date_cols = []
        for col in self.df.columns:
            try:
                    if col in self.df.select_dtypes(include=["object"]).columns:
                        self.df['timestamp'] = pd.to_datetime(self.df[col])
                        date_cols.append(col)
                    else:
                        if any(keyword in col.lower() for keyword in ['date', 'month', 'year', 'time', "hours", "minutes", 'timestamp']):
                            date_cols.append(col)

            except ValueError:
                if any(keyword in col.lower() for keyword in ['date', 'month', 'year', 'time', "hours","minutes",'timestamp']):
                    date_cols.append(col)


        self.date_cols = date_cols

    def numerical_cols_analyze_correlations(self):
        """
        Analyze the correlations between numerical columns.

        The correlations between all numerical columns are calculated using
        the Pearson correlation coefficient. The maximum and minimum correlations
        are then returned.

        Returns
        -------
        tuple:
            A tuple containing the maximum and minimum correlations, as well as
            the columns on which they are found.
        """
        self.numeric_cols = set(self.df.select_dtypes(exclude=['object']).columns) - set(self.date_cols)- {'timestamp'}
        self.numeric_cols = list(self.numeric_cols)
        self.numeric_cols = [col for col in self.numeric_cols if "_id" not in col.lower()]
        try:
            corr_matrix = self.df[self.numeric_cols].dropna().corr(method='pearson')
            corr_matrix_mask = np.eye(corr_matrix.shape[0], dtype=bool)
            corr_matrix.mask(corr_matrix_mask, inplace=True)
            max_corr = corr_matrix.unstack().sort_values(ascending=False)
            min_corr = corr_matrix.unstack().sort_values(ascending=True)
            max_corr_columns = max_corr.index[0]
            min_corr_column = min_corr.index[0]
            return (f"The maximum correlations is found between columns {max_corr_columns[0]} and {max_corr_columns[1]} with a value of {max_corr.iloc[0]}."
                    f"The minimum correlation is between columns {min_corr_column[0]} and {min_corr_column[1]} with a value of {min_corr.iloc[0]}",
                    max_corr_columns[0],max_corr_columns[1],min_corr_column[0],min_corr_column[1])
        except Exception  as e:
            return ("No Relevant Numerical Column Found")

    def numerical_cols_analyze_outliers(self):
        """
        Analyze numerical columns for outliers.

        This function calculates the interquartile range (IQR) for each numerical column
        and identifies any data points that fall outside the IQR bounds as outliers.

        Returns
        -------
        tuple:
            A tuple containing a message indicating the presence of outliers and a dictionary
            where keys are column names and values are the count of outliers in that column.
            If no outliers are found, a message indicating no outliers is returned.
        """
        try:
            outliers_dict = {}
            for col in self.numeric_cols:
                q1 = self.df[col].quantile(0.25)
                q3 = self.df[col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                outliers = self.df[(self.df[col] < lower_bound) | (self.df[col] > upper_bound)]
                if len(outliers) > 0:
                    outliers_dict[col] = len(outliers)
            if outliers_dict:
                return (f"Outliers found in column {outliers_dict}",outliers_dict)
            else:
                return ("No Outliers Found")
        except Exception as e:
            return ("No Relevant Numerical Column Found")

    def numerical_cols_analyze_cluster(self):
        try:
            df = self.df[self.numeric_cols]
            sil_score = []
            max_score = 0
            max_cluster_num = 0
            df = pd.DataFrame(SimpleImputer().fit_transform(df), columns=df.columns)
            df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns)
            for i in range(3,11):
                kmeans = KMeans(n_clusters=i, random_state=42)
                kmeans.fit(df)
                if max_score < silhouette_score(df, kmeans.labels_):
                    max_score = silhouette_score(df, kmeans.labels_)
                    max_cluster_num = i
            kmeans = KMeans(n_clusters=max_cluster_num, random_state=42)
            kmeans.fit(df)
            labels = kmeans.labels_
            df['cluster'] = labels
            y=df['cluster']
            x=df[self.numeric_cols]
            rf= RandomForestRegressor()
            rf.fit(x,y)
            rf.feature_importances_
            feature_importances = pd.DataFrame(rf.feature_importances_, index=x.columns, columns=['importance']).sort_values('importance', ascending=False)
            return (f"The most important features are {feature_importances.index[0]}, {feature_importances.index[1]} and {feature_importances.index[2]} with "
                    f"feature importances of {feature_importances.iloc[0]}, {feature_importances.iloc[1]} and {feature_importances.iloc[2]} respectively",
                    df,feature_importances.index[0],feature_importances.index[1])
        except Exception as e:
            return ("No Relevant Numerical Column Found")

    def text_word_analyzer(self):
        if self.text_cols:
            text_cols_nunique = {col:self.df[col].nunique() for col in self.text_cols}
            df= pd.DataFrame(text_cols_nunique.items(), columns=['Column Name', 'Number of Unique Words'])
            df.sort_values(by='Number of Unique Words', ascending=True, inplace=True)
            return (f"The number of unique elements in text columns are {df}",df.iloc[0,0])
        else:
            return ("No Text Columns Found",[])


    def create_visualisations(self):
        c=0
        if self.numerical_cols_analyze_correlations() != "No Relevant Numerical Column Found":
            max_1 = self.numerical_cols_analyze_correlations()[1]
            max_2 = self.numerical_cols_analyze_correlations()[2]
            min_1 = self.numerical_cols_analyze_correlations()[3]
            min_2 = self.numerical_cols_analyze_correlations()[4]
            df = self.df[self.numeric_cols]
            df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns)
            if  not os.path.exists(self.filename):
                os.mkdir(self.filename)
            plt.figure(figsize=(512/96, 512/96),dpi=96)
            sns.scatterplot(x=max_1, y=max_2, data=df, color="red",alpha=0.5)
            sns.scatterplot(x=min_1, y=min_2, data=df, color="blue",alpha=0.5)
            plt.title("Correlation Graph For Scaled Variables")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.tight_layout(pad=0)
            plt.legend([f"Maximum Correlation between {max_1} and {max_2}", f"Minimum Correlation between {min_1} and {min_2}"],
                       fontsize=6)
            plt.savefig(f"{self.filename}/correlation_graph.png",dpi=96,bbox_inches='tight',pad_inches=0)
            c=c+1

        if (self.numerical_cols_analyze_outliers() != "No Relevant Numerical Column Found") and (
            self.numerical_cols_analyze_outliers() != "No Outliers Found"):
            outliers_dict = self.numerical_cols_analyze_outliers()[1]
            if len(outliers_dict)>=3:
                top_3_keys = sorted(outliers_dict, key=outliers_dict.get, reverse=True)[:3]
            else:
                top_3_keys = outliers_dict.keys()
            df = self.df[top_3_keys]
            if  not os.path.exists(self.filename):
                os.mkdir(self.filename)
            df.plot(kind='box',subplots=True,figsize=(512/96, 512/96))
            plt.title('Boxplots of Outliers')
            plt.tight_layout(pad=0)
            plt.savefig(os.path.join(self.filename, 'outlier_boxplots.png'), bbox_inches='tight', pad_inches=0,dpi=96)
            c=c+1
        if self.numerical_cols_analyze_cluster() != "No Relevant Numerical Column Found":
            try:
                if  not os.path.exists(self.filename):
                    os.mkdir(self.filename)
                df = self.numerical_cols_analyze_cluster()[1]
                important_feature1 = self.numerical_cols_analyze_cluster()[2]
                important_feature2 = self.numerical_cols_analyze_cluster()[3]
                X = df[self.numeric_cols]
                y = df['cluster']
                X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
                if len(X.columns) <= 3:
                    plt.figure(figsize=(512 / 96, 512 / 96), dpi=96)
                    plt.scatter(X[important_feature1], X[important_feature2], c=y, cmap='tab20',alpha=0.4)
                    plt.xlabel(important_feature1)
                    plt.ylabel(important_feature2)
                    plt.title('Visualizing Clusters in 2 Dimensions')
                    plt.tight_layout(pad=0)
                    plt.savefig(os.path.join(self.filename, 'Cluster_visualization.png'), bbox_inches='tight', pad_inches=0,dpi=96)
                    c=c+1
                else:
                    lda = LinearDiscriminantAnalysis(n_components=2)
                    lda.fit(X, y)
                    X_lda = lda.transform(X)
                    plt.figure(figsize=(512 / 96, 512 / 96), dpi=96)
                    plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='tab20',alpha=0.4)
                    plt.xlabel('Component 1')
                    plt.ylabel('Component 2')
                    plt.title('Visualizing Clusters in 2 Dimensions')
                    plt.tight_layout(pad=0)
                    plt.savefig(os.path.join(self.filename, 'Cluster_visualization.png'), bbox_inches='tight', pad_inches=0,dpi=96)
                    c=c+1
            except Exception as e:
                print ("No Relevant Clustering Analysis can be done on less than 2 numerical columns")

        if self.text_word_analyzer()[1]:
            important_feature1 = self.numerical_cols_analyze_cluster()[2]
            column_comparison = self.text_word_analyzer()[1]
            df = self.df[[important_feature1,column_comparison]]
            df.loc[:, important_feature1] = df.loc[:, important_feature1].fillna(df.loc[:, important_feature1].mean())
            df.loc[:, column_comparison] = df.loc[:, column_comparison].fillna(df.loc[:, column_comparison].mode()[0])
            plt.figure(figsize=(512 / 96, 512 / 96), dpi=96)
            plt.tight_layout(pad=0)
            df.groupby(column_comparison).mean().plot(kind="bar")
            plt.savefig(os.path.join(self.filename, 'Column_Visualization_mean.png'), bbox_inches='tight', pad_inches=0,dpi=96)
            c=c+1

        if self.text_word_analyzer()[1]:
            important_feature1 = self.numerical_cols_analyze_cluster()[2]
            column_comparison = self.text_word_analyzer()[1]
            df = self.df[[important_feature1,column_comparison]]
            df.loc[:, important_feature1] = df.loc[:, important_feature1].fillna(df.loc[:, important_feature1].mean())
            df.loc[:, column_comparison] = df.loc[:, column_comparison].fillna(df.loc[:, column_comparison].mode()[0])
            plt.figure(figsize=(512 / 96, 512 / 96), dpi=96)
            plt.tight_layout(pad=0)
            df.groupby(column_comparison).count().plot(kind="bar")
            plt.savefig(os.path.join(self.filename, 'Column_Visualization_count.png'), bbox_inches='tight', pad_inches=0,dpi=96)
            c=c+1


df = DataAnalyzer(file_path)
df.identify_link_or_word_columns()
df.identify_date_columns_and_create_timestamp()
df.numerical_cols_analyze_correlations()
df.numerical_cols_analyze_outliers()
df.numerical_cols_analyze_cluster()
df.text_word_analyzer()
df.create_visualisations()
