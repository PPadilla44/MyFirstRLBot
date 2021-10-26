from tools import  *
from objects import *
from routines import *


#This file is for strategy

class MyFirstRLBot(GoslingAgent):
    def run(agent):
        if len(agent.stack) < 1:
            agent.controller.boost = True





            # WAVE DASH
            # agent.push(wavedash())


            # GO TO BOOST
            # if agent.me.boost < 30:
            #     large_boosts = [ boost for boost in agent.boosts if boost.large and boost.active ]
            #     closest = large_boosts[0]
            #     closest_distance = (closest.location - agent.me.location).magnitude()
            #     for item in large_boosts:
            #         item_distance = (item.location - agent.me.location).magnitude()
            #         if item_distance < closest_distance:
            #             closest = item
            #             closest_distance = item_distance
            #     agent.push(goto_boost(closest, agent.ball.location))


            # SHORT SHOTS
            # agent.push(short_shot(agent.foe_goal.location))


            #FLIPS
            # relative_target = agent.foes[0].location - agent.me.location
            # agent.push(flip(agent.me.local(relative_target)))


            # JUMP SHOTS
            # targets = {"goal": (agent.foe_goal.left_post, agent.foe_goal.right_post)}
            # shots = find_hits(agent,  targets)
            # if len(shots['goal']) > 0:
            #     agent.push(shots['goal'][0])
            # else:
            #     relative = agent.friend_goal.location - agent.me.location
            #     defaultPD(agent, agent.me.local(relative))
            #     defaultThrottle(agent, 1410)


        # #An example of using raw utilities:
        # relative_target = agent.ball.location - agent.me.location
        # local_target = agent.me.local(relative_target)
        # defaultPD(agent, local_target)
        # defaultThrottle(agent, 2300)
        # agent.controller.boost = True
        


        # #An example of pushing routines to the stack:
        # if len(agent.stack) < 1:
        #     if agent.kickoff_flag:
        #         agent.push(kickoff())
        #     else:
        #         agent.push(atba())

