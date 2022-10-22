""" trigger/02000245_bf/trigger_02_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703,704], visible=False)
        destroy_monster(spawnIds=[604,605,606,607,608,609,610,611,612])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[604,605,606,607,608,609,610,611,612], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[604,605,606,607,608,609,610,611,612]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703,704], visible=False)
        set_timer(timerId='1', seconds=180)


