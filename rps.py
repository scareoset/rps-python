# rps.py | dani wright
# a script to generate contestants for a fantasy rps league
# rules:
#     options
#         rock(win: scissors, lose: paper)
#         paper(win: rock, lose: scissors)
#         scissors(win: paper, lose: rock)
#    a contestant chooses an option from the list of valid options
#    after a countdown (1, 2, 3, shoot!) both contestants show their choices
#    determine winner and adjust scores

# import statements
import random
import time

# variables
options = ["rock", "paper", "scissors"]
roster = []
first_names = [
    "Merideth", "Cierra", "Dorothea", "Leisa", "Ila", "Regenia", "Alicia",
    "Sherise", "January", "Eusebio", "Jewell", "Robin", "Columbus",
    "Jeannette", "Gerry", "Malorie", "Nana", "Jammie", "Lorilee", "Shanell",
    "Alvaro", "Lesley", "Cristina", "Caroyln", "Earl", "Reyna", "Sherilyn",
    "Chau", "Brenna", "Dorothy", "Sadye", "Joel", "Tula", "Jennie",
    "Valencia", "Annette", "Ione", "Hollie", "Margo", "Mandie", "Matha",
    "Allison", "Theodora", "Orlando", "Karin", "Lonna", "Trena", "Lon",
    "Perry", "Kiley"
]
last_names = [
    "Chagolla", "Labrecque", "Macauley", "Roush", "Dance", "Azure", "Santi",
    "Weatherly", "Bollman", "Bembry", "Batt", "Hasbrouck", "Larock", "Giel",
    "Bolan", "Vankleeck", "Caro", "Armwood", "Milnes", "Garrido", "Crotty",
    "Falkowski", "Toribio", "Hartmann", "Waugh", "Borgeson", "Sabine",
    "Abercrombie", "Whalen", "Laforge", "Himes", "Veliz", "Till", "Jansen",
    "Lawton", "Schalk", "Sandifer", "Shimer", "Serrata", "Garibay",
    "Lowenstein", "Kovacs", "Brickman", "Ord", "Speier", "Matson", "Wingate",
    "Reilley", "Dupler", "Champlin"
]

class Contestant:
    # a contestant
    #     has a name(first_name last_name)
    #     has a score
    #     and is either alive or dead
    def __init__(this, first_name, last_name):
        this.first_name = first_name
        this.last_name = last_name
        this.score = 0
        this.alive = True
        this.strategy = "default"
        this.choice = "rock"

    # gives a contestant a new name
    # called when a contestant has a name change
    def set_name(this, new_first_name, new_last_name):
        this.first_name = new_first_name
        this.last_name = new_last_name

    # updates a contestant's score
    # called after a match
    def update_score(this, points):
        this.score += points

    # changes a contestant's alive status
    # called whenever a player dies or is resurrected
    def change_alive(this):
        this.alive = not this.alive

    # player chooses an option for a match
    # called once per round in a match
    def choose(this):
        if this.strategy == "default":
            this.choice = random.choice(options)

    # return player name
    # default to_string()
    def to_string(this):
        return this.first_name + " " + this.last_name

    # return player name: points
    # for roster_to_string()
    def to_string_r(this):
        return (this.first_name + " " + this.last_name  + ": " + str(this.score)
            + " points")

def create_roster(length):
    if len(roster) != 0:
        print("warning: roster is not empty!")
    else:
        print("making new roster")
        for x in range(length):
            f_n = random.choice(first_names)
            l_n = random.choice(last_names)
            new_contestant = Contestant(f_n, l_n)
            roster.append(new_contestant)

def roster_to_string():
    str = "--------------------------------\nroster:\n"
    for x in roster:
        str += x.to_string_r() + "\n"
    return str

# a match takes place between two contestants
# a match consists of three rounds
# the contestant who wins two rounds first wins the match
#     if a match ends and no contestant has won two rounds
#         the contestant who has won the most rounds wins the match
#         if the contestants are tied, the winner is decided by who has the most
#             points
#         if both contestants have the same amount of points, the winner is
#             decided by a coin flip
def match():
    print("--------------------------------\nstarting new match")
    time.sleep(0.1)

    # select contestants
    c_1 = random.choice(roster)
    c_2 = random.choice(roster)

    # make sure contestants are not playing against themselves
    while c_2 == c_1:
        print(c_1.to_string() + " selected to play themself.")
        c_2 = random.choice(roster)

    # announce matchup
    print("match: " + c_1.to_string() + " v " + c_2.to_string())
    time.sleep(0.1)

    # three rounds in a match
    for i in range(3):
        round(c_1, c_2, i)

    # match over
    print("match end")

# three rounds in a match
# in each round
#     countdown
#     contestants choose
#     shoot (reveal)
#     evaluate outcome and award points
def round(c_1, c_2, num):
    # announce round number
    print("round " + str(num + 1))
    time.sleep(0.1)
    c_1_points = 1
    c_2_points = 1

    # contestants make decisions
    c_1.choose()
    c_2.choose()

    # countdown
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    # reveal choices
    print("shoot!")
    print(c_1.to_string() + ": " + c_1.choice)
    print(c_2.to_string() + ": " + c_2.choice)

    # evaluate round outcome and award points
    winner = find_winner(c_1, c_2)
    if winner == 0:
        print("draw!")
    elif winner == 1:
        print(c_1.to_string() + " wins the round!")
        c_1_points = 2
        c_2_points = -1
    elif winner == 2:
        print(c_2.to_string() + " wins the round!")
        c_1_points = -1
        c_2_points = 2
    c_1.update_score(c_1_points)
    c_2.update_score(c_2_points)
    time.sleep(0.3)

    # announcenew point totals
    print(c_1.to_string() + " has " + str(c_1.score) + " points.")
    print(c_2.to_string() + " has " + str(c_2.score) + " points.")
    print("round end")

# rock(win: scissors, lose: paper)
# paper(win: rock, lose: scissors)
# scissors(win: paper, lose: rock)
# tie return 0
# c_1 win return 1
# c_2 win return 2
def find_winner(c_1, c_2):
    if c_1.choice == c_2.choice:
        return 0
    elif c_1.choice == "rock" and c_2.choice == "paper":
        return 2
    elif c_1.choice == "rock" and c_2.choice == "scissors":
        return 1
    elif c_1.choice == "paper" and c_2.choice == "rock":
        return 1
    elif c_1.choice == "paper" and c_2.choice == "scissors":
        return 2
    elif c_1.choice == "scissors" and c_2.choice == "rock":
        return 2
    elif c_1.choice == "scissors" and c_2.choice == "paper":
        return 1

# run the simulation

create_roster(10)

for x in range(10):
    match()

print(roster_to_string())
