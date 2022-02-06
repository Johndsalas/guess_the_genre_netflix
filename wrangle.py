

import pandas as pd
import re

import unicodedata
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

def get_movie_data():
    '''reads data from csv into pandas'''

    return pd.read_csv('netflixdata.csv')


def lemmatizer(value):
    '''Takes in a value from a pandas column and returns the value lemmatized'''
    
    # create lemmatizer object
    wnl = nltk.stem.WordNetLemmatizer()
    
    # get list of lemmatized words in value
    value_lemmas = [wnl.lemmatize(word) for word in value.split()]
    
    # turn list or words back into a string and return value
    return ' '.join(value_lemmas)

def tokenizer(df):
    '''Takes in a value from a pandas column and returns the value tokenized'''

    # create tokenizer object
    tokenizer = nltk.tokenize.ToktokTokenizer()

    # tokenize text in description
    df['description'] = df['description'].apply(lambda value: tokenizer.tokenize(value, return_str=True))

    return df

def remove_stopwords(value):
    
    # get list english language stopwords list from nlt
    stopword_list = stopwords.words('english')
    
    # split words in pandas value into a list and remove words from the list that are in stopwords
    value_words = value.split()
    filtered_list = [word for word in value_words if word not in stopword_list]
    
    # convert list back into string and return value
    return ' '.join(filtered_list)


def prep_description_text(df):

    # remove non-ascii characters from description text 
    df['description'] = df['description'].apply(lambda value: unicodedata.normalize('NFKD', value)\
                                                                         .encode('ascii', 'ignore')\
                                                                         .decode('utf-8', 'ignore'))

    # remove special characters from description text
    df['description'] = df['description'].apply(lambda value: re.sub(r"[^a-z0-9\s]", '', value))

    # tokenizes text in description
    df = tokenizer(df)

    # lemmatize the text in description
    df['description'] = df['description'].apply(lambda value: lemmatizer(value))

    # remove stopwords from text in description
    df['description'] = df['description'].apply(lambda value: remove_stopwords(value))

    return df

def remove_cinima_type(value):
    '''Take in genre text from a pandas column
       Remove text indicating standalone movie or series
       return remainder of the text'''
     
    value = value.replace(' tv','') 
    value = value.replace('tv ','')
    value = value.replace(' shows','')
    value = value.replace(' movies','')
    value = value.replace(' series','')
    value = value.replace(' features','')
    
    value = [genre.strip() for genre in value.split(',')]
    
    return ','.join(value)

def get_genre_list(value):
    '''takes in string list of genes from a pandas column
       creates a python list of those genres 
       removes genres in the cut list 
       returns created list'''
    
    cut_list = ['international', 
                'teen', 
                'korean', 
                'anime', 
                'classic & cult', 
                "kids'", 
                'cult', 
                'movies', 
                'shows',
                'spanish-language', 
                'british', 
                'children & family', 
                'anime series',
                'lgbtq',
                'classic', 
                'international',
                'independent',
                'sci-fi & fantasy',
                'sports',
                'faith & spirituality',
                'stand-up comedy & talk',
                'mysteries']
    
    genre_list = value.split(',')
    genre_list = [genre.strip() for genre in genre_list]
    
    return [genre for genre in genre_list if genre not in cut_list]

def merge_genres(value, merge_list, replacement):
    '''Take in a pandas value that is a list of genres
       a merge list and a replacement string
       If one of the genres in genre_list is in merge_list 
       return a list containing the replacement string
       otherwise return original list'''

    # builds list of genres from value matching merge_list
    check_list = [genre for genre in value if genre in merge_list]

    # if check_list is not empty return list with just documentary
    if len(check_list) > 0:
        
        return [replacement]
    
    # otherwise return original list
    else:
        
        return value

def prepair_genres(df):

    # remove text indicating standalone movie or series
    df['genre'] = df['genre'].apply(lambda value: remove_cinima_type(value))

    # get new column with string of genres in each row made into a curated list of those genras 
    df['genre_list'] = df['genre'].apply(lambda value: get_genre_list(value))

    # merge all films in 'documenty' genre into one catagory named documentaries
    df['genre_list'] = df['genre_list'].apply(lambda value: merge_genres(value,['docuseries', 'documentary', 'documentaries'],'documentaries'))


    return df

def prep_movie_data(df):

    # drop columns not related to this project
    df = df[['Description','Genres']]

    # Lowercase all of the letters in both columns
    df['Description'] = df['Description'].apply(lambda value: value.lower())
    df['Genres'] = df['Genres'].apply(lambda value: value.lower())

    # rename columns
    df = df.rename(columns={'Description':'description', 'Genres':'genre'})

    # prepare text in description for exploration
    df = prep_description_text(df)

    # modify values in genre untill there is only one genre in each value 
    df = prepair_genres(df)

    return df

# def get_my_data():

#     df = get_movie_data()

#     df = prep_movie_data(df)

#     return df.head()

# get_my_data()