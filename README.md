# Instructions

The following instructions assume that the python package virtualenvwrapper is installed for Python 3.

## Installation

Before doing anything else, create a virtual environment to run the programs in, and install the required packages:

```
mkvirtualenv <your environment name here>
cd <coding challenge code directory>
pip install -r requirements.txt
```

## Running the first task (display board)

```
cd <coding challenge code directory>
python 1_show.py <FEN string>
```

## Running the second task (make suggested move)

```
cd <coding challenge code directory>
python 2_move.py <FEN string>
```

## Running stretch code (combined)

```
cd <coding challenge code directory>
python stretch.py <FEN string>
```

## Running tests

The tests are in the 'tests' folder. I mostly ran them using pytest:

```
cd <coding challenge code directory>
PYTHONPATH=$(pwd) pytest
```

# Some notes

After doing both tasks and the stretch goal, I added functionality that updates aspects of the game state related to the other fields in the FEN file. Because of this, once a turn is taken, the other fields won't match the examples given in the challenge description. However, they should accurately represent the new game state after the turn has been taken.

I've written a lot of stubs for tests that I thought would be good for this project. There's a fair number of them, and I haven't implemented all of them, but I left the stubs to give an idea of thoughts I had about other tests that could be implemented.