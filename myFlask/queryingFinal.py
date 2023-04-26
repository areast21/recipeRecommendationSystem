import pandas as pd
import numpy as np
import re
from functools import reduce
from sklearn.feature_extraction.text import TfidfVectorizer
import io
import sys

recipes = pd.read_csv('finalCleanedlDataSet.csv')

# Creating TF-IDF Matrices and recalling text dependencies

'''import text_tokenized.csv here'''

# TF-IDF vectorizer instance
vectorizer = TfidfVectorizer(lowercase = True,
                            ngram_range = (1,1))

'''text_tfidf = vectorizer.fit_transform(tokenized_text)'''
title_tfidf = vectorizer.fit_transform(recipes['title'])
# text_tfidf    <== Variable with recipe ingredients and instructions

tags_tfidf = vectorizer.transform(recipes['tags'].values.astype('U'))
# recipes   <== DataFrame; For indexing and printing recipes

# Query Similarity Weights
w_title = .2
w_text = .3
w_categories = .5

def qweight_array(query_length, qw_array = [1]):
    '''Returns descending weights for ranked query ingredients'''
    if query_length > 1:
        to_split = qw_array.pop()
        split = to_split/2
        qw_array.extend([split, split])
        return qweight_array(query_length - 1, qw_array)
    else:
        return np.array(qw_array)

def ranked_query(query):
    '''Called if query ingredients are ranked in order of importance.
    Weights and adds each ranked query ingredient vector.'''
    query = [[q] for q in query]      # place words in seperate documents
    q_vecs = [vectorizer.transform(q) for q in query] 
    qw_array = qweight_array(len(query),[1])
    q_weighted_vecs = q_vecs * qw_array
    q_final_vector = reduce(np.add,q_weighted_vecs)
    return q_final_vector

def overall_scores(query_vector):
    '''Calculates Query Similarity Scores against recipe title, instructions, and keywords.
    Then returns weighted averages of similarities for each recipe.'''
    final_scores = title_tfidf*query_vector.T*w_title
    final_scores += tags_tfidf*query_vector.T*w_categories
    return final_scores

def format_recipes(index, query, recipe_range):
    '''Prints recipes according to query similary ranks'''
    recoR3 = {}
    for i, index in enumerate(index, recipe_range[0]):
        recipeTitle = recipes.loc[index,'title']
        recipeIngredients = recipes.loc[index, 'ingredient_text']
        recipeInstructions = recipes.loc[index, 'instructions']
        recoR3[recipeTitle] = [recipeIngredients, recipeInstructions]
    return recoR3

        
def Search_Recipes(query, query_ranked=False, recipe_range=(0,3)):
    '''Master Recipe Search Function'''
    if query_ranked == True:
        q_vector = ranked_query(query)
    else:
        q_vector = vectorizer.transform([' '.join(query)])
    recipe_scores = overall_scores(q_vector)
    sorted_index = pd.Series(recipe_scores.toarray().T[0]).sort_values(ascending = False)[recipe_range[0]:recipe_range[1]].index
    return format_recipes(sorted_index, query, recipe_range)

#Search_Recipes(query, query_ranked=True, recipe_range=(0,3))