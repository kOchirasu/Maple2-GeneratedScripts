""" trigger/02020062_bf/boss_object3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=False)
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        destroy_monster(spawnIds=[713,723])
        set_interact_object(triggerIds=[12000113], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=1):
            return 레버3_체크()


class 레버3_체크(state.State):
    def on_enter(self):
        create_monster(spawnIds=[723], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if monster_dead(boxIds=[713]):
            return 레버3_발동()
        if all_of():
            return 종료()


class 레버3_발동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=True)
        set_interact_object(triggerIds=[12000113], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 대기()
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000113], arg2=0):
            return 레버3_안내()


class 레버3_안내(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버3_재활성()


class 레버3_재활성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000113], state=1)

    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if object_interacted(interactIds=[12000113], arg2=0):
            return 레버3_재활성_대기()


class 레버3_재활성_대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BossObjectStart', value=2):
            return 종료()
        if all_of():
            return 종료()
        if wait_tick(waitTick=20000):
            return 레버3_재활성()


class 종료(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5201], visible=False)
        set_user_value(triggerId=99990023, key='MonsterSpawn', value=0)
        destroy_monster(spawnIds=[713,723])
        set_interact_object(triggerIds=[12000113], state=2)


