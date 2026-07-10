if __name__ == "__main__":
    new_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        new_list.append([name, score])
    scores = [student[1] for student in new_list]
    unique_sorted_scores = sorted(list(set(scores)))
    second_lowest = unique_sorted_scores[1]
    two_low = []
    for student in new_list:
        if student[1] == second_lowest:
            two_low.append(student[0])

    two_low.sort()
    for name in two_low:
        print(name)
