""" trigger/02100009_bf/monsterdie_2.xml """
from common import *
import state


class 유저감지(state.State):
    def on_enter(self):
        set_skill(triggerIds=[1000049], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[100000002]):
            return 버프()


class 버프(state.State):
    def on_enter(self):
        add_buff(boxIds=[100000001], skillId=50000217, level=1, arg4=True, arg5=False)
        set_skill(triggerIds=[1000049], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return None


