""" trigger/52000084_qd/4100_ladder.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[4100], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[4101], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[4102], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_ladder(triggerIds=[4103], visible=False, animationEffect=False, animationDelay=0) # Ladder_Shortcut
        set_interact_object(triggerIds=[10001128], state=0, arg4=False) # LeverForLadder

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9200, spawnIds=[101]):
            return PCComeDown()


class PCComeDown(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9400]):
            return LadderOn()


class LadderOn(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[4100], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[4101], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[4102], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut
        set_ladder(triggerIds=[4103], visible=True, animationEffect=True, animationDelay=2) # Ladder_Shortcut


