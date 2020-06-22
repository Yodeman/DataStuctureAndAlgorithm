class GameEntry:
    """Represents one entry of a list of high scores."""
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)

class Scoreboard:
    """Fixed-length sequence of high scores in nondecresing order."""
    def __init__(self, capacity):
        """
        Initialize scoreboard with given maximum capacity.
        All Entries are initially None.
        """
        self._board = [None]*capacity
        self._n = 0

    def add(self, entry):
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()
        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() <  score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry

    def __getitem__(self, k):
        """Return entry at index k."""
        return self._board[k]

    def __str__(self):
        return "\n".join(str(self._board[j]) for j in range(self._n))

if __name__ == "__main__":
    entry = {"Michael":1000, "Paul":2500, "Lydia":3000, "Mary":3500, "Peter":200}
    game_entry = [GameEntry(k,v) for (k,v) in entry.items()]
    score_board = Scoreboard(10)
    for obj in game_entry:
        score_board.add(obj)
    print(score_board)
