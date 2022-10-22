""" trigger/02000328_bf/level_01_11.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5111], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10011" arg2="1" />
        set_mesh(triggerIds=[32101,32102,32103,32104,32105,32106,32107,32108,32109,32110,32111,32112,32113,32114,32115,32116,32117,32118,32119,32120,32121,32122,32123,32124,32125,32126,32127,32128,32129,32130,32131], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[42101,42102], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10015]):
            set_mesh(triggerIds=[32101,32102,32103,32104,32105,32106,32107,32108,32109,32110,32111,32112,32113,32114,32115,32116,32117,32118,32119,32120,32121,32122,32123,32124,32125,32126,32127,32128,32129,32130,32131], visible=True, arg3=0, arg4=100, arg5=1)
            set_mesh(triggerIds=[42101,42102], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


