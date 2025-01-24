import tkinter
import tkinter.messagebox
import json
import random


class ProgramGUI:

    def __init__(self):
        self.main = tkinter.Tk()  # Creates the main window of the program

        self.main.title('Quiz')
        self.main.geometry('600x200')

        # Loading the file with questions
        FILENAME = 'data.txt'
        try:
            with open(FILENAME, 'r') as fin:
                self.data = json.load(fin)
        except:
            tkinter.messagebox.showerror('File Error', 'Missing/Invalid file')
            self.main.destroy()
            return  # This ensures the constructor ends cleanly

        # Check there are enough questions in the database
        if len(self.data) < 5:
            tkinter.messagebox.showerror('Error', 'Insufficient number of questions')
            self.main.destroy()
            return  # Constructor ends cleanly

        # Create and pack question number label
        self.font_style = ('Arial', 10)
        self.question_number_label = tkinter.Label(self.main, font=self.font_style, padx=10, pady=10)
        self.question_number_label.pack()

        # Create and pack question text label
        self.font_style = ('Arial', 16)
        self.question_text_label = tkinter.Label(self.main, font=self.font_style, padx=10, pady=10)
        self.question_text_label.pack()

        # Create Frame widget to hold entry and button widgets
        self.bottom = tkinter.Frame(self.main, padx=10, pady=5)
        self.bottom.pack()

        # Create the Entry area for user to write answer
        self.user_response = tkinter.Entry(self.bottom, width=40)
        self.user_response.pack(side='left')
        # This allows the user to press Enter key on their keyboard
        self.user_response.bind('<Return>', self.check_answer)

        # Create the Submit Answer button
        self.answer_button = tkinter.Button(self.bottom, text='Submit Answer', command=self.check_answer)
        self.answer_button.pack(side='right', padx=10, pady=10)

        # Create a label to show the difficult question message
        self.hard_label = tkinter.Label(self.main, text='This is a hard one - good luck!', fg='blue')

        # ------ Pick 5 random questions ------
        self.quiz_questions = random.sample(self.data, k=5)

        self.current_question = 0   # Keeps track of which question user is up to
        self.score = 0              # Keeps track of user score

        # ------ Call the show_question method to display question
        self.show_question()

        # ------ Run the main window loop
        tkinter.mainloop()


    def show_question(self):
        self.user_response.delete(0, tkinter.END)   # Clear the entry widget
        self.user_response.focus_set()              # Focus on the entry widget

        # Set current question to ask by popping an item off the self.quiz_questions list
        self.question_to_show = self.quiz_questions.pop()
        self.question_text_label.configure(text=self.question_to_show['question'])

        # Display the question number
        combined_string = f'Question {self.current_question + 1} of 5:'
        self.question_number_label.configure(text=combined_string)

        # Remove the hard question label from previous question before checking if next question is a hard one
        self.hard_label.pack_forget()

        # If the question is a hard one (i.e. has a difficulty of 4 or 5)
        if self.question_to_show['difficulty'] >= 4:
            self.hard_label.pack(before=self.question_text_label)


    def check_answer(self, event=None):
        # Create a variable to store the right answers for the current question
        right_answers = self.question_to_show['answers']

        # When the user presses the Submit Answer button increment self.current_question by 1
        self.current_question += 1

        # Compare the string they entered in the "user_response" entry widget with the list of "right_answers"
        if self.user_response.get().lower() in right_answers:
            tkinter.messagebox.showinfo('Correct!', 'You are correct!')
            # Increase their score -> question difficulty * 2
            self.score += 2 * self.question_to_show['difficulty']
        else:
            tkinter.messagebox.showerror('Incorrect!', 'Sorry, that was incorrect!')

        # Keep track of how many questions have been asked and end the game if 5 questions have been asked
        if self.current_question == 5:
            # End game and show user their final score
            tkinter.messagebox.showinfo('Final Score', f'Game over.\nFinal score: {self.score}\n\nThank you for playing!')
            self.main.destroy()
        else:
            self.show_question()

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()