#!/usr/bin/env python3
from pacman.capture import *
import pacman.captureGraphicsDisplay as captureGraphicsDisplay
from bots import baselineTeam
import pacman.layout as layout
import sys

if __name__ == '__main__':
    replay = sys.argv[1]
    display = captureGraphicsDisplay.PacmanGraphics("Red", "Blue", 1, 0, capture=False)
    import pickle
    with open(replay, 'rb') as f:
        recorded = pickle.load(open(replay, 'rb'))
        recorded['display'] = display
        replayGame(**recorded)
    sys.exit(0)


