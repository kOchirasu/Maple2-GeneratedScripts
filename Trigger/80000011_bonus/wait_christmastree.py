""" trigger/80000011_bonus/wait_christmastree.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=True, arg5=-90)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='ME_001_Wait_00')
        show_guide_summary(entityId=26100001, textId=26100001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기2()
        if time_expired(timerId='1'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26100001)


class 대기2(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='ME_001_Wait_00')
        show_guide_summary(entityId=26100002, textId=26100002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 대기()
        if time_expired(timerId='1'):
            return 종료()

    def on_exit(self):
        hide_guide_summary(entityId=26100002)


class 종료(state.State):
    pass


