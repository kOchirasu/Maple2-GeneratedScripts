""" trigger/52000014_qd/collapse_2000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2000,2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[12000], visible=False) # Vibrate Short
        set_effect(triggerIds=[22000], visible=False) # Vibrate Sound

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 무너짐01()


class 무너짐01(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=2)
        set_event_ui(type=1, arg2='$52000014_QD__COLLAPSE_2000__0$', arg3='4000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 무너짐02()


class 무너짐02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=8)
        set_effect(triggerIds=[12000], visible=True) # Vibrate Short
        set_effect(triggerIds=[22000], visible=True) # Vibrate Sound
        set_random_mesh(triggerIds=[2000,2001,2002,2003,2004], visible=False, meshCount=5, arg4=0, delay=200)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return None # Missing State: 무너짐03


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[12000], visible=False) # Vibrate Short
        set_effect(triggerIds=[22000], visible=False) # Vibrate Sound


