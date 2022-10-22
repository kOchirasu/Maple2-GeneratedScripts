""" trigger/02000245_bf/trigger_04_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[707,708], visible=False)
        destroy_monster(spawnIds=[616,617,618,619,620,621,622,623,624])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[204]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[616,617,618,619,620,621,622,623,624], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[616,617,618,619,620,621,622,623,624]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[707,708], visible=False)
        set_timer(timerId='1', seconds=180)


