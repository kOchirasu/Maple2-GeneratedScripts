""" trigger/02000328_bf/level_01_12.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5112], isVisible=False)
        # <action name="몬스터를생성한다" arg1="10012" arg2="1" />
        set_mesh(triggerIds=[32201,32202,32203,32204,32205,32206,32207,32208,32209,32210,32211,32212,32213,32214,32215,32216,32217,32218,32219,32220,32221,32222,32223,32224,32225,32226,32227,32228,32229,32230,32231,32232,32233,32234,32235,32236,32237,32238,32239,32240,32241,32242], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[42201,42202], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10015]):
            set_mesh(triggerIds=[32201,32202,32203,32204,32205,32206,32207,32208,32209,32210,32211,32212,32213,32214,32215,32216,32217,32218,32219,32220,32221,32222,32223,32224,32225,32226,32227,32228,32229,32230,32231,32232,32233,32234,32235,32236,32237,32238,32239,32240,32241,32242], visible=True, arg3=0, arg4=100, arg5=1)
            set_mesh(triggerIds=[42101,42202], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


