# Uber-Travel-Time-Predictions

DESCRIPTION

Welcome to Team 26's final CX 4242 product! 

Our team has created a web application that looks to improve current methods for determining future Uber travel times. Current resources, namely Uber Movement, only use past aggregated travel time data to summarize the average travel time between two points at a specific time of day and only handle inputs of census tract ids instead of exact addresses. 

Our application consists of an interactive map of Atlanta, GA aggregated into census tracts from 2010 and input fields for the user to enter information such as starting and ending locations, date, and time. When entering the start and end locations, the user can either type in an exact address or double-click the map to set the starting census tract and single-click the map to set the ending census tract. The user's input data then gets sent to our algorithm in the back end, which consists of a regression neural network that takes in the data along with other derived features such as distance between the start and end locations and the weather for the specific time and day, and it returns the predicted travel time with an average error rate of about +/- 5 minutes.

The user interface and algorithm have been implemented as separate entities connected via a RESTful API that facilitates communication and the passing of data between the two. The following sections will go over how to install the necessary components and run the web app locally.

INSTALLATION

First, you must ensure that you have a version of Python 3.X installed on your computer, preferablly >= Python 3.8. If you do not already have a valid Python version installed, use the following link to download Python 3.9.5 and scroll to the bottom to download the correct installation file for your machine: https://www.python.org/downloads/release/python-395/.

Now, in your command line or terminal, cd into the "CODE" directory in the same directory as this file and run the following commands:

    pip install virtualenv
    OR
    python3 -m pip install virtualenv

    virtualenv team26cx4242

If you are a Windows user, run the following command:

    team26cx4242\Scripts\activate

and if you are a MacOS user, run the following command:

    source team26cx4242/bin/activate

You should now see the prompt in your command line change to

    (team26cx4242) user@machine $

Finally, run this command to install the necessary packages:

    pip install -r requirements.txt
    OR
    python -m pip install -r requirements.txt

You are now ready to run the code!

EXECUTION

To run the web app, you will need two command line or terminal windows open. In the first one, cd into the directory "backend". Then, for Windows users, run the following commands:

    set FLASK_APP=backend
    
    flask run

and for MacOS users, run the following commands:

    export FLASK_APP=backend

    flask run

In the other command line or terminal window, cd into the directory "frontend". Then run the following command:

    python -m http.server

You should now be complete and be able to get to the web app at the following url:
    
    http://localhost:8000/model.html 