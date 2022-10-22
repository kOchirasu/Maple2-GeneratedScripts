""" trigger/02000241_bf/trigger_02_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703,704], visible=False)
        destroy_monster(spawnIds=[613,614,615,616,617,618,619,620,621])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[613,614,615,616,617,618,619,620,621], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[613,614,615,616,617,618,619,620,621]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=180)


