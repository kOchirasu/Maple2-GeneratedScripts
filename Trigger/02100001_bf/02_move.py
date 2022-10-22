""" trigger/02100001_bf/02_move.xml """
from common import *
import state


#  아프렐라 오지 : 독수리쪽에서 건너올 수 있는 발판 
class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001241], state=1) # CrowMove
        set_breakable(triggerIds=[4500], enabled=False) # Move
        set_visible_breakable_object(triggerIds=[4500], arg2=True) # Move

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001241], arg2=0):
            return MoveStart()


class MoveStart(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4500], enabled=True) # Move

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return MoveStop()


class MoveStop(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4500], enabled=False) # Move

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001241], state=1) # CrowMove

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001241], arg2=0):
            return MoveStart()


