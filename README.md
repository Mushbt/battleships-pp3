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
  - Testing has also been done by myself, my friends, my family and within the Slack Community. There are no known issues that cause the application to crash.

# PEP8 Validation
  - Code was run though the Code Institute PEP8 Validator and below are the screenshots of the results.
  - Most of the errors were trailing white lines or 1 blank line rather than 2 under functions. These were all resolved.
  - The remaining errors are because of the logo and do not cause the code to break.

![PEP8 Validator errors](insert image here)
![PEP8 Validator errors](insert image here)
![PEP8 Validator after errors are fixed](Insert image here)

# Bugs
## Resolved
  - The game would end directly after the player has taken their first turn. This was resolved by reindenting my code underneath a while loop and then adding an if condition.
  - There was an issue with the ships printing on both boards. The ships were printing on the computers board which should not happen and the ships on the players board were appearing after the computer has taken its first turn. This was fixed by reindenting my code underneath a while loop.
  - During the game, when trying to hit computers ships, it always showed I did not hit any ships at all but then all of a sudden I have sunk all the computers ships and won.
  This was fixed by adding a print ship function to the computers board. This led to another issue of the ships on the computers board being visible. I then had to edit my code within the print board function so that '@'(Ships) would be replaced with ' ' which led to all ships on the computer board being hidden.
  - The player was targeting their own board. This was fixed by redoing my start game function and going through each step at a time while putting the code in the order the game should be played out. Code was also reindented underneath a while loop.

## Unresolved
  - There are no known unresolved bugs to mention.

[Back to top](<#Table of Contents>)

# Deployment
* The app was deployed via Heroku and the live link can be found here [Battleships Game](insert link here)
  - To deploy the project through Heroku, the following steps were taken:
    - Sign up / Log in to [Heroku](https://www.heroku.com/)
    - From the main Heroku Dashboard, press the 'New' button and then press on the 'Create New App' button.
    - Give the project a name (Needs to be a unique name) and then select the region that is suitable to you. After this is done, press on the 'Create App' button.
    - Once the app has been created, you will be redirected to the deploy section. Using the submenu at the top, press on the settings button.
    - Once on the settings page, scroll down a to the 'Config vars' section. Once located, press on the 'Reveal congfig vars' button. This will reveal the current config vars for the app. There should not be any vars configured beforehand.
    - In the KEY input field, input PORT in capital letters and in the VALUE field, input 8000. Then click on the 'Add' button. This needs to be done for the Code Institute template. If you are not using the CI template, you may not need to do this.
    - Next, you need to click on the 'Add buildpack' button below. This should trigger a popup. Select Python as your first buildpack and press on the 'save changes' button.
    - Repeat the above step but this time select Node.js as the buildpack. The order of the buildpacks is important. Python should be first and Node.js second. If you accidently do them in the wrong order, you can click on either buildpacks and drag them to put them in the correct order.
    - Next, you need to navigate to the deploy page which you can do from the submenu at the top of the page.
    - Once on the deploy page, look for the deployment method section and press on the Github logo. Once done, a small section should appear underneath. Click on the 'Connect to GitHub' button. On your first time doing this, you may be promted to follow some steps which you should do.
    - Once done, a 'Connect to GitHub section should appear. Here you will need to search for the repository you want to connect to. You can either type in the repository name in the input field and press search or you can just press search right away and a list of all your repositories should appear and you can press on the one you would like to connect to. Once you have have found the repository you would like to connect to, press on the 'Connect' button on the right hand side.
    - Now that your app has been connected to GitHub, double check the 'Choose a branch deploy' drop down menu is deploying the correct branch from your GitHub Repository. Once you are sure, you need to decide if you would like to enable automatic deploys via the 'Enable Automatic Deploys' button below or if you would like to deploy it manually everytime. The difference is, with automatic deploy, your app will be updated automatically everytime you push the changes in GitHub where as with manual deploy, you will need to go back to the deploy page everytime you want to update the app with the changes. I prefer for it to be automatically done but it is entirely upto you.
    - Once you have decided how you want the deploys to be, press on the deploy branch below. Heroku will now build the app for you. Once it has been completed, a 'Your App Was Successfully Deployed' message will appear with a link the live site.

[Back to top](<#Table of Contents>)

# Credits
- Inspiration for my battleships game came from [Copyassignment](https://copyassignment.com/battleship-game-code-in-python/)
- GitHub template came from [Code Institute](https://codeinstitute.net)
- Colors used in my repository came from [Gist][gist.github.com/minism/1590432]
- I was able to solve some of the bugs I encountered by searching on [Stack OverFlow](https://stackoverflow.com/)
- The tutors at [Code Institute](https://codeinstitute.net) for always being there when ever I was stuck. A special thank you to Rebecca for being patient and really taking her time to help me find where my code was breaking!
- The [Slack Community](https://slack.com) for also helping me resolve bugs and for testing my app throughout!
- My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for giving me great feedback on how to improve my game!

[Back to top](<#Table of Contents>)

This game was done as part of my project piece for my Full Stack Software Development Diploma at the [Code Institute](https://codeinstitute.net).
Mustafa Habet 2023

