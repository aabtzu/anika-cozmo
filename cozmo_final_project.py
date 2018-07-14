import cozmo

def cozmo_program(robot: cozmo.robot.Robot):

    robot.say_text("Hello There! My name is Cozmo").wait_for_completed()

    robot.say_text("It's nice to meet you").wait_for_completed()

# Answer Variable Code

    robot.say_text("How are you?").wait_for_completed()
    answer = input("How are you?")

    robot.say_text("That's nice to hear. I'm ..." +answer+ ",too!").wait_for_completed()

# Answer2 Variable Code

    robot.say_text("I'll help you, come stay inside!! Global warming has made it so hot").wait_for_completed()
    answer2 = input("I'll help you, come stay inside!! Global warming has made it so hot.")

    robot.say_text("You're welcome!").wait_for_completed()

# Answer3 Variable Code

    robot.say_text("If you stay inside with me, we will learn more about global warming!").wait_for_completed()

    answer3 = input("\nIf you stay inside with me, we will learn more about global warming!")

# Answer4 Variable Code
    robot.say_text("Global warming has many interesting facts.Let's get started. For example, "
                   "Over time the ozone layer has broken little by little because of fumes and gases.").wait_for_completed()
    robot.say_text("Since the ozone layer is broken, it is hotter.The ozone layer keeps the heat out and its not "
                   "working.").wait_for_completed()
    robot.say_text("Did you know that?" +
                   "A. Yes!" +
                   "B. No").wait_for_completed()

    answer4 = input("\nGlobal warming has many interesting facts.\n\nLet's get started\n\nFor example, "
                    "Over time the ozone layer has broken little by little because of fumes and gases.\n\nSince "
                    "the ozone layer is broken, it is hotter.\n\nThe ozone layer keeps the heat out and its not "
                    "working.\n\nDid you know that?\n" +
                    "A. Yes!\n" +
                    "B. No\n")

    if answer4 == "A. Yes!":
        robot.say_text("That's great!").wait_for_completed()

    else:
        robot.say_text("That's okay, you learned something new!").wait_for_completed()


# Answer5 Variable Code

    robot.say_text("Also global warming has changed the weather and climate. It has made it so colder places are "
                   "melting and losing their natural beauty.What do you think about this?" +
                   "A. This is bad" +
                   "B. This is good").wait_for_completed()

    answer5 = input("\nAlso global warming has changed the weather and climate. It has made it "
                    "so colder places are melting and losing there natural beauty.\n\nWhat do you "
                    "think about this?" +
                    "\nA. This is bad\n" +
                    "\n\nB. This is good\n")

    if answer5 == "A. This is bad":
        robot.say_text("That's what I thought too!").wait_for_completed()

    else:
        robot.say_text("I wasn't thinking that... maybe try rethinking your answer").wait_for_completed()

# Answer6 Variable Code

    robot.say_text("Have you noticed that over the years the summers have gotten hotter and the "
                   "winter have gotten less cold? That happened because of global warming. "
                   "What do you think about this?" +
                   "A. I think it is bad" +
                   "B. It is good").wait_for_completed()

    answer6 = input("\nHave you noticed that over the years the summers have gotten hotter and the "
                    "winters have gotten less cold?\n\n That happened because of global warming. What do "
                    "you think about this?\n\n" +
                    "A. I think it is bad\n" +
                    "B. It is good\n")

    if answer6 == "A. I think it is bad":
        robot.say_text("Me too! I think it is bad for the environment").wait_for_completed()

    else:
        robot.say_text("I don't think it is good... maybe try rethinking your answer").wait_for_completed()

    robot.say_text("Those were all the facts about global warming I had to share "
                   "with you! Thank you and Goodbye!!").wait_for_completed()

cozmo.run_program(cozmo_program)