""" trigger/02000245_bf/trigger_01_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,603])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601,602,603], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)


