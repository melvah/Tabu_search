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
        ), f"""The length of goal must be equal to "length". The length of the goal is {len(self.goal)} but the length is {len(solution)}
        Please initialize the Tabu Search object with another vector with length {len(solution)}."""

        cost = abs(np.subtract(self.goal, solution).sum())
        return cost

    def tabu_search(
        self, length: int, fun, list_size: int, num_iter: int, time_out: int
    ):
        ini_solution = self.initialSolution(length)
        current_solution = ini_solution
        best_solution = ini_solution
        cost_ini = fun(ini_solution)
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

                # for value in tabudict.values():

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

            del tabulistKey[0]
            end = time.time()
            time_exec = int(end - start)

            if time_exec >= time_out:
                print("TimeOut")
                time_flag = False
                break
        return best_solution
