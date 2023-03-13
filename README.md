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

[Back to top](<#Table of Contents>)

