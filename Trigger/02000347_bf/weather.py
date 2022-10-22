""" trigger/02000347_bf/weather.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_interact_object(triggerIds=[10000804], state=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[60002]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000804], state=1)
        set_effect(triggerIds=[600], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000804], arg2=0):
            return 비내림()


class 비내림(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)
        set_timer(timerId='30', seconds=30)
        set_event_ui(type=1, arg2='$02000347_BF__MAIN1__4$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            set_event_ui(type=1, arg2='$02000347_BF__MAIN1__3$', arg3='2000', arg4='0')
            return 시작()
        if monster_dead(boxIds=[101]):
            set_effect(triggerIds=[600], visible=False)
            return 종료()


class 종료(state.State):
    pass


