## Trivia game

### Admin.py
This program allows the user to manage a list of quiz questions which are
stored in a text file called `data.txt`. 
The program stores the trivia questions in JSON format and uses the `json` module to write data to the text
file and to read the JSON data back into a variable called `data`.

### Quiz.py
This program is the GUI that uses the questions in `data.txt` to show a simple five-question quiz to a user. The program keeps
track of the user's score and displays the results at the end. A user's score is calculated by multiplying a question's difficulty by two.
