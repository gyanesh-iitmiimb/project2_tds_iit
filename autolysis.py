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
#   "regex",
#   "python-signal"
# ]
# ///
import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from dotenv import load_dotenv, find_dotenv
import os
import sys
import base64



class DataAnalyzer:
    """
    DataAnalyzer is a class for analyzing CSV files and generating insights and visualizations.

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
    numeric_cols : List[str]
        The columns that contain numeric data.
    text_cols : List[str]
        The columns that contain text data.
    df : pandas.DataFrame
        The DataFrame object of the CSV file.
    """

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
        self.important_feature1 = None
        self.important_feature2 = None
        self.important_feature3 = None

    def identify_link_or_word_columns(self):
        """
        Identify columns that contain links or words.

        Columns that contain links are identified by the presence of URLs.
        Columns that contain words are identified by the presence of at least one word
        with more than 4 letters.

        Parameters
        ----------


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
        pass
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
        pass
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
        pass
        if self.date_cols:
            self.numeric_cols = set(self.df.select_dtypes(exclude=['object']).columns) - set(self.date_cols)- {'timestamp'}
        else:
            self.numeric_cols = set(self.df.select_dtypes(exclude=['object']).columns) - {'timestamp'}
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
        pass
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
        """
        Analyze numerical columns for clustering.

        This function uses the k-means clustering algorithm to identify clusters
        in the numerical columns. The silhouette score is used to evaluate the
        quality of the clustering. The feature importances of the clusters are
        then calculated using a random forest regressor and the most important
        features are returned.

        Returns
        -------
        tuple:
            A tuple containing a message indicating the most important features
            and a DataFrame containing the cluster labels. If no relevant numerical
            columns are found, a message indicating no relevant columns is returned.
        """
        try:
            df = self.df[self.numeric_cols]
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
            rf= RandomForestClassifier(n_estimators=30, random_state=42)
            rf.fit(x,y)
            feature_importances = pd.DataFrame(rf.feature_importances_, index=x.columns, columns=['importance']).sort_values('importance', ascending=False)
            self.important_feature1 = feature_importances.index[0]
            self.important_feature2 = feature_importances.index[1]
            return (f"The most important features are {feature_importances.index[0]}, {feature_importances.index[1]} and {feature_importances.index[2]} with "
                    f"feature importances of {feature_importances.iloc[0]}, {feature_importances.iloc[1]} and {feature_importances.iloc[2]} respectively",
                    df)
        except Exception as e:
            return ("No Relevant Numerical Column Found")

    def text_word_analyzer(self):
        """
        Analyze text columns by counting the number of unique words in each column.

        Parameters
        ----------
        None


        Returns
        -------
        tuple:
            A tuple containing a message and a DataFrame with the column names
            and the number of unique words in each column. If no text columns are
            found, a message indicating no text columns is returned.
        """
        if self.text_cols:
            text_cols_nunique = {col:self.df[col].nunique() for col in self.text_cols}
            df= pd.DataFrame(text_cols_nunique.items(), columns=['Column Name', 'Number of Unique Words'])
            df.sort_values(by='Number of Unique Words', ascending=True, inplace=True)
            return (f"The number of unique elements in text columns are {df}",df.iloc[0,0])
        else:
            return ("No Text Columns Found",[])

    def create_correlation_plot(self):
        """
        Creates correlations for the data in the specified file path.

        The plots is saved in the specified file path.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.numerical_cols_analyze_correlations() != "No Relevant Numerical Column Found":
            max_1 = self.numerical_cols_analyze_correlations()[1]
            max_2 = self.numerical_cols_analyze_correlations()[2]
            min_1 = self.numerical_cols_analyze_correlations()[3]
            min_2 = self.numerical_cols_analyze_correlations()[4]
            df = self.df[self.numeric_cols]
            df = pd.DataFrame(StandardScaler().fit_transform(df), columns=df.columns)
            if not os.path.exists(self.filename):
                os.mkdir(self.filename)
            plt.figure(figsize=(350 / 96, 350 / 96), dpi=96)
            sns.scatterplot(x=max_1, y=max_2, data=df, color="red", alpha=0.5)
            sns.scatterplot(x=min_1, y=min_2, data=df, color="blue", alpha=0.5)
            plt.title("Correlation Graph For Scaled Variables")
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.tight_layout(pad=0)
            plt.legend([f"Maximum Correlation between {max_1} and {max_2}",
                        f"Minimum Correlation between {min_1} and {min_2}"],
                       fontsize=6)
            plt.savefig(f"{self.filename}/correlation_graph.png", dpi=96, bbox_inches='tight', pad_inches=0)

    def create_boxplots(self):
        """
        Creates boxplots for the data in the specified file path.

        The plots are saved in the specified file path.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if (self.numerical_cols_analyze_outliers() != "No Relevant Numerical Column Found") and (
                self.numerical_cols_analyze_outliers() != "No Outliers Found"):
            outliers_dict = self.numerical_cols_analyze_outliers()[1]
            if len(outliers_dict) >= 3:
                top_3_keys = sorted(outliers_dict, key=outliers_dict.get, reverse=True)[:3]
            else:
                top_3_keys = outliers_dict.keys()
            df = self.df[top_3_keys]
            if not os.path.exists(self.filename):
                os.mkdir(self.filename)
            df.plot(kind='box', subplots=True, figsize=(350 / 96, 350 / 96))
            plt.title('Boxplots of Outliers')
            plt.tight_layout(pad=0)
            plt.savefig(os.path.join(self.filename, 'outlier_boxplots.png'), bbox_inches='tight', pad_inches=0, dpi=96)

    def cluster_visualizer(self):
        """
        Creates a scatter plot of clusters in 2 dimensions.

        The clusters are obtained by performing k-means clustering on the data
        in the specified file path. The clusters are then visualized in 2
        dimensions by using either a linear discriminant analysis (LDA) or by
        plotting the two most important features.

        The plot is saved in the specified file path.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.numerical_cols_analyze_cluster() != "No Relevant Numerical Column Found":
            try:
                if  not os.path.exists(self.filename):
                    os.mkdir(self.filename)
                df = self.numerical_cols_analyze_cluster()[1]
                important_feature1 = self.important_feature1
                important_feature2 = self.important_feature2
                X = df[self.numeric_cols]
                y = df['cluster']
                X = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
                if len(X.columns) <= 3:
                    plt.figure(figsize=(350 / 96, 350 / 96), dpi=96)
                    plt.scatter(X[important_feature1], X[important_feature2], c=y, cmap='tab20',alpha=0.4)
                    plt.xlabel(important_feature1)
                    plt.ylabel(important_feature2)
                    plt.title('Visualizing Clusters in 2 Dimensions')
                    plt.tight_layout(pad=0)
                    plt.savefig(os.path.join(self.filename, 'Cluster_visualization.png'), bbox_inches='tight', pad_inches=0,dpi=96)

                else:
                    lda = LinearDiscriminantAnalysis(n_components=2)
                    lda.fit(X, y)
                    X_lda = lda.transform(X)
                    plt.figure(figsize=(350 / 96, 350 / 96), dpi=96)
                    plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='tab20',alpha=0.4)
                    plt.xlabel('Component 1')
                    plt.ylabel('Component 2')
                    plt.title('Visualizing Clusters in 2 Dimensions')
                    plt.tight_layout(pad=0)
                    plt.savefig(os.path.join(self.filename, 'Cluster_visualization.png'), bbox_inches='tight', pad_inches=0,dpi=96)

            except Exception as e:
                print ("No Relevant Clustering Analysis can be done on less than 2 numerical columns")

    def text_word_analyzer_plot_mean(self):
        """
        Plot the mean of a numerical column grouped by a categorical column.

        The categorical column is the one with the most number of unique words,
        and the numerical column is the one with the highest correlation with
        the categorical column.

        The plot is saved in the specified file path.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.text_word_analyzer()[1] and self.important_feature1:
            important_feature1 = self.important_feature1
            column_comparison = self.text_word_analyzer()[1]
            df = self.df[[important_feature1,column_comparison]]
            df.loc[:, important_feature1] = df.loc[:, important_feature1].fillna(df.loc[:, important_feature1].mean())
            df.loc[:, column_comparison] = df.loc[:, column_comparison].fillna(df.loc[:, column_comparison].mode()[0])
            plt.figure(figsize=(350 / 96, 350 / 96), dpi=96)
            plt.tight_layout(pad=0)
            df.groupby(column_comparison).mean().plot(kind="bar")
            plt.savefig(os.path.join(self.filename, 'Column_Visualization_mean.png'), bbox_inches='tight', pad_inches=0,dpi=96)

    def text_word_analyzer_plot_count(self):
        """
        Plot the count of a numerical column grouped by a categorical column.

        The categorical column is the one with the most number of unique words,
        and the numerical column is the one with the highest correlation with
        the categorical column.

        The plot is saved in the specified file path.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.text_word_analyzer()[1] and self.important_feature1:
            important_feature1 = self.important_feature1
            column_comparison = self.text_word_analyzer()[1]
            df = self.df[[important_feature1,column_comparison]]
            df.loc[:, important_feature1] = df.loc[:, important_feature1].fillna(df.loc[:, important_feature1].mean())
            df.loc[:, column_comparison] = df.loc[:, column_comparison].fillna(df.loc[:, column_comparison].mode()[0])
            plt.figure(figsize=(350 / 96, 350 / 96), dpi=96)
            plt.tight_layout(pad=0)
            df.groupby(column_comparison).count().plot(kind="bar")
            plt.savefig(os.path.join(self.filename, 'Column_Visualization_count.png'), bbox_inches='tight', pad_inches=0,dpi=96)




