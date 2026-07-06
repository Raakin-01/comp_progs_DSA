if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    # 1. Convert the map object into a usable list
    scores_list = list(arr)

    # 2. Remove all duplicates by converting it to a set
    unique_scores = set(scores_list)

    # 3. Remove the absolute highest score
    unique_scores.remove(max(unique_scores))

    # 4. The new highest score is now the runner-up!
    runner_up = max(unique_scores)

    print(runner_up)
