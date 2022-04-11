from tkinter import *
import time


class DissapearingTextGUI:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width=800, height=600)
        self.window.title("Dissapearing Text App")

        # upper text
        self.upper_text = Label(text="Start Writing", font=("Arial", 20))
        self.upper_text.grid(row=0, column=1)


        # How much time you can pass w/o writing
        self.time_for_writing = 10

        # Time not written (second counter)
        self.time_not_written = self.time_for_writing

        # Entry
        self.entry = Text(
            width=100
        )
        # self.entry.pady = 100
        self.entry.grid(row=1, column=0, columnspan=3, padx=100, pady=50)

        self.check_text(self.time_for_writing, self.get_text())

        self.window.mainloop()

    def get_text(self):
        return self.entry.get(1.0, "end-1c")

    def countdown_label(self, time):
        self.upper_text['text'] = time
        print(time)
        self.time_not_written -= 1

    def reset_label(self):
        self.upper_text['text'] = "Continue Writing"

    def check_text(self, count, prev_text):
        text = self.get_text()
        # print(text)


        if count > 0:
            print(count)
            if prev_text == text:
                self.window.after(1000, self.check_text, count - 1, text)
                print("OPAAA")

                self.countdown_label(self.time_not_written)
            else:
                print("doing well, doing well")
                count = self.time_for_writing
                self.window.after(1000, self.check_text, count, text)

                # Resetting the not writing timer
                self.time_not_written = self.time_for_writing

                # Resetting Label
                self.reset_label()


dissapearing_text_gui = DissapearingTextGUI()
