# Hanabi assistant

This is an assistant that records hints about each tile, and tells you the probabilities of what each tile is.
Hanabi is available to play against humans and AIs at https://hanabi.cards/.

This was a project for me to learn about object oriented programming, writing tests, and type checking.

## Usage
Sorry, this isn't very user-friendly.

1. Run `ipython -i assistant.py`.

1. Upon starting a game, add all the seen cards to `initial` and load them into the `seen` matrix.
For example, if at https://hanabi.cards/, you pick seed 9178 under advanced options with 4 players, these are the initial conditions.
```
initial = [ "4b", "5g", "1y", "2g", "1b", "1y", "3b", "1w", "3g", "5y", "2y", "1b" ]

for tile in initial:
    add_new_sighting(tile, seen)
```

2. Run `h.probs(seen)` to see the probability matrices for each tile.

3. Play your turn.

3. After your turn, if you play a tile, run `h.drop_tile(i)` where `i` is the the 0-based indexed of the played tile.

4. Run `add_new_sighting` a bunch of times after other players complete their turn to update `seen` matrix.

5. Repeat.
