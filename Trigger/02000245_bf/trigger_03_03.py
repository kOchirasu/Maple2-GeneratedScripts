""" trigger/02000245_bf/trigger_03_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[613,614,615])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[203]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[613,614,615], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[613,614,615]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)


