import random
import pandas as pd

def get_bingo():
    num_chosen = [0]*50
    num_list = []
    while len(num_list) < 25:
        rand_num = random.randint(1, 40)
        if num_chosen[rand_num] == 0:
            num_list.append(str(rand_num))
            num_chosen[rand_num] = 1
    return num_list

def get_comp_list(n):
    competitors = [[]]
    max = int(input("Input max number: "))
    competitors[0] = get_bingo()
    for i in range(1, n):
        competitors.append(get_bingo())
    return competitors

def main():
    n = int(input("Input number of competitors: "))
    competitors = get_comp_list(n)
    
    data_frame = pd.DataFrame(competitors, columns = ["Bingo"] + [""]*24)
    data_frame.index += 1
    data_frame.to_csv("bingo_list.csv")
    
    for i in range(n):
        print(competitors[i])

if __name__=="__main__":
    main()