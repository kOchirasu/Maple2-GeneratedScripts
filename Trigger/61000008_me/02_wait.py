""" trigger/61000008_me/02_wait.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60, clearAtZero=True, display=False) # 테스트 수정 가능 지점

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100001, textId=26100001, duration=5000)

    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기2()
        if time_expired(timerId='1'):
            return 종료()


class 대기2(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26100002, textId=26100002, duration=5000)

    def on_tick(self) -> state.State:
        if count_users(boxId=9001, boxId=50):
            return 종료()
        if wait_tick(waitTick=5000):
            return 대기()
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    pass


