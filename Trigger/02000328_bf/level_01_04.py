""" trigger/02000328_bf/level_01_04.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5104], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10004" arg2="1" />
        set_mesh(triggerIds=[31401,31402,31403,31404,31405,31406,31407,31408,31409,31410,31411,31412,31413,31414,31415,31416,31417,31418,31419], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41401,41402], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_mesh(triggerIds=[31401,31402,31403,31404,31405,31406,31407,31408,31409,31410,31411,31412,31413,31414,31415,31416,31417,31418,31419], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41401,41402], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


