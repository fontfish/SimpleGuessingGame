# A very simple example game using some of the concepts covered in this course:
# https://www.futurelearn.com/courses/video-game-design-development

# Define the Fairy class as a description of a fairy-tale character.
# Include values for their name and how many guesses they will allow.
# Also define something they do, in this case declaring their name.
class Fairy:
  def __init__(self, name, guesses):
    self.name = name
    self.guesses = guesses
  
  def printName(self):
    print("My name is actually " + self.name)

# Define our nemesis using the Fairytale class.
# By editing this, we can change our nemesis's trait values.
fairy1 = Fairy("Rumplestiltskin", 10)
guessesleft = fairy1.guesses
while guessesleft > 0:
  print("You have " + str(guessesleft) + " chances to guess my name.")
  guess = input(">>>")
  guessesleft -= 1

  if guess == fairy1.name:
    print("Congratulations! You guessed my name.")
    guessesleft = -1 # Breaks the while condition so the loop doesn't run again.
  elif guessesleft > 0:
    print("Wrong!")
  else:
      print("Wrong again!")
      print("Game Over")
      fairy1.printName() #Use the function defined in the character's class to have them give their name.
