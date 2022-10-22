""" trigger/02000213_bf/regenmob28.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 소환몹등장()


class 소환몹등장(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000261], arg2=1):
            create_monster(spawnIds=[1028], arg2=False)
            return 소멸체크()


class 소멸체크(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000261], arg2=0):
            return 소멸()
        if object_interacted(interactIds=[10000261], arg2=2):
            return 소멸()
        if monster_dead(boxIds=[1028]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=15)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 소환몹등장()

    def on_exit(self):
        reset_timer(timerId='1')


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1028])
        set_timer(timerId='1', seconds=1200)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()

    def on_exit(self):
        reset_timer(timerId='1')


