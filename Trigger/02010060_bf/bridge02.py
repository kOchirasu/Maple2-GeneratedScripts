""" trigger/02010060_bf/bridge02.xml """
from common import *
import state


class NPC감지대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[702], isEnable=False)
        set_effect(triggerIds=[611], visible=False)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10000919], state=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[2099]):
            return 오브젝트반응대기()
        if user_value(key='SecondPhaseEnd', value=1):
            return 오브젝트반응대기()


class 오브젝트반응대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[702], isEnable=True)
        set_interact_object(triggerIds=[10000919], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000919], arg2=0):
            return 다리생성()


class 다리생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=True)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243], visible=True, arg3=0, arg4=50, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이펙트생성()


class 이펙트생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3300,3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311,3312,3313,3314,3315,3316,3317,3318,3319], visible=True, arg3=0, arg4=100, arg5=2)


