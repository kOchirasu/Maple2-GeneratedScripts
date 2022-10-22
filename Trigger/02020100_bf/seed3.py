""" trigger/02020100_bf/seed3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='EliteClear', value=0)
        set_user_value(triggerId=99990001, key='Seed3interact', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Seed3start', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[229])
        set_mesh(triggerIds=[1304], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002111], state=1, arg3=True)

    def on_tick(self) -> state.State:
        if user_value(key='Seed3start', value=2):
            return 종료()
        if object_interacted(interactIds=[10002111], arg2=0):
            return 씨앗3_심기()


class 씨앗3_심기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Seed3interact', value=1)
        set_mesh(triggerIds=[1304], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002122], state=1, arg3=True)

    def on_tick(self) -> state.State:
        if user_value(key='Seed3start', value=2):
            return 종료()
        if object_interacted(interactIds=[10002122], arg2=0):
            return 씨앗3_중보()
        if not check_any_user_additional_effect(boxId=0, additionalEffectId=70002109, level=1):
            return 시작()


class 씨앗3_중보(state.State):
    def on_enter(self):
        set_actor(triggerId=1404, visible=True, initialSequence='Interaction_lapentatree_A01_On')
        destroy_monster(spawnIds=[121,122,123,124])
        create_monster(spawnIds=[229], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[229]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='EliteClear', value=1)
        set_interact_object(triggerIds=[10002111], state=0)


