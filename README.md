# Tabu search

Tabu search is a metaheuristic  technique designed to solve problems with an approximate solution when classic methods fail to find an exact solution 
in a reasonable amount of time 
(NP-hard problems).  Tabu search escapes from a local optimum by allowing flexible movements. The Tabu search selects a new search movement in such a way that temporally forbids the evaluation of previous solutions. 


## Tabu search algorithm
* Creating an initial solution.
* Creating neighbour solutions
* Evaluation of a solution (cost function).
* Adding the solution to the Tabu list based on the tabu list size.
    * Tabu list: is the instrument that lends a short-to-medium size memory to the algorithm. The List “remembers” and disables movements from previous searches. These disabled movements are referred to as Tabu Moves.
    * Tabu list size is the number of iterations that a Tabu list disables the tabu moves.
* Sometimes the tabu moves are allowed, based on certain constraints. For example, if the given move allows a new global best solution and all allowed moves are worse than the actual one. 
In thses situations the move is accepted.

# Project tree 
```
.
├── README.md
├── requirements.txt
└── src
    ├── main.py
    └── utils.py
```    

# Steps to  run the code

Please follow these steps to run the code, all the codes are written in python=3.8

* Make sure you are inside the project directory (Tabu_search folder)
* Install the `requirements.txt` file.
```
pip install -r requirements.txt
```
* You can run the main file of the project (`main.py`) as follows:
```
python -m src.main
```

