import random as r
import pandas as pd


def get_25_diff_num_list(_max):
    return r.sample([x for x in range(1, _max + 1)], k=25)


def get_comp_list(n):
    _max = int(input("Input bingo number: "))
    competitors = []
    
    for num in range(0, n):
        rand_list = get_25_diff_num_list(_max)
        index = num*5
        
        for i in range(5):
            if i == 0:
                tmp = [("%03d") % (num+1)]
            else:
                tmp = [""]
            for j in range(5):
                tmp.append(str(rand_list[5*i+j]))
            competitors.append(tmp)
    return competitors


def main():
    n = int(input("Input number of competitors: "))
    competitors = get_comp_list(n)
    data_frame = pd.DataFrame(competitors, columns=["Number", "Bingo"] + [""] * 4)
    data_frame.to_csv("bingo_list.csv", index=False)
    print(data_frame.to_string(index=False))


if __name__ == "__main__":
    main()
