""" trigger/02000328_bf/level_01_02.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5102], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10002" arg2="1" />
        set_mesh(triggerIds=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_cube(triggerIds=[5102], isVisible=True)
            set_mesh(triggerIds=[31201,31202,31203,31204,31205,31206,31207,31208,31209,31210,31211,31212,31213,31214,31215,31216,31217,31218], visible=True, arg3=0, arg4=200, arg5=2)
            return 종료()


class 종료(state.State):
    pass


