import random
import numpy as np
import time


class TabuSearch:
    def __init__(self, goal: np.array) -> None:
        """Initializing the class by the vector that we want the mimimum distance from

        Args:
            goal (np.array): [The goal must be a vector with the same length as
            the parameter length for the tabu search]
        """

        # goal is the target to minimize the distance for
        self.goal = goal

    def initialSolution(self, length: int) -> np.array:
        """This function initializes a random solution to the problem
        by creating a binary vector (array) with the given length.

        Args:
            length (int): [The length of the initial solution ]

        Returns:
            np.array: [The random binary vector with the given length
            (initial solution)]
        """
        initial_solution = np.random.choice([0, 1], size=(length,))

        return initial_solution

    def generatingSolution(self, solution: np.array) -> np.array:
        """Generating neighbourhood solutions based on a given solution
        by flipping only one element of the current solution.

        Args:
            solution (np.array): [The current solution]

        Returns:
            np.array: [The generated solution]
        """
        _solution = solution.copy()

        length_sol = len(_solution)
        idx = random.randint(0, length_sol - 1)
        if _solution[idx] == 1:
            _solution[idx] = 0

            return _solution
        else:
            _solution[idx] = 1

            return _solution

    def fun(self, solution):
        """Objective function to evaluate solutions. This function
        finds the absolute distance of two vectors (the new solution and
        the current solution) by |current_solution - new_solution|.sum()

        Args:
            solution (np.array): [The current solution]

        Returns:
            np.array: [The generated solution]
        """
        assert len(solution) == len(
            self.goal
        ), f"""The length of goal must be equal to "length". The length of the goal is {len(self.goal)} but the length is {len(solution)}
        Please initialize the Tabu Search object with another vector with length {len(solution)}."""

        cost = abs(np.subtract(self.goal, solution)).sum()
        return cost

    def tabu_search(
        self, length: int, fun, list_size: int, num_iter: int, time_out: int
    ):
        """The main function that does the tabu search

        Args:
            length (int): [The length of the vector solutions]
            fun ([type]): [Objective functions to evaluate solutions]
            list_size (int): [The size of the tabu list (tabu tenture)]
            num_iter (int): [Maximum number of iterations]
            time_out (int): [Time limit for running the tabu search in seconds]

        Returns:
            best_solution (np.array): [The best solution]
        """
        # initializing a solution
        ini_solution = self.initialSolution(length)
        # Assigning the initial solution as the current solution and
        # the best solution.
        current_solution = ini_solution
        best_solution = ini_solution
        # Fining the cost for the initial solution
        cost_ini = fun(ini_solution)
        # Setting the initial cost as the best cost
        best_cost = cost_ini

        tabulistKey = []
        tabulistKey.append(0)
        tabudict = {}
        tabudict[0] = ini_solution
        max_iter = True
        time_flag = True
        start = time.time()
        iter = 0
        while max_iter or time_flag:
            if iter == num_iter:
                print("maximum number of iterations reached")
                max_iter = False
                return best_solution

            while len(tabulistKey) <= list_size:

                new_solution = self.generatingSolution(current_solution)

                iter += 1

                if not (abs(np.subtract(tabudict[iter - 1], new_solution))).all():

                    tabudict[iter] = new_solution
                    current_solution = new_solution

                    tabulistKey.append(iter)

                    new_cost = fun(current_solution)
                    if new_cost < best_cost:

                        best_cost = new_cost
                        best_solution = current_solution
                        if iter == num_iter:

                            max_iter = False
                            return best_solution
                else:
                    break
            # Tabu list is full
            # remove the first elemen to fthe tabu list
            del tabulistKey[0]
            end = time.time()
            time_exec = int(end - start)

            if time_exec >= time_out:
                print("TimeOut")
                time_flag = False
                break
        return best_solution
