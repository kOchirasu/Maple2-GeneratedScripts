""" trigger/52020010_qd/main_c.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2007], questIds=[60200055], questStates=[2]):
            return Actor_On()
        if quest_user_detected(boxIds=[2007], questIds=[60200055], questStates=[3]):
            return Actor_On()
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[1]):
            return Actor_On()
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off()
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[3]):
            return Actor_Off()


class Actor_On(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=True, initialSequence='Event_01_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off()
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[3]):
            return Actor_Off()


class Actor_Off(state.State):
    def on_enter(self):
        set_actor(triggerId=8001, visible=True, initialSequence='Event_01_A')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off()
        if quest_user_detected(boxIds=[2007], questIds=[60200060], questStates=[2]):
            return Actor_Off()


