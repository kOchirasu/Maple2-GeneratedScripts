""" trigger/02000066_bf/cannon08.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[8008])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[8008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[8008]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            return 시작()


