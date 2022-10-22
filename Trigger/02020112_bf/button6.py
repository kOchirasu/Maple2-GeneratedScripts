""" trigger/02020112_bf/button6.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[931], jobCode=0):
            return 작동()


class 작동(state.State):
    def on_enter(self):
        set_actor(triggerId=9906, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> state.State:
        if user_value(key='ButtonSuccess', value=1):
            return 종료()
        if user_detected(boxIds=[922], jobCode=0):
            return 감지()


class 감지(state.State):
    def on_enter(self):
        set_actor(triggerId=9906, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> state.State:
        if user_value(key='ButtonSuccess', value=1):
            return 종료()
        if not user_detected(boxIds=[922], jobCode=0):
            return 작동()


class 종료(state.State):
    def on_enter(self):
        set_actor(triggerId=9906, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')


