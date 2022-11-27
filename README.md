# Algov

<h2>Methodology</h2>
<p>The code is broken up into four distinct sections/files:
<p>1. The Sorting Algorithms</p>
<p>2. The Search Algorithms</p>
<p>3. The Main Game Classes</p>
<p>4. The Menu Classes</p>
<h3>The Sorting Algorithms</h3>
<p>Within the Sorting.py file is a Node class, which is utilized to represent the bars of varying height contained within the sorted list, a List class 
that represents the list being sorted and contians methods that preform the sorting algorithms.</p>
<h3>The Search Algorithms</h3>
<p>The Search.py file contains a Node and Grid class that are used to build the grid on which the search algorithm is performed. The Grid Class also contains
the necessary methods to perform the search algorithms.</p>
<h3>The Main Game Classes</h3>
<p>The GameClass.py file contains the Game class which is responsible for initializing Menu/Sort/Search Objects and maintaining the game loop. The
Game class contains data/methods that are necessary for the operation of the game.</p>
<h3>The Menu Classes</h3>
<p>The Menu.py file contains all of the classes which represent the different menus. There is a main Menu class, which contains methods for updating the
screen and cursor locations, that is inherited by the Main, Sorting and Searching menus/gamestates. The three other classes function as different gamestates
and screens.</p>
<h2>Features</h2>
<h3>Sorting Algorithms</h3>
<p>The program features visualizations for the following sort algorithms:</p>
<p>1. Bubble Sort</p>
<p>2. Merge Sort</p>
<p>3. Quick Sort</p>
<p>4. Insertion Sort</p>

<h3>Searching Algorithms</h3>
<p>The program features visualizations for the following search algorithms:</p>
<p>1. A* Search</p>

<h2>How To Use</h2>
<p>Upon running the code, a pygame window will appear with a main menu that can be navigated by using the "W" and "S" keys.
The small star indicates the current menu selection. After selecting the desired menu option, clicking enter will update the game state and show
the desired algorithms. From here the user can select a sort algorithm or draw on the grid and begin the search algorithms. By clicking backspace the
user will be returned to the main menu.</p>
