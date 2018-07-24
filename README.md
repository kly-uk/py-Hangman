# py-Hangman
Hangman game made with Python 3.6

*(Code has not been cleaned as yet! There are lots of lines of code that could be shortened and more organized unfortunately.)*

               
 
  
               ### About

1. A large quantity of words (related to my experience in DevOps) stored inside a list called "*words*".

1. Application begins by asking the user if they would like to play the game, prompting the user to enter options "y" or "n".

1. App now asks the user for their name and assigns them the attributes associated with the "*Player*" Class.

1. Function "*getWords()*" generates a new random word from the list and is assigned to the variable "*chosenWords*" as a string.

1. Game now displays that word with each character replaced with "_". This process takes place in the function "generateLines()".

1. An input is now prompted for which letter from the alphabet the user would like to use for their guess. Wrong answer results in the player losing one life and generating the "*drawHangman()*" function, which draws the progress of the hangman based off the amount of remaining lives the player currently has. Correct answer will cause that specific letter chosen to be displayed according to the given word.

1. Player now gets the option to guess the answer using their current progress.

1. Player now gets to choose their next letter. The game goes on till when the player either wins or loses.

1. At the end of the game, player is asked whether they want to continue playing which will reset all stats excluding the player's score, which increments with each win and resets to "0" with  each failed attempt.



              ### Rules

* Players start with 6 lives.

* Players cannot choose the same letter twice, nor can they select a number or more than one characters in a single turn.

* Players loses a life with each incorrect answer.

* Players loses 2 lives for each incorrect wild guess.

* A Player **Wins** either by getting all characters in the chosen word correctly, or by guessing the whole word correctly.

* A Player **Loses** either by losing all of their lives.


                                            ## HOPE YOU ENJOY!!
