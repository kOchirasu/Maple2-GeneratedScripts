""" trigger/02100001_bf/04_move.xml """
from common import *
import state


#  아프렐라 오지 : 산 아래에서 올라올 수 있는 발판 
class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001244], state=1) # CrowMove
        set_breakable(triggerIds=[4502], enabled=False) # Move
        set_visible_breakable_object(triggerIds=[4502], arg2=True) # Move

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001244], arg2=0):
            return MoveStart()


class MoveStart(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4502], enabled=True) # Move

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return MoveStop()


class MoveStop(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4502], enabled=False) # Move
        set_visible_breakable_object(triggerIds=[4502], arg2=False) # Move

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return Reset()


class Reset(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001244], state=1) # CrowMove
        set_visible_breakable_object(triggerIds=[4502], arg2=True) # Move

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001244], arg2=0):
            return MoveStart()


