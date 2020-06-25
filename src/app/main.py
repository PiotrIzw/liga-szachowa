import os

from src.app import Player
from src.app import Statistics

while True:
    print("Menu:")
    print("1. Zawodnik")
    print("2. Statystyki")
    print("3. Ranking")
    print("4. Wyjście")
    what_to_do = input("Wybierz jedną z opcji:\n")
    if what_to_do == '1':
        Player.playerMenu()
    elif what_to_do == '2':
        Statistics.statisticsMenu()
    elif what_to_do == '3':
        print("...")
    elif what_to_do == '4':
        print("Do zobaczenia :)")
        exit()
    else:
        print("Bledny wybor. Sprobuj jeszcze raz.\n")
