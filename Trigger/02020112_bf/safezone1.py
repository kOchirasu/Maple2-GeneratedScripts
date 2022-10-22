""" trigger/02020112_bf/safezone1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='Safe', value=0)
        set_interact_object(triggerIds=[10002117], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902], jobCode=0):
            return 감지()


class 감지(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            return 안전장치_활성화()


class 안전장치_활성화(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002117], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002117], arg2=0):
            return 안전장치_작동()


class 안전장치_작동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020112_BF__SAFEZONE1__0$', arg3='5000')
        set_user_value(triggerId=99990002, key='Safe', value=1)


