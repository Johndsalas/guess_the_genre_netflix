
import matplotlib.pyplot as plt
import pandas as pd

def all_common(train):
    ''' get bar chart with 20 most frequent words across all genres'''
    all_words = ' '.join(train.description).split(' ')
    all_freq = pd.Series(all_words).value_counts().head(20).sort_values(ascending = True)
    all_freq.plot(kind = 'barh', title = "Top 20 Most Frequent Words Across All Genres")
    plt.show()

def explore_word_count_raw(genre, train):
    '''takes in a genre and returns a chart showing a raw count of the 20 most frequently occuring words in that genre'''
    bag_of_words = ' '.join(train[train.genre == genre].description).split(' ')
    word_freq = pd.Series(bag_of_words).value_counts().head(20).sort_values(ascending = True)
    word_freq.plot(kind = 'barh', title = f"Top 20 Most Frequent Words in {genre} Raw Count")
    plt.show()

def explore_word_count_norm(genre, train):
    '''takes in a genre and returns a chart showing a normalized count of the 20 most frequently occuring words in that genre'''
    bag_of_words = ' '.join(train[train.genre == genre].description).split(' ')
    word_freq = pd.Series(bag_of_words).value_counts(normalize = True).head(20).sort_values(ascending = True)
    word_freq.plot(kind = 'barh', title = f"Top 20 Most Frequent Words in {genre} Normalized")
    plt.show()