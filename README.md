# Guess the Genre

## Project Goal: 
Review the basics of Natural Language Processing by creating a machine learning model that can predict the genre on a Netflix movie based upon it's description.

## Project Description: 
Movie genres have always been somewhat loosely understood and many genres have a fairly large degree of overlap. This can lead confusion and disappointed customers, who do not get the kind of experience they were expecting. I am hoping my analysis will provide insight into what drives a movies genre and produce an algorithem that can accuratly the genra of new movies as they come out. This would reduce the ammount of time spend having to label the genre of incoming movies, reduce the human error involved in labeling these movies, and provide customers with an experience that is more consistant with thier expectations.   

## Project Planning:

### Acquire
* Dowload csv of data from Kaggle
* Create wrangle module and use it to import the data into my notebook

### Prepare
* Drop all columns other than 'description' and 'genre'
* Prepare text in 'description' for exploration
  * Convert all letters in the text to lower case
  * Remove all non-asci and special characters form the text
  * Tokenize the words in the text
  * Lemmatize the words in the text
  * Remove stopwords

### Explore
* Answer Exploration Questions
  * What are the top 20 most frequently occuring words?
  * Are there any words that occur in only one genre?
  * Are there any words that occur much more frequently in one genre than in others?
  * What are the top 20 most frequently occuring bigrams?
  * Are there any bigrams that occur in only one genre?
  * Are there any bigrams that occur much more frequently in one genre than in others?

### Modeling
