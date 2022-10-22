""" trigger/02000328_bf/level_01_00.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5100], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10000" arg2="1" />
        set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41001,41002], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10002]):
            set_mesh(triggerIds=[31001,31002,31003,31004,31005,31006,31007,31008,31009,31010,31011,31012,31013,31014,31015,31016,31017], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41001,41002], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


