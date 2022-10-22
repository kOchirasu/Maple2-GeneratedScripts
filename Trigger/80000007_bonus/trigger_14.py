""" trigger/80000007_bonus/trigger_14.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[303]):
            return 막힘()


class 막힘(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[401,402,403,404,405,406,407,408,409], visible=False)


