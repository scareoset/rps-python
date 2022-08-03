# rps-python
a rock paper scissors tournament written in python

## shoot options
🪨 rock
    - win
        - ✂️ scissors
    - lose
        - 📄 paper
    - draw
        - 🪨 rock
📄 paper
    - win
        - 🪨 rock
    - lose
        - ✂️ scissors
    - draw
        - 📄 paper
✂️ scissors
    - win
        - 📄 paper
    - lose
        - 🪨 rock
    - draw
        - ✂️ scissors

## matches

    a match takes place between two contestants

    a match consists of three rounds.

    at the end of each round points are awarded to each contestant

        win: +2

        draw: +1

        loss: -1

    the contestant who wins the match advances in the season bracket

    the contestant who wins two rounds first wins the match

        if a match ends and no contestant has won two rounds

            the contestant who has won the most rounds wins the match

            if the contestants are tied, the winner is decided by who has the most points

            if both contestants have the same amount of points, the winner is decided by a coin flip