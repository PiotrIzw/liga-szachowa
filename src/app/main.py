import os

from src.app import Player


while True:
    print("Menu:")
    print("1. Zawodnik:")
    print("2. Statystyki:")
    print("3. Ranking:")
    print("4. ...")
    print("9. Wyjście:")
    what_to_do = input("Wybierz jedną z opcji:\n")
    if what_to_do == '1':
        Player.playerMenu()
    elif what_to_do == 2:
       print("...")
    elif what_to_do == '9':
       print("Do zobaczenia :)")
       exit()
