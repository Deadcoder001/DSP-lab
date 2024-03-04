from collections import Counter

def find_winner(votes):

    vote_counter = Counter(votes)

    winner = max(vote_counter, key=vote_counter.get)

    return winner

votes = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'D']

winner = find_winner(votes)

print(f"The winner of the election is: {winner}")
