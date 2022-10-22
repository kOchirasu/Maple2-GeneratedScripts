""" trigger/80000015_bonus/lever2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7102], isEnable=False)
        set_interact_object(triggerIds=[10001315], state=1)
        set_mesh(triggerIds=[3006,3007,3008,3009,3010,3011], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 반응대기()


class 반응대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 안내()
        if object_interacted(interactIds=[10001315], arg2=0):
            return 문열림()


class 안내(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$80000015_bonus__lever2__0$', arg3='2000', arg4='102')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001315], arg2=0):
            return 문열림()
        if wait_tick(waitTick=5000):
            return 반응대기()


class 문열림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True)
        spawn_npc_range(rangeIds=[2002], isAutoTargeting=False, score=1500)
        set_mesh(triggerIds=[3006,3007,3008,3009,3010,3011], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_user_value(triggerId=999101, key='Dead_B', value=1)
        set_effect(triggerIds=[6000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            set_skill(triggerIds=[7102], isEnable=True)
            return 종료()


class 종료(state.State):
    pass


