""" trigger/52010038_qd/npc_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6203], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='GaugeStart', value=1):
            return npc체크()


class npc체크(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1803]):
            return 이펙트()
        if not monster_in_combat(boxIds=[1803]):
            return 생성()
        if user_value(key='GaugeClosed', value=1):
            return 종료()


class 이펙트(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6203], visible=True)

    def on_tick(self) -> state.State:
        if not monster_in_combat(boxIds=[1803]):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6203], visible=False)
        init_npc_rotation(spawnIds=[1803])
        create_monster(spawnIds=[4000], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return npc체크()
        if user_value(key='GaugeClosed', value=1):
            return 종료()


class 종료(state.State):
    pass


