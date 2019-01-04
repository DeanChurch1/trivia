#Dean Church
#1/19
#trivia challenge
#trivia game reads a plain text file
import sys


def open_file(file_name,mode):
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file",file_name,"Ending program.\n",e)
        input("\n\nPress enter key to exit")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    exp_line = next_line(the_file)
    return category,question,answers,correct,exp_line


def welcome(title):
    print("\t\tWelcome to Trivia Challenge\n")
    print("\t\t",title,"\n")

def main():
    main = open_file("test_file.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category,question,answers,correct,exp_line
    next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answers)
    answer = input("What is your answer")
    if answer == correct:
        print("Congratulations")
        score += 1
    else:
        print("incorrect")
    print("explanation")
    print("This is your score",score)
    next_block(the_file)







##the_file = open_file("test_file.txt","r")
##title = next_line(the_file)
##category,question,answers,correct,exp_line = next_block(the_file)
##welcome(title)
##print(category)
##print(question)
##print(answers)
##print(correct)
##print(exp_line)


##file_name = "test_file.txt"
##the_file = open_file(file_name,"r")
##line = next_line(the_file)
##print(line)
