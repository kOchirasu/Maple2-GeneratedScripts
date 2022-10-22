""" trigger/02000328_bf/level_01_08.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5108], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10008" arg2="1" />
        set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[41801], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10006]):
            set_mesh(triggerIds=[31801,31802,31803,31804,31805,31806,31807,31808,31809,31810,31811,31812,31813,31814,31815,31816,31817,31818,31819,31820,31821,31822], visible=True, arg3=0, arg4=200, arg5=2)
            set_mesh(triggerIds=[41801], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


