""" trigger/02000355_bf/actor09.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[609], visible=False)
        set_actor(triggerId=209, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1901]):
            return 몬스터소환대기()


class 몬스터소환대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[609], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2009], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 더미해제()


class 더미해제(state.State):
    def on_enter(self):
        set_actor(triggerId=209, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2009]):
            return 종료()


class 종료(state.State):
    pass


