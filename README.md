# NIM_Project
Class project that will create a NIM mathematical game.

## What is NIM?
NIM is a mathematical game in which two players remove objects from a heap of objects. The name has many different origin theories.  The German word *nimm* means "take(imperitive)" or an obsolete English verb *nim* of the same meaning is most likely where the name originated. 

## How does this game work?
There are many variations of the game NIM.  Players in this particular game take turns with Dr. NIM.  The player can take from one to three objects at a time on their turn.  Dr. NIM takes his turn in the same fashion.  The player who leaves only one object is declared the winner.  **Dr. NIM will always win!!!!**

1. Why can the player never win?
  + The game is based on a system that takes the amount of moves and ensures the total count is offset by the minimum number of moves added to the maximum number of counter moves
  + The offset amount will ensure that Dr. NIM will make the last move and leaves only one object
2. WHAT!?!
  + Player 1 can take minimum number of one
  + Dr. NIM can take a maximum number of three
  + Our offset number will be four
  + Our total number of objects must be a multiple of four plus one
3. Why the plus one?
  + Since our offset number is four, we need a multiple of four to ensure every round takes a total of four objects
  + The plus one ensures that one objest will remain and Dr. NIM will win.
4. What if we increased the number Player 1 may take?
  + If Player 1 can take a maximum of 4 so can Dr. NIM
  + Minimum number of one plus the maximum number of four will result in an offset number of five
  + the total number of objects must be a multiple of five plus one
5. How does Dr. NIM decide how many to take?
  + Programming!!
  + Dr. NIM is programmed to take counter objects to make a total of offset objects required

## So what if Player 1 tries to cheat?
The python code is programed with certain rules in order to progress the game

1. The player must take 1, 2, or 3 objects
  + no taking negative objects (returning objects)
  + no taking zero objects
  + no taking more than allowed objects
2. The game will inform the player that he is cheating and repeat its last command
3. The game will continue until Player 1 makes a legal move

## Does the game require any software instalation to play?
Yes.  A version of Python 2.7 must be installed but the code does not require the python shell window to run.  A user can just open the file and the game will begin.

## How does a user change the game perameters (total objects, Dr. NIM's coding, etc)?
The python file will require to be open in IDLE in order to update or modify the file.
