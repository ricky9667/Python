import pandas as pd

def get_competitor_data(competitor):
    event_list = {"3x3x3 Cube":3, "2x2x2 Cube":4, "4x4x4 Cube":5, "5x5x5 Cube":6, "6x6x6 Cube":7, "7x7x7 Cube":8,
             "3x3x3 OH":9, "Clock":10, "Pyraminx":11, "Skewb":12, "Square-1":13}
    data = pd.read_csv("template.csv")

    template = data.values.tolist()
    for i in range(2,len(template)):
        if not (i == 11):
            event = template[i][1]
            event = str(event)
            event_index = event_list[event]
            template[i][2] =  competitor[event_index]
    return template

def main():
    data = pd.read_csv("competitor_list.csv")
    comp_list = data.values.tolist()
    competitors = [[]]

    for i in range(1, 128): # 127 competitors
        competitor = get_competitor_data(comp_list[i])
        size = len(competitor)
        competitors.append(["%02d" % i, comp_list[i][1]]) 
        print("Hi")
        for j in range(size):
            competitors.append(competitor[j])
        competitors.append([""])

    length = len(competitors)
    for i in range(length):
        print(competitors[i])

    # convert to .csv

if __name__ == "__main__":
    main()