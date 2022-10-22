""" trigger/02000328_bf/level_01_07.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5107], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10007" arg2="1" />
        set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41701], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10006]):
            set_mesh(triggerIds=[31701,31702,31703,31704,31705,31706,31707,31708,31709,31710,31711,31712,31713,31714,31715,31716,31717,31718,31719], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41701], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


