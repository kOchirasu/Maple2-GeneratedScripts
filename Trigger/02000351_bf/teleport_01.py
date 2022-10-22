""" trigger/02000351_bf/teleport_01.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=1):
            return start_sound()

    def on_exit(self):
        set_effect(triggerIds=[9000005], visible=True) # TeleportSound EFfect On


class start_sound(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return idle()

    def on_exit(self):
        set_effect(triggerIds=[9000005], visible=False) # TeleportSound EFfect On


