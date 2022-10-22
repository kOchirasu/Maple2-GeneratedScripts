""" trigger/99999922/event8.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1003])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999910]):
            return 진행1()


class 진행1(state.State):
    def on_enter(self):
        set_timer(timerId='300', seconds=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1003]):
            return 진행2()


class 진행2(state.State):
    def on_enter(self):
        add_buff(boxIds=[999910], skillId=49179111, level=1, arg5=True)
        set_timer(timerId='300', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='300'):
            return 시작10()


class 시작10(state.State):
    def on_enter(self):
        set_timer(timerId='400', seconds=60)


