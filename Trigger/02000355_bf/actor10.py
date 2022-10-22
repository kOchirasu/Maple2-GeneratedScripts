""" trigger/02000355_bf/actor10.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=False)
        set_actor(triggerId=210, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[10001]):
            return 몬스터소환대기()


class 몬스터소환대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[610], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 더미해제()


class 더미해제(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2010]):
            return 소멸()
        if monster_dead(boxIds=[2099]):
            return 소멸()
        if npc_detected(boxId=105, spawnIds=[2010]):
            destroy_monster(spawnIds=[2010])
            return 리젠준비()


class 대기시간(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 리젠준비()
        if monster_dead(boxIds=[2099]):
            return 소멸()


class 리젠준비(state.State):
    def on_enter(self):
        set_actor(triggerId=210, visible=True, initialSequence='Regen_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class 소멸(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2010])


