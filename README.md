# Hanabi assistant

This is an assistant that records hints about each tile, and tells you the probabilities of what each tile is.
Hanabi is available to play against humans and AIs at https://hanabi.cards/.

## Usage
Sorry, this isn't very user-friendly.

1. Run `ipython -i assistant.py`.

1. Upon starting a game, add all the seen cards to `initial` and load them into the `seen` matrix:
```
initial = [ "1r", "3y", "2g", "3b", "1w", "2w", "4r", "3g", "2r", "2b", "2r", "4b" ]

for tile in initial:
    add_new_sighting(tile, seen)
```

2. Run `h.probs(seen)` to see the probability matrices for each tile.

3. Play your turn.

3. After your turn, if you play a tile, run `h.drop_tile(i)` where `i` is the the 0-based indexed of the played tile.

4. Run `add_new_sighting` a bunch of times after other players complete their turn to update `seen` matrix.

5. Repeat.
