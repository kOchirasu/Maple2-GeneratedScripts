""" trigger/99999896/01_intro.xml """
from common import *
import state


class 스타트(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 멘트대기()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트_1()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트_1(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)
        set_event_ui(type=1, arg2='$99999896__01_INTRO__0$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트_2()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트_2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_event_ui(type=1, arg2='$99999896__01_INTRO__1$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 멘트_3()

    def on_exit(self):
        reset_timer(timerId='1')


class 멘트_3(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_event_ui(type=1, arg2='$99999896__01_INTRO__2$', arg3='2000')
        create_item(spawnIds=[1,2,3])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 완료()

    def on_exit(self):
        reset_timer(timerId='1')


class 완료(state.State):
    pass


