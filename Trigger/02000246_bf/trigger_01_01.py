""" trigger/02000246_bf/trigger_01_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[601,602,603,604,605,606,607,608,609])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[201]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[601,602,603,604,605,606,607,608,609], arg2=False)
        set_timer(timerId='1', seconds=120)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604,605,606,607,608,609]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=180)


