""" trigger/02000452_bf/04_breakwall.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=False) # CubeBreak
        set_user_value(key='BossKill', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return BreakWall()
        if user_value(key='BossKill', value=1):
            return BreakWall()


class BreakWall(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7000], isEnable=True) # CubeBreak


