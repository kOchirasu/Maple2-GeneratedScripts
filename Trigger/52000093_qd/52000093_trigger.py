""" trigger/52000093_qd/52000093_trigger.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3003,3004], visible=False)
        destroy_monster(spawnIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008])

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9100], questIds=[50100490], questStates=[1]):
            return 진행중일때20002274()
        if quest_user_detected(boxIds=[9100], questIds=[20002274], questStates=[1]):
            return 진행중일때20002274()


class 진행중일때20002274(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008], arg2=False) # ,90537,90539

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1000,1001,1002,1003,1004,1005,1006,1007,1008]):
            return 진행중일때20002274()


