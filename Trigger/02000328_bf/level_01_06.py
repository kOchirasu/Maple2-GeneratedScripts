""" trigger/02000328_bf/level_01_06.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5106], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10006" arg2="1" />
        set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41601,41602,41603], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10006]):
            set_cube(triggerIds=[5106], isVisible=True)
            set_mesh(triggerIds=[31601,31602,31603,31604,31605,31606,31607,31608,31609,31610,31611,31612,31613,31614,31615,31616,31617,31618,31619,31620,31621,31622,31623], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41601,41602,41603], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


