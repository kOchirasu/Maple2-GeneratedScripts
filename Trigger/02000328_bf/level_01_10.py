""" trigger/02000328_bf/level_01_10.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5110], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10010" arg2="1" />
        set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[42001], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10006]):
            set_mesh(triggerIds=[32001,32002,32003,32004,32005,32006,32007,32008,32009,32010,32011,32012,32013,32014,32015,32016,32017,32018,32019,32020,32021,32022], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[42001], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


