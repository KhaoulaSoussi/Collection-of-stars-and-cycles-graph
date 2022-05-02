# Collection-of-stars-and-cycles-graph

## Description of the problem
This project was assigned in Analysis of Algorithms class with Dr. Naeem Nisar Sheikh. 
The program checks if a graph is a collection of stars and cycles and displays the number of stars and cycles in it.

## Proposed Solution
The program reads from an input file the number of vertices, the number of edges, and the edges themselves. 
I created four input files to test different cases, and of course you can create another file of yours that has the same format as the other files.
In the program, the file name is set by default to "inp.txt"; if you would like to change it to another file, just replace the file name in statement line 14 with the name of the desired file. 

Here are details about the content of each file: 
inp.txt ==>   
	A star of size 3 centered at vertex 1; a star of size 3 centered at vertex 10
	A cycle of size 4 starting at vertex 3; a cycle of size 3 starting at vertex 12;
inp2.txt ==>
	Not a collection of stars and cycles because a potential star center (vertex 1) is connected to a non-degree-1 vertex
inp3.txt ==>
	A star of size 3 centered at vertex 1; a star of size 4 centered at vertex 5
	Zero cycles
inp4.txt ==>
	Zero stars
	A cycle of size 4 starting at vertex 1; a cycle of size 5 starting at vertex 4


Done on April 30th, 2021
