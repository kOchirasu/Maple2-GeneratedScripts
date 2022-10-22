""" trigger/82000002_survival/220_boat.xml """
from common import *
import state


#  맵 외곽 동선 
class BoatPatrol(state.State):
    def on_enter(self):
        npc_to_patrol_in_box(boxId=9520, npcId=11400001, spawnId='interactObject', patrolName='MS2PatrolData_220')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=200):
            return BoatPatrol()

