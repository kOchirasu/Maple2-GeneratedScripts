""" trigger/02020061_bf/boss_object1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        destroy_monster(spawnIds=[711,721])
        set_interact_object(triggerIds=[12000094], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=1):
            return 레버1_체크()


class 레버1_체크(state.State):
    def on_enter(self):
        create_monster(spawnIds=[721], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if monster_dead(boxIds=[711]):
            return 레버1_발동()
        if all_of():
            return 종료()


class 레버1_발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_interact_object(triggerIds=[12000094], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000094], arg2=0):
            return 레버1_안내()


class 레버1_안내(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if wait_tick(waitTick=10000):
            return 레버1_재활성()


class 레버1_재활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000094], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000094], arg2=0):
            return 레버1_재활성_대기()


class 레버1_재활성_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if wait_tick(waitTick=10000):
            return 레버1_재활성()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        destroy_monster(spawnIds=[711,721])
        set_interact_object(triggerIds=[12000094], state=2)


