""" trigger/02000525_bf/qeagle_07.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000487], state=1)
        set_actor(triggerId=913, visible=False, initialSequence='Attack_Idle_A')
        set_effect(triggerIds=[914], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000487], arg2=0):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_enter(self):
        set_actor(triggerId=913, visible=True, initialSequence='Attack_Idle_A')
        set_effect(triggerIds=[914], visible=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 그리폰제거()

    def on_exit(self):
        set_actor(triggerId=913, visible=False, initialSequence='Attack_Idle_A')
        set_effect(triggerIds=[914], visible=False)


class 그리폰제거(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=600)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


