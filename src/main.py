from .utils import TabuSearch
import numpy as np


def main():
    goal = np.array([1, 2, 3])
    tabu_obj = TabuSearch(goal=goal)  # object from the the tabu search class
    res = tabu_obj.tabu_search(
        3, tabu_obj.fun, 1, 20000000, 10
    )  # tabu search method applied on tabu_obj

    print(
        f"""Tabu search is trying to find the closest binary vector solution in terms of 
        distance to the goal vector.
        ------------------------------------------------------------------------\n
        goal vector = {goal}
        binary solution = {res}"""
    )


if __name__ == "__main__":
    main()
