import random
import numpy as np
import time


class TabuSearch:
    def __init__(self, goal: np.array) -> None:

        self.goal = goal

    def initialSolution(self, length: int) -> np.array:
        initial_solution = np.random.choice([0, 1], size=(length,))

        return initial_solution

    def generatingSolution(self, solution: np.array) -> np.array:
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
        assert len(solution) == len(
            self.goal
        ), """The length of goal must be equal to length\n
        Please initialize the Tabu Search object with another vector"""

        cost = abs(np.subtract(self.goal, solution).sum())
        return cost

    def tabu_search(
        self, length: int, fun, list_size: int, num_iter: int, time_out: int
    ):
        ini_solution = self.initialSolution(length)
        best_solution = ini_solution
        cost_ini = fun(ini_solution)
        best_cost = cost_ini
        tabulist = []
        tabulist.append(ini_solution)
        max_iter = True
        time_flag = True
        start = time.time()
        iter = 0
        while max_iter or time_flag:
            while len(tabulist) <= list_size:

                new_solution = self.generatingSolution(ini_solution)
                iter += 1
                if np.all(new_solution) not in tabulist:
                    tabulist.append(new_solution)
                    new_cost = fun(new_solution)
                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_solution = new_solution
                        if iter == num_iter:
                            max_iter = False
                            return best_solution

            del tabulist[0]
            end = time.time()
            time_exec = int(end - start)
            if time_exec >= time_out:
                time_flag = False
        return best_solution
