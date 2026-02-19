import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    argc: int = len(sys.argv)
    if argc == 1:
        print("No score provided. usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list[int] = [0] * (argc - 1)
        count: int = 0
        i: int = 1
        while i < argc:
            try:
                scores[count] = int(sys.argv[i])
                count += 1
            except ValueError:
                print(f"Invalid score '{sys.argv[i]}' skipped")
            i += 1
        scores = scores[:count]
        if (len(scores)) == 0:
            print("No score provided. usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")

        else:
            print(f"total players: {argc - 1}")
            print(f"total score: {sum(scores)}")
            print(f"agerage score: {sum(scores) / len(scores)}")
            print(f"high score: {max(scores)}")
            print(f"low score: {min(scores)}")
            print(f"score range: {max(scores) - min(scores)}")
