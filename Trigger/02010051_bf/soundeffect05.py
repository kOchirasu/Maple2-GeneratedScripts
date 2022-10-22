""" trigger/02010051_bf/soundeffect05.xml """
from common import *
import state


class 대기01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        set_effect(triggerIds=[900], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 음성연출()


class 음성연출(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)
        set_effect(triggerIds=[900], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기02()


class 대기02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10000]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[900], visible=False)


