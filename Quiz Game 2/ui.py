from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # pass in quiz_brain (aka, quiz) to call properties from "QuizBrain
        self.quiz = quiz_brain  # initialize quiz_brain (quiz) for use

        # WINDOWS
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # CANVAS
        self.canva = Canvas(bg="white", height=250, width=300)
        self.questiontext = self.canva.create_text(150, 125, width=280, text="I'm trying to fi",
                                                   font=("Ariel", 20, "italic"), fill="black")
        self.canva.grid(column=0, row=1, columnspan=2, pady=50)

        # LABEL
        self.score = Label(text="Score: 0", font=("Ariel", 20, "normal"), bg=THEME_COLOR, padx=20, pady=20)
        self.score.grid(column=1, row=0)

        # BUTTONS
        true = PhotoImage(file="images/true.png")
        self.truebutton = Button(highlightthickness=0)
        self.truebutton.config(image=true, command=self.choicetrue)
        self.truebutton.grid(column=0, row=2)

        false = PhotoImage(file="images/false.png")
        self.falsebutton = Button(highlightthickness=0)
        self.falsebutton.config(image=false, command=self.choicefalse)
        self.falsebutton.grid(column=1, row=2)

        self.getnextquest()
        self.window.mainloop()

    def getnextquest(self):
        self.canva.config(bg="white")  # change "bg" back to white
        if self.quiz.still_has_questions():  # check for more questions
            self.score.config(text=f"Score: {self.quiz.score}")
            qtext = self.quiz.next_question()  # self.object.method
            self.canva.itemconfig(self.questiontext, text=qtext)
        else:
            self.canva.itemconfig(self.questiontext, text="End of Quiz.")
            self.truebutton.config(state="disabled")  # turns off buttons
            self.truebutton.config(state="disabled")

    def choicetrue(self):
        isright = self.quiz.check_answer("True")  # self.module.method from Quiz_Brain(answer chosen); checks answer
        self.feedback(isright)

    def choicefalse(self):
        self.feedback(self.quiz.check_answer("False"))
        self.canva.config(bg="red")

    def feedback(self, isright):  # display a new question 1 sec after a button is pressed
        if isright:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.getnextquest)

