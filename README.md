# TicTacToe
First of all you need to install pygame in your python console by typing: 'pip install pygame', then you're ready to compile this code.
This's a simple Python script for the game "TicTacToe" for two players. I used pygame for the nice graphics. Now I'll explain my functions I wrote in this game. You have all rights for using these files.

printMouse(turn): This function prints out the Mouse Pointer. There're 2 diffrent ones. Both are in the folder "Graphics".
printChart(): This function prints out the Chart, including the X and O from the game.
printX(x, y): This function prints out one X with the x and y coordinates from the point in the center.
printO(x, y): This function prints out one O with the x and y coordinates from the point in the center.
setOX(): This function returns which field in the game is selected.
noOX(posi): This function checks if this field is free, so if there is no O or X.
getx(posi): This function returns the x coordinate of a position give as posi.
gety(posi): This function returns the y coordinate of a position give as posi.
checkWin(): This function checks if anyone in this game won.
