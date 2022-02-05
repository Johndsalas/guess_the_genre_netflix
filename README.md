# Guess the Netflix Genre

## Project Goal: 
Review the basics of Natural Language Processing by creating a machine learning model that can predict the genre on a Netflix movie based upon it's description.

## Project Description: 
Movie genres have always been somewhat loosely understood and many genres have a fairly large degree of overlap. This can lead confusion and disappointed customers, who do not get the kind of experience they were expecting. I am hoping my analysis will provide insight into what drives a movies genre and produce an algorithem that can accuratly the genra of new movies as they come out. This would reduce the ammount of time spend having to label the genre of incoming movies, reduce the human error involved in labeling these movies, and provide customers with an experience that is more consistant with thier expectations.   

## Project Planning:

### Acquire
* Dowload csv of data from Kaggle
* Create wrangle module and use it to import the data into my notebook
* Add a markdown block describing the shape of the data, what each observation repesents, and where the data can be acquired from

### Prepare
* Drop all columns other than 'description' and 'genre'
* Prepare text in 'description' for exploration
  * Convert all letters in the text to lower case
  * Remove all non-asci and special characters form the text
  * Tokenize the words in the text
  * Lemmatize the words in the text
  * Remove stopwords
* Modify genre by merging and removing genres untill there is only one genre for each observation
* Add code to wrangel module and import it into the notebook
* Add a markdown block to the notebook describing how the data was prepared

### Explore
* Answer Exploration Questions
  * What are the top 20 most frequently occuring words?
  * Are there any words that occur in only one genre?
  * Are there any words that occur much more frequently in one genre than in others?
  * What are the top 20 most frequently occuring bigrams?
  * Are there any bigrams that occur in only one genre?
  * Are there any bigrams that occur much more frequently in one genre than in others?
* Create an Explore module to hold my code for this section and import that code into the notebook

### Modeling
* Vectorize the data in 'description'
* Split the data into train, validate, and test
* Establish baseline by finding the accuracy of guessing the most frequently occuring genre for each or the observations in the train data set
* Use vectorized data to build models of differint types of classification models
  * Decision Tree
  * Random Forest
  * K- Nearest Neighbors
  * Logistic Regression
* Compare model predictions on train and test data
* Select top performing model based on highest accuracy
* Observe selected model's predictions on test data to guadge how it is likely perform on unseen data
* Create a modeling module to hold my code for this section and import that code into the notebook

### Conclutions
* Draw conclusions and make recommendations
* Record ideas for next steps
* Add 'steps to reproduce' to README

### Delivery
* Create a slide show in Canva to show my findings
  * Begin with executive summery
  * Show highlights of exploration
  * Give a brief explination of how the model uses the data to make predictions
  * End with recommendations, next steps, and final thoughts

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|Genre|The catagory of the movie as assigned by Netflix (With some modifications, See prepare steps)|
|Description| Text describing what the movie is about|

