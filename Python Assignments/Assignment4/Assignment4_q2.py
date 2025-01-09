def main():
    voters = set()
    votes = {}

    while True:
        print("\nVoting System: ")
        print("1. Cast Vote")
        print("2. View Vote Counts")
        print("3. Exit")
        choice = input("Enter your choice(1-3): ").strip()

        if choice == '1':
            voter_id = input("Enter your voter ID: ").strip()
            if voter_id in voters:
                print("You have already voted.")
            else:
                candidate = input("Enter the candidate name for you want to vote: ").strip()
                voters.add(voter_id)
                if candidate in votes:
                    votes[candidate] += 1
                else:
                    votes[candidate] = 1
                print(f"Vote cast for {candidate}.")
        elif choice == '2':
            if not votes:
                print("No votes have been cast yet.")
            else:
                print("\nVote Counts: ")
                for candidate, votes in votes.items():
                    print(f"{candidate}: {count} vote(s)")
        elif choice == '3':
            print("Exciting the voting system.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()