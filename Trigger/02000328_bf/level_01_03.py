""" trigger/02000328_bf/level_01_03.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5103], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10003" arg2="1" />
        set_mesh(triggerIds=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41301,41302,41303], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_mesh(triggerIds=[31301,31302,31303,31304,31305,31306,31307,31308,31309,31310,31311,31312,31313,31314,31315,31316], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41301,41302,41303], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


