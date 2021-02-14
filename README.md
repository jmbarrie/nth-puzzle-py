# nth-puzzle-py

This is an AI project for University of California, Riverside's CS 170 (Intro to
Artificial Intelligence) course. It demonstrates the use of the A* algorithm 
for solving N-th size puzzles. 

## Usage
### Environment set up

It is recommend that a virtual environment be set up.

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install pytest
```

### Running it

Once the environment has been set up, the solver can be ran by simply calling

```
$ python3 driver.py
```

The first selection is for a default or custom puzzle. After, an algorithm can
be selected between Uniform Cost Search, A* with Misplaced Tile Heuristic, or A*
with Manhattan Distance Heuristic. 