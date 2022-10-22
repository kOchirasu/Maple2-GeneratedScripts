""" trigger/80000009_bonus/exp_ball.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            create_item(spawnIds=[9001,9002,9003,9004,9005])
            return 초5()


class 초5(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            create_item(spawnIds=[9001])
            return 초10()


class 초10(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            create_item(spawnIds=[9001])
            return 초15()


class 초15(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            create_item(spawnIds=[9001])
            return 초20()


class 초20(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            create_item(spawnIds=[9001])
            return 초25()


class 초25(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            create_item(spawnIds=[9001])
            return 완료()


class 완료(state.State):
    pass


