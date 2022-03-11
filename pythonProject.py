#!/usr/bin/python3

import requests
from game_data import data
import random
from art import logo, vs

def main():
    #while loop for entry of favorite NBA Player
    while True:
        favorite_player = input("Enter the name of your favorite NBA Player: \nEnter 'IDK' if you need more information\n")
        #if statement to provide user with list of NBA Allstars to choose from
        if favorite_player == "IDK":
            
            #print llist of NBA Allstars to screen for user to review
            print(f"Here are the top players in the NBA: {all_stars}")
        else:
          # define base URL
            URL = f"https://balldontlie.io/api/v1/players?search={favorite_player}"
            # Make HTTP GET request 
            player_data = requests.get(f"{URL}")
            player_data = player_data.json()
            player_data = player_data.get("data")

            # information pulled to describe a given player
            first_name = player_data[0].get("first_name")
            last_name = player_data[0].get("last_name")
            name = ' '.join([first_name, last_name])
            height_feet = str(player_data[0].get("height_feet"))
            height_inches = str(player_data[0].get("height_inches"))
            height = ' feet '.join([height_feet, height_inches])
            position = player_data[0].get("position")
            team = player_data[0].get("team")
            team_name = team.get("full_name")
            team_id = team.get("id")

             # information pulled to describe a given team
            TEAMURL = f"https://balldontlie.io/api/v1/teams/{team_id}"
            team_data = requests.get(f"{TEAMURL}")
            team_data = team_data.json()
            city = team_data.get("city")
            conference = team_data.get("conference")
            division = team_data.get("division")
            
            #prompt user with second question
            #dive into player information, team information, or play a game
            answer = ""
            while True:
                answer = input(f"Do you want to: \nA) Learn more about {name}... \nB) Learn more about his team, The {team_name}... \nC) Choose another NBA Player \nD) Play the Higher/Lower game, comparing NBA Stars points per game...\n")
                if answer == "A":
                    print(f"Player Data: \nFirst Name: {first_name} \nLast Name: {last_name} \nHeight: {height} \nPosition: {position} \nTeam:{team_name}")
                elif answer == "B":
                    print(f"Team Data: \nCity: {city} \nConference: {conference} \nDivision: {division}")
                elif answer == "C":
                    break
                elif answer == "D":
                    def get_random_player():
                      #Get data from random player
                      return random.choice(data)

                    def format_data(player):
                      #Format player's info into printable format: name, position and team
                      name = player["name"]
                      position = player["position"]
                      team = player["team"]
                      # print(f'{name}: {player["points_per_game"]}')
                      return f"{name}, plays the {position} position, for the {team}"

                    def check_answer(guess, a_points, b_points):
                      #Checks points against user's guess and returns True if they got it right.Or False if they got it wrong. 
                      if a_points > b_points:
                        return guess == "a"
                      else:
                        return guess == "b"


                    def game():
                      print(logo)
                      score = 0
                      game_should_continue = True
                      player_a = get_random_player()
                      player_b = get_random_player()

                      while game_should_continue:
                        player_a = player_b
                        player_b = get_random_player()

                        while player_a == player_b:
                          player_b = get_random_player()

                        print(f"Compare A: {format_data(player_a)}.")
                        print(vs)
                        print(f"Against B: {format_data(player_b)}.")
                        
                        guess = input("Who has more points? Type 'A' or 'B': ").lower()
                        a_points_per_game = player_a["points_per_game"]
                        b_points_per_game = player_b["points_per_game"]
                        is_correct = check_answer(guess, a_points_per_game, b_points_per_game)

                        print(logo)
                        if is_correct:
                          score += 1
                          print(f"You're right! Current score: {score}.")
                        else:
                          game_should_continue = False
                          print(f"Sorry, that's wrong. Final score: {score}")

                    game()
                else:
                    print("Incorrect Input. Please enter A, B, C or D")
all_stars = "Lebron James\n Giannis Antetokounmpo\n Steph Curry\n DeMar Derozan\n Nikola Jokic\n Joel Embid\n Ja Morant\n Jayson Tatum\n Trae Young \n Luka Doncic\n"
        


if __name__ == "__main__":
    main()