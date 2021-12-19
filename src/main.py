from .utils import TabuSearch
import numpy as np


def main():
    tabu_obj = TabuSearch(np.array([1, 2, 3]))
    res = tabu_obj.tabu_search(3, tabu_obj.fun, 2, 10, 1000)

    print(res)


if __name__ == "__main__":
    main()
