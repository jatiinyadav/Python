class Section:

    def __init__(self, Yadav, kumar):
        self.jatin = Yadav
        self.jeet = kumar


    def say(self):
        print("The compute is ", self.jatin, self.jeet )


one = Section(12, "Jatin")
two = Section(18, "Yadav")

one.say()
two.say()
