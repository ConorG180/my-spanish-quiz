# Spanish quiz
This programme is designed to test a user's level of spanish and to assist them in learning the Spanish language. This quiz is designed not only to grade the user's level of spanish, but also to provide the user with the correct translation of the word once they have guessed, thus helping them to learn more.  
The quiz can be played on an easy, medium or hard level of difficulty to adapt to player's different levels of the language, and there will be a different dictionary of words chosen depending on the user's chosen difficulty.  
The user also has the feature to choose the amount of words to be graded on, with a maximum of 100 words per game.  

The full **[Spanish quiz](<!-- Add Heroku project link here later -->)** game can be played here. Go on, have a go!
# Flow chart
Before beginning the project, a flow chart was designed to visualize the logic behind the programme. The flow chart can be seen below. Please note that this flowchart was made in the initial design process for the project, and some minor changes may be incorporated as the project is being built. One example of this can be seen in requesting the user for their name. This is currently requested in the programme, however it is not present in the flowchart.  
![Spanish quiz flowchart](assets/flow-charts/flowcharts/spanish-quiz-flowchart.drawio.png "Spanish quiz flowchart")

# Features
## Existing Features
 - Name input - Along with the inputs relevant for the quiz, we also request the user's name so that we can refer to them by name, making for a more personalised experience throughout the quiz.
 - User input validation - The programme includes validation checking on all user input entered into the programme. Rather than crashing the programme, the user will receive a relevant error message upon the wrong input being entered, and asked to repeat their input.
 - Difficulties - The programme is designed to be played on either an easy, medium or hard difficulty. This allows for users of various levels of spanish to enjoy and participate in the quiz, thereby increasing accessibility and the target audience of the programme.
 - Score - During the game, the user's score is tracked. This is used to calculate how many questions the user has gotten correct, and how many they have gotten incorrect. It is also later used to find out the user's percentage of right/wrong answers.
 - Grading - At the end of the game, the user will be given a grade based on how well they have done (based off the irish grading system e.g. B1, B2, A1 etc.), along with a comment which is relevant to their grade. Other statistics include a percentage of the user's correct/incorrect answers, how many correct and incorrect answers the user has inputted, and the total amount of words that they have been tested on.
 - Object oriented programming (OOP) - This project was created using the OOP methodology. Because of this, the code should have increased readibility and be easier to add new features and maintain in the future, and will also be advantageous to others who may wish to update/edit/study the programme.
 - Automatic clearing of terminal - A method was created to automatically clear the user terminal at various stages throughout the script. This makes the programme more readable and aesthetic for the user, as there is only a little bit of new information to be processed as opposed to lots of information, most of which the user will have read already.
 - Play again, restart or exit - When the user has completed their quiz, they then have 3 options to pick from - They can either choose to replay the quiz with the same settings (Same name, number of words and difficulty), restart the game to play with different settings, or exit the game entirely.
## Future features
 - English to Spanish questions - In the future, a feature may be added to allow the user to be tested on words in English, and attempt to provide a translation of the word in to Spanish.
 - Saving grades - A feature may be added to allow the user to save the grade in the form of a .txt document. This feature simply involves asking the user if they would like to save their grade, along with all their statistics about how they have done on the quiz. If the user wants, a .txt document would be written up outlining the user's grade and quiz results, and be saved on to the user's device.
 - Phrases - Currently, the dictionaries used to hold the words simply hold the spanish word as a key, and the english translation as the value. However, a feature may later be added to this programme whereby a second key is added to each of these dictionaries called "phrase" which would give an example of how the word is used in a Spanish sentence once the user has attempted their answer. This would help the user to learn more, as it would not only provide a phrase for the user and in turn more Spanish vocabulary, but would also help with grammar and allow the user to better understand the context of where the word is typically used.
 - Grammar/Vocabulary/Verbs modes - To better target a user's particular area of learning, it may be a good idea to provide different modes in which the quiz could be run. This would involve creating 3 separate dictionaries for each type of mode (one for easy, medium and hard) and then inputting the correct words(grammar, vocabulary or verbs) into the appropriate dictionaries depending on their degree of difficulty.

# Testing and bugs
For all testing, please refer to the [TESTING.md](TESTING.md) file.
<!-- ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Conor,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding! -->