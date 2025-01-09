import statistics

def main():
    user_input = input("Enter a list of numbers separated by commas: ")
    user_input = user_input.split(",")
    user_input = [float(i) for i in user_input]

    print("Mean: ", statistics.mean(user_input))
    print("Median: ", statistics.median(user_input))
    print("Mode: ", statistics.mode(user_input))
    print("Standard Deviation: ", statistics.stdev(user_input))

if __name__ == "__main__":
    main()

