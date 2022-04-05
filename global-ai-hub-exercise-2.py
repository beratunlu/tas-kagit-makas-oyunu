#Collect all the components of your program to run it in a while loop
#Import the random library

import random

#Add the code to create a list containing the three actions of the game.

List = ["Rock","Paper","Scissors"]

#Add the code to set the scores of players to 0

kactur = int(input("Kaç tur Oynamak İstiyorsunuz:"))


Oyuncu1 = 0  

Oyuncu2 = 0

oyun = 0

#Write a while loop and put the game inside

while oyun < kactur:

  #Add the code to select a random action for each player

  player1 = random.choice(List)
  player2 = random.choice(List)

  #Add the code to print the players choices

  print(f"\n Player-1 chose: {player1}, Player-2 Chose: {player2} \n")


  #Add the tie condition

  if player1 == player2:
    print("Oyun Berabere")
    oyun-=1

  #Add the remaining condition
  elif player1 == "Paper":
    if player2 == "Rock":
      print("Kağıt Taşı Yener {}".format(player1))
      Oyuncu1 = Oyuncu1 + 1
      
    elif player2 == "Scissors":
      print("Makas Kağıdı Keser. Kaybettin")
      Oyuncu2 = Oyuncu2 + 1
  elif player1 == "Scissors":
    if player2 == "Rock":
      print("Makas Taşa Kaybeder")
      Oyuncu2 = Oyuncu2 + 1
    elif player2 == "Paper":
      print("Makas Kağıdı Keser. Yendin") 
      Oyuncu1 = Oyuncu1 + 1       
  elif player1 == "Rock":
    if player2 == "Paper":
      print("Taş Kağıda Kaybeder. Kaybettin ")
      Oyuncu2 = Oyuncu2 + 1
    elif player2 == "Scissors":
      print("Taş Makası Yener. Yendin")
      Oyuncu1 = Oyuncu1 + 1      

  #print the score


  print("Skor Tablosu")

  print("Oyuncu-1: {}".format(Oyuncu1))

  print("Oyuncu-2: {}".format(Oyuncu2))

  

  oyun+=1

if Oyuncu1 > Oyuncu2:
    print(f"Oyunu: {Oyuncu1}  Kazandı:-)")
else:
    print (f"Oyunu: {Oyuncu2} Kazandı:-)")
