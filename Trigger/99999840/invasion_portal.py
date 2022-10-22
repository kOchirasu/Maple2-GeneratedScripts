""" trigger/99999840/invasion_portal.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990010, key='PCmove', value=0)
        set_interact_object(triggerIds=[10002183], state=2, arg3=False)


class 포탈열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True)
        set_interact_object(triggerIds=[10002183], state=1, arg3=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if time_expired(timerId='1'):
            reset_timer(timerId='1')
            return 포탈닫힘()
        if object_interacted(interactIds=[10002183], arg2=2):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990010, key='PCmove', value=1)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if dungeon_variable(varID='2000', value=1):
            return 포탈열림()


class 포탈닫힘(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990010, key='PCmove', value=0)
        set_timer(timerId='2', seconds=60, clearAtZero=True)
        set_interact_object(triggerIds=[10002183], state=2, arg3=False)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if time_expired(timerId='2'):
            reset_timer(timerId='2')
            return 대기()


class 종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002183], state=2, arg3=False)


