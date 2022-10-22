""" trigger/02000328_bf/level_01_01.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5101], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10001" arg2="1" />
        set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41101,41102], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_mesh(triggerIds=[31101,31102,31103,31104,31105,31106,31107,31108,31109,31110,31111,31112,31113,31114], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41101,41102], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


