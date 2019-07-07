#!/usr/bin/env python3
import argparse
from pacman.capture import *
import pacman.captureGraphicsDisplay as captureGraphicsDisplay
import pacman.layout as layout

def parse_args():
    parser = argparse.ArgumentParser(description="Helper file to run a bot")
    parser.add_argument("--redBot", type=str, help='Module name of the red bot', default="MyBot")
    parser.add_argument("--blueBot", type=str, help='Module name of the blue bot', default="MyBot")
    parser.add_argument("--layout", type=str, help='Name of the layout (in the layouts directory or "random"', default="RANDOM")
    parser.add_argument("--numGames", type=int, help='Number of games to be played', default=1)
    parser.add_argument("--gameLength", type=int, help='Length of a game', default=1000)
    parser.add_argument('--seed', type=str, help='Seed to set randomness', default=None)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    redBot = __import__(args.redBot).createTeam
    blueBot = __import__(args.blueBot).createTeam

    display = captureGraphicsDisplay.PacmanGraphics(args.redBot, args.blueBot, 1, 0, capture=True)
    agents = sum([list(el) for el in zip(redBot(0, 2, True), blueBot(1, 3, False))],[])

    options = {
        'agents': agents,
        'display': display,
        'length': args.gameLength,
        'numGames': args.numGames,
        'record': True,
        'numTraining': 0,
        'redTeamName': args.redBot,
        'blueTeamName': args.blueBot,
        'muteAgents': False,
        'catchExceptions': True,
        'seed': args.seed,
        'layout': args.layout
    }

    games = runGames(**options)
    print('Score: %d' % games[0].state.data.score)
