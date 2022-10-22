""" trigger/02000355_bf/actor03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=False)
        set_actor(triggerId=203, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1301]):
            return 몬스터소환대기()
        if user_detected(boxIds=[1302]):
            return 몬스터소환대기()
        if user_detected(boxIds=[1303]):
            return 몬스터소환대기()


class 몬스터소환대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 몬스터소환()


class 몬스터소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2003], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 더미해제()


class 더미해제(state.State):
    def on_enter(self):
        set_actor(triggerId=203, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2003]):
            return 종료()


class 종료(state.State):
    pass


