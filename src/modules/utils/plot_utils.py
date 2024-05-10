import matplotlib.pyplot as plt
import math
import seaborn as sns
import polars as pl

def plot_correlation_matrix(corr_matrix: pl.DataFrame, title: str='Correlation Matrix Heatmap'):
    plt.figure(figsize=(15, 12))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

def plot_histogram(features: list[str], data: pl.DataFrame):
    sns.set(style="whitegrid")
    num_features = len(features)
    num_rows = math.ceil(num_features / 3)  # Calculate the number of rows needed
    plt.figure(figsize=(25, 5 * num_rows))  # Adjust height based on number of rows

    list(map(lambda idx_feature: (
        plt.subplot(num_rows, 3, idx_feature[0] + 1),
        sns.histplot(data[idx_feature[1]], kde=True, color='blue'),
        plt.title(f'Distribution of {idx_feature[1]}'),
        plt.xlabel(idx_feature[1]),
        plt.ylabel('Frequency')
    ), enumerate(features)))

    plt.tight_layout()
    plt.show()


def plot_bar_chart(features: list[str], data: list[str]):
    # Determine the size of the grid
    num_features = len(features)
    cols = 2  # Number of columns in subplot grid
    rows = math.ceil(num_features / cols)  # Number of rows in subplot grid

    plt.figure(figsize=(20, 10))
    sns.set(style="whitegrid")
    list(map(lambda idx_feature: (
        plt.subplot(rows, cols, idx_feature[0] + 1),
        sns.countplot(x=features[idx_feature[0]], data=data),
        plt.title(f'Count of {features[idx_feature[0]]}'),
        plt.xlabel(features[idx_feature[0]]),
        plt.ylabel('Counts')
    ), enumerate(features)))

    plt.tight_layout()
    plt.show()

