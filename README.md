# recipeRecommendationSystem
README File - Recipe Recommender System

-Link to the Github Repo for the Flask web app
	https://github.com/areast21/recipeRecommendationSystem/tree/main
	
-App is hosted at 
    http://recor3.pythonanywhere.com/

-*NOTE* Please make sure that you have the following python libraries installed before running the flask web app:
	1. flask
	2. pandas
	3. numpy
	4. functools
	5. sklearn
-The processed data set is also available in the repository as "finalCleanedlDataSet.csv"
-To run the flask app, open up the terminal or cmd and make sure the directory is pointed at "myFlask" level.
-Enter "flask run", user can notice that the development server has launched.
-Go to the mentioned IP address in any browser and access the web app.

-Refer the IR.ipynb file for the dataset preparation steps. It also involves few sample queries.

-The role of the flask app is to obtain the inputs from the client side and toss them into the backend (simply the querying algorithm which has access to the finalCleanedDataSet.csv).

-*NOTE* To run the IR.ipynb file you must download additional python libraries:
    1. re
    2. spacy
    3. string
    4. operator
    5. multiprocessing
    6. nltk
    7. time
    8. networkx
    9. scipy
    10. matplotlib
    11. itertools

-****Running the IR.ipynb file is not required to run the flask application. myFlask is a standalone app.****

-Repository contributors: Adithya Ramesh, Darshan Swami, Parth Jay Dhruv, Sidhanth Jain
-Project submitted as part of the course "Information Retrieval" - Spring 2023 - Worcester Polytechnic Institute, MA, USA
