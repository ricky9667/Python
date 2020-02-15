import random as r
import pandas as pd


def get_25_diff_num_list(_max):
    return r.sample([x for x in range(1, _max + 1)], k=25)


def get_comp_list(n):
    _max = int(input("Input max number: "))
    return [get_25_diff_num_list(_max) for x in range(n)]


def main():
    n = int(input("Input number of competitors: "))
    competitors = get_comp_list(n)
    data_frame = pd.DataFrame(competitors, columns=["Bingo"] + [""] * 24)
    data_frame.to_csv("bingo_list.csv")
    print(data_frame.to_string(index=False))


if __name__ == "__main__":
    main()
