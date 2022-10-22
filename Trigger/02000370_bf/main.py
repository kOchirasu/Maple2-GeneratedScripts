""" trigger/02000370_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3200], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 전투01()
        if user_detected(boxIds=[1002]):
            return 전투01()


class 전투01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105,106,107], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105,106,107]):
            return 포털개방()


class 포털개방(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3100,3200], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=True, arg3=0, arg4=100, arg5=1)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, arg3=0, arg4=100, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


