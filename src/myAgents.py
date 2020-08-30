
from pacman import Directions
from game import Agent, Actions
from pacmanAgents import LeftTurnAgent


class TimidAgent(Agent):
    """
    A simple agent for PacMan
    """

    def __init__(self):
        super().__init__()  # Call parent constructor
        # Add anything else you think you need here

    def inDanger(self, pacman, ghost, dist=3):
        """inDanger(pacman, ghost) - Is the pacman in danger
        For better or worse, our definition of danger is when the pacman and
        the specified ghost are:
           in the same row or column,
           the ghost is not scared,
           and the agents are <= dist units away from one another

        If the pacman is not in danger, we return Directions.STOP
        If the pacman is in danger we return the direction to the ghost.
        """



    
    def getAction(self, state):
        """
        state - GameState
        
        Returns the next action of pacman.

        If in danger, move
        """
        pacman = state.getPacmanState()
        ghosts = state.getGhostStates()
        heading = pacman.getDirection()

        legal = state.getLegalPacmanActions()
        # loop through each of the ghosts and evaluate whether there is danger
        # if there is danger, return the optimal direction to turn
        for ghost in ghosts:
            ghostDir = self.inDanger(pacman, ghost)
            # if ghost isnt in danger, check next ghost
            if self.inDanger(pacman,ghost) is Directions.STOP:
                continue

            if Directions.REVERSE[heading] in legal:
                return Directions.REVERSE[heading]
            elif Directions.LEFT[heading] in legal:
                return Directions.LEFT[heading]
            elif Directions.RIGHT[heading] in legal:
                return Directions.RIGHT[heading]
            elif heading in legal:
                return heading
            else:
                return Directions.STOP

        # if there is no danger from any ghosts

        # turn left
        if Directions.LEFT[heading] in legal:
            return Directions.LEFT[heading]
        # continue forward
        elif heading in legal:
            return heading
        # turn right
        elif Directions.RIGHT[heading] in legal:
            return Directions.RIGHT[heading]
        # turn around
        elif Directions.REVERSE[heading] in legal:
            return Directions.REVERSE[heading]
        else:
            return Directions.STOP

