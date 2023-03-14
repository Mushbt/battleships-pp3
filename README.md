# Battleships

Battleships is a Python terminal game which runs on Heroku. It is based on the popular strategy type guessing game [Battleships](https://en.wikipedia.org/wiki/Battleship_(game)).
Players will play against the computer, and the game aim is to guess where the computer has placed its ships on the 8x8 board/grid and try and sink them. The computer will also be trying to do the same. Players and the computer will have 5 ships each which consists of the following:
- Destroyer (Takes up 2 board positions)
- Submarine (Takes up 3 board positions)
- Cruiser (Takes up 3 board positions)
- Battleship (Takes up 4 board positions)
- Carrier (Takes up 5 board positions)
Players will choose where to place their ships whilst the computers ships will be located randomly. Players will get to choose if they want their ships positioned Horizontally or Vertically. They will then decide where to place their ships using coordinates on the side of the board.
Once the player or the computer sink the opponents ships, the game will end.

The live link can be found here - [Battleships](Enter game link here)

![readme hero image](add hero image here)

## Table of Contents
* [How to Play](#How-To-Play)
* [Features](#Features)
 * [Existing Features](#Existing-Features)
 * [Future Features](#Future-Features)
* [Design](#Design)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits And Acknowledgements](#credits-and-acknowledgements)

## How To Play

- 5 ships will be placed on each board automatically.
- When all ships have been placed, the game will begin.
- The player must try and guess where the computers ships are located using coordinates.
- If the player can sink all the computers ships before theirs are sunk, they will win the game.

[Back to top](<#Table of Contents>)

## Features
# Existing Features
- The Introduction
  - When a new game is started, a Battleships logo is printed.
  - After the logo is printed, a simple welcome message which reads "Welcome to Battleships!" follows.
  - User will also get information on what the Battleships game is and instructions on how to play.
  - User will also get information on all the ship sizes and names that will be used in the game.
  - User will also get a game legend which tells them what the symbols in the game will be.

![Battleships logo](Insert logo image here)
![Welcome message](Insert welcome message image here)
![Battleships instructions and how to play](Insert instructions image here)
![Ship sizes and names](Insert ship info image here)
![Legend](Insert Legend image here)

[Back to top](<#Table of Contents>)

- Players board
  - The players board will have letters and numbers on the x and y axis respectively. These will be the game coordinates for the game.
  - The players ships will be visible. Ships have been randomly placed.
- Computers board
  - The computers board will have letter and numbers on the x and y axis respectively. There will be the game coordinates for the game.
  - The computers ships will not be visible. Reason for this is because the player will need to guess where the ships are located. Ships have been randomly placed.

![Players board](Insert players board image here)
![Computers board](Insert computers board image here)

[Back to top](<#Table of Contents>)

- Legend Display
  - Ships that have not been hit on the players board are displayed as a "@"
  - Ships that have been hit on both the players and computers boards are displayed as a "X"
  - Missed hits are displayed as a "O" on both the players and computers board

![Players board during game](Insert players board image here during gameplay)
![Computers board during game](Insert computers board image here during gameplay)

[Back to top](<#Table of Contents>)

- Player feedback
  - Feedback is constantly displayed to the player during the game
  - The player is requested to input coordinates whenever they have their turn. They are asked for the y axis first, which are numbers.
  If they do not input a number between 1 and 8, they get asked to input a valid number between 1 and 8. Once done right, they are asked to input coordinates
  for the x axis which are letters. If they do not input a letter between A and H, they are asked to input a valid letter between A and H. The player takes their turn once
  the coordinates are input correctly. The computer takes its turn directly after.
  - Once the player and computer have taken their turns, feedback is given to the player. The feedback is telling the player if they hit or missed the computers ship. They
  also get feedback telling them if the computer has hit or missed their ship.
  - Player will also get feedback once the game has ended. The feedback will be telling the player they have either one or lost.

![Y axis request](insert image here of y axis request)
![Y axis feedback](insert image here of y axis feedback if incorrect)
![X axis request](insert image here of x axis request)
![X axis feedback](insert image here of x axis feedback if incorrect)
![Player hit image](insert player hit image here)
![Player miss image](insert player miss image here)
![Computer hit image](insert computer hit image here)
![computer miss image](insert computer miss image here)
![Game end image](insert game end image here)

[Back to top](<#Table of Contents>)

- Play again
  - When the player or the computer has sunk the opponents ship, the game will end.
  - Once game has ended, the player will be asked if they want to play again. Player will need to input Y for yes or N for no.
  - If the player decides to play again, the game will reload from the begining.
  - If the player decides against playing again, they will get a goodbye message.

![Play again image](insert play again image here)
![goodbye message](insert goodbye message here)

[Back to top](<#Table of Contents>)

# Future Features
- In the future, I would like to add the following features
  - Add a username input which would ask the player to create a username for the game
  - Add a highscore table which would go hand in hand witht he username input feature. The scoreboard can be used for how many hits it took to win the game.
  - Add difficulty levels that the player can choose from.
  - Allow the player to position their ships.
  - Allow the player to choose the size of the grid.

[Back to top](<#Table of Contents>)

# Design
* When thinking about the design for this project, I had a look at various examples online and thought it would be good to keep it simple 
seeing as it was going to be a game on a terminal which normally consists of a simple black background and white text. I did however, decide to add abit of color for better 
UX for the player.
- I made the battleships logo at the beginning red which I thought was a subtle color that went nicely with the black background.
- Before the game has started, I have given the player information on the ships and their lengths that they will have during the game. I have colored the ship names in different colors, this was to differentiate between the different ships and I felt makes it easier for player to see the differences.
- During the game, the player gets feedback on if they have hit or missed any ships aswell as feedback if their ships have been hit or missed. If the player hits a ship, the feedback will be in green which is normally attributed to something positive or a go sign. If the players ships have been hit, the feedback will be in red which is normally attributed to something bad or danger. The feedback for hitting empty waters for both the player and computer, I have chosen the color blue which is the color of the ocean.
- At the end of the game, if the player has won, the feedback given is in green and if the player loses feedback will be in red, which as before during the game I felt it would be the colors attributed with such outcomes.

[Back to top](<#Table of Contents>)

# Technologies
* Languages
  - Python - Provides the functionality for the application

* Frameworks & Software
  - Github - Used to host and edit the application
  - Gitbash - Terminal in Gitpod used to push changes to the Github Repository.
  - Heroku - A cloud platform that the application is deployed to.

* Python Packages
  - Sys - This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. ([https://docs.python.org/3/library/sys.html#:~:text=This%20module%20provides%20access%20to,It%20is%20always%20available.])
  - Time - A module that provides various time-related functions.

[Back to top](<#Table of Contents>)

# Testing
  - Testing and debugging has been performed throughout the building phase via the gitpod terminal. Proof of this is within the commits.
  - Tested in the gitpod terminal and CI Heroku terminal.
  - Testing has also been done by myself, my friends, my family and within the Slack Community. There is no known issues that cause the application to crash.