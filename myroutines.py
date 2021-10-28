from typing import Counter
from objects import GoslingAgent
from routines import *
from utils import *


class kickoff_flip():

    def __init__(self, position):
        self.position = position
        self.counter = 0

    def run(self, agent: GoslingAgent):

        if self.counter == 0:
            kickoff_position = self.position

        target = agent.ball.location + Vector3(0, 75*side(agent.team), 0)
        local_target = agent.me.local(target - agent.me.location)

        agent.controller.boost = True
        defaultPD(agent, local_target)
        defaultThrottle(agent, 2300)
        mag = local_target.magnitude()

        # CORNER
        if mag < 2900 and mag > 2600 and kickoff_position == 2:
            agent.pop()
            agent.push(
                my_flip(agent.me.local(agent.ball.location - agent.me.location)))

        #  FAR MID
        if mag < 3600 and mag > 2500 and kickoff_position == 0:
            agent.pop()
            # flip towards opponent goal
            agent.push(
                my_flip(agent.me.local(agent.ball.location - agent.me.location)))

        #  CLOSE MID
        # TODO  GET BOOST
        if kickoff_position == 1:
            agent.pop()
            agent.controller.boost = True
            if agent.team == 0:
                agent.push(goto_boost(agent.boosts[7], target))
            else:
                agent.push(goto_boost(agent.boosts[26], target))

        if mag < 2000 and mag > 2200 and kickoff_position == 1:
            agent.pop()
            


            # flip towards opponent goal
            agent.push(
                my_flip(agent.me.local(agent.ball.location - agent.me.location)))

        # FLIP INTO BALL TOWARDS GOAL
        if mag < 350:
            agent.pop()
            # flip towards opponent goal
            agent.push(
                my_flip(agent.me.local(agent.foe_goal.location - agent.me.location)))


class my_flip():
    # Flip takes a vector in local coordinates and flips/dodges in that direction
    # cancel causes the flip to cancel halfway through, which can be used to half-flip
    def __init__(self,vector, cancel = False):
        self.vector = vector.normalize()
        self.pitch = abs(self.vector[0])* -sign(self.vector[0])
        self.yaw = abs(self.vector[1]) * sign(self.vector[1])
        self.cancel = cancel
        # the time the jump began
        self.time = -1
        # keeps track of the frames the jump button has been released
        self.counter = 0
    def run(self,agent):
        if self.time == -1:
            elapsed = 0
            self.time = agent.time
        else:
            elapsed = agent.time - self.time
        if elapsed < 0.10:
            agent.controller.jump = True
        elif elapsed >=0.10 and self.counter < 5:
            agent.controller.jump = False
            self.counter += 1
        elif elapsed < 0.15 or (not self.cancel and elapsed < 0.9):
            agent.controller.jump = True
            agent.controller.pitch = self.pitch
            agent.controller.yaw = self.yaw
        else:
            agent.pop()
            agent.push(recovery())