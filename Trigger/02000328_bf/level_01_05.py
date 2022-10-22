""" trigger/02000328_bf/level_01_05.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5105], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10005" arg2="1" />
        set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41501,41502], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520,31521], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41501,41502], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


