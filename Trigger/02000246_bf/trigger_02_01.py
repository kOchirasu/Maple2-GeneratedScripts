""" trigger/02000246_bf/trigger_02_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[611,612,613,614,615,616,617,618,619])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[202]):
            return 몹생성()


class 몹생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[611,612,613,614,615,616,617,618,619], arg2=False)
        set_timer(timerId='1', seconds=120)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[611,612,613,614,615,616,617,618,619]):
            return 통과()


class 통과(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=180)