class DataAnalyzerMarkdown(DataAnalyzer):
    """
    Initialize a DataAnalyzerMarkdown instance.

    Parameters
    ----------
    file_path : str
        The path to the CSV file to be analyzed.
    api_base : str
        The base URL of the OpenAI API.
    api_key : str
        The OpenAI API key.

    Attributes
    ----------
    md_filename : str
        The path to the Markdown file to be written.
    api_base : str
        The base URL of the OpenAI API.
    api_key : str
        The OpenAI API key.
    """
    def __init__(self, file_path, api_base, api_key):
        """
        Initialize a DataAnalyzerMarkdown instance.

        Parameters
        ----------
        file_path : str
            The path to the CSV file to be analyzed.
        api_base : str
            The base URL of the OpenAI API.
        api_key : str
            The OpenAI API key.

        Attributes
        ----------
        md_filename : str
            The path to the Markdown file to be written.
        api_base : str
            The base URL of the OpenAI API.
        api_key : str
            The OpenAI API key.
        """
        super().__init__(file_path)
        self.md_filename = os.path.join(self.filename, 'README.md')
        self.api_base = api_base
        self.api_key = api_key
        self.identify_date_columns_and_create_timestamp()
        self.identify_link_or_word_columns()
        self.corr = self.numerical_cols_analyze_correlations()[0]
        self.outliers = self.numerical_cols_analyze_outliers()[0]
        self.cluster = self.numerical_cols_analyze_cluster()[0]
        self.word_analyzer = self.text_word_analyzer()[0]
        self.create_correlation_plot()
        self.create_boxplots()
        self.cluster_visualizer()
        self.text_word_analyzer_plot_mean()
        self.text_word_analyzer_plot_count()

    def chat_completion(self, content, context):
        """
        Make a request to the OpenAI API to generate a completion based on the content and context.

        Parameters
        ----------
        content : str
            The content to be completed.
        context : str
            The context to be used for generating the completion.

        Returns
        -------
        str
            The generated completion.
        """
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}
        response = requests.post(self.api_base, headers=headers,
                                 data=json.dumps({"model": "gpt-4o-mini",
                                                  "messages": [{"role":"system","content":f"{context}"},
                                                      {"role": "user","content": f"{content}"}]}))
        response.raise_for_status()
        messages = response.json()

        return messages["choices"][0]["message"]["content"]

    def brief_data_description(self):
        """
        Generate a brief description of the data in this report.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A brief description of the data in 2-3 sentences.
        """
        self.data_desc = self.chat_completion(context="Briefly describe the data in this report. Be precise in 2-3 sentences. Give a generalised answer the data passed is just an example subset"
                                            f"be generic in your answer, as data contains {len(self.df)} rows",
                                    content=f"{self.df.head(1)}")
        return self.data_desc

    def explain_data_analysis(self):
        """
        Summarize the data analysis in 2-3 lines.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A summary of the data analysis in 2-3 lines.
        """
        self.data_analysis = self.chat_completion(context= "You are given few sentences about the data set, summarise those in 2 to 3 lines.",
                                    content = (f"{self.corr} " +
                                                        f"{self.cluster} " +
                                                        f"{self.outliers} " +
                                                        f"{self.word_analyzer}"))
        return self.data_analysis

    def explain_data_insights(self):
        """
        Generate insights from the data and data analysis in 2-3 lines.

        Parameters
        ----------
        None

        Returns
        -------
        str
            Insights from the data and data analysis in 2-3 lines.
        """
        self.data_insight = self.chat_completion(context= "You are a good data scientist, given few summaries of the data and data analysis. Generate dood insights"
                                             "in about two to three lines",
                                    content = (f"{self.data_desc}" + " " + f"{self.data_analysis}" ))
        return self.data_insight

    def analyze_implications_with_images(self):
        """
        Analyze text and images to identify key implications.

        Parameters
        ----------
        None
        Returns
        -------
        str
            The generated insights from the text and images.
        """
        text = ""
        image_paths = [os.path.join(self.filename,file) for file in os.listdir(self.filename) if file.endswith('.png')]
        # Convert images to base64 strings
        content = ""
        images_base64 = [self.convert_image_to_base64(image_path) for image_path in image_paths]

        # Combine text with image data
        content = f"{text}\n\n{' '.join(images_base64)}"

        content = f"images:{content}" + " " +self.data_desc + " " + self.data_analysis + " " +self.data_insight


        # Use chat_completion to analyze implications
        try:
            signal.alarm(80)
            return self.chat_completion(
                context="You are a data scientist. Analyze the given text and images to identify key implications."
                        "Be crisp and deliver a short paragraph, try to contain under 300 words",
                content=content
            )
        except Exception as e:
            return self.chat_completion(context="You are a data scientist. Analyze the given text and images to identify key implications."
                        "Be crisp and deliver a short paragraph, try to contain under 300 words",
                content=self.data_desc + " " + self.data_analysis + " " +self.data_insight
            )
        finally:
            signal.alarm(0)

    def convert_image_to_base64(self, image_path):
        """
        Convert an image file to a base64 encoded string.

        Parameters
        ----------
        image_path : str
            The path to the image file.

        Returns
        -------
        str
            The base64 encoded string of the image.
        """
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")




    def write_report_md(self):
        """
        Write the report to a markdown file.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        with open(self.md_filename, 'w') as f:
            f.write('# Report\n\n')
            f.write('## Data Description \n \n')
            f.write(self.brief_data_description() + '\n \n')
            f.write('## Numerical Columns\n\n')
            f.write(self.corr + '\n\n')
            f.write(self.outliers + '\n\n')
            f.write(self.cluster + '\n\n')
            f.write('## Text Columns\n\n')
            f.write(self.word_analyzer + '\n\n')
            f.write ('## Data Analysis \n\n')
            f.write (self.explain_data_analysis() + '\n \n')
            f.write ('## Data Insights \n\n')
            f.write (self.explain_data_insights() + '\n \n')
            f.write ('## Data Implications \n\n')
            f.write (self.analyze_implications_with_images() + '\n\n')
            f.write('## Visualizations\n\n')
            image_files = [file for file in os.listdir(self.filename) if file.endswith('.png')]
            for image_file in image_files:
                image_path = os.path.join(self.filename, image_file)
                if os.path.exists(image_path):
                    f.write(f'![{image_file}](/{self.filename}/{image_file})' +'\n\n')
            f.write('\n')
            f.close()
load_dotenv(find_dotenv())
endpoint = "https://aiproxy.sanand.workers.dev/openai/"
api_key = os.getenv("OPENAI_API_KEY")
api_base = endpoint + "v1/chat/completions"

if len(sys.argv) != 2:
    print("Usage: python autolysis.py <file_path>")
    sys.exit(1)
file_path = sys.argv[1]
md = DataAnalyzerMarkdown(file_path = file_path,api_base =api_base, api_key=api_key)
md.write_report_md()