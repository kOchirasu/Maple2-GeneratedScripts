""" trigger/02020062_bf/battle_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='ObjectClear', value=0)
        set_user_value(triggerId=99990004, key='ObjectStart', value=0)
        set_user_value(triggerId=99990005, key='ObjectStart', value=0)
        set_user_value(triggerId=99990006, key='ObjectStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=1):
            create_monster(spawnIds=[811,812,821,822,831,832], arg2=False)
            return 오브젝트소환()


class 오브젝트소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[711,712,713], arg2=False)
        set_user_value(triggerId=99990004, key='ObjectStart', value=1)
        set_user_value(triggerId=99990005, key='ObjectStart', value=1)
        set_user_value(triggerId=99990006, key='ObjectStart', value=1)
        set_user_value(triggerId=99990024, key='MovePanel01', value=1) # 이동 발판 트리거 생성
        set_user_value(triggerId=99990025, key='MovePanel02', value=1) # 이동 발판 트리거 생성
        set_user_value(triggerId=99990026, key='MovePanel03', value=1) # 이동 발판 트리거 생성
        set_user_value(triggerId=99990027, key='MovePanel04', value=1) # 이동 발판 트리거 생성

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_1()


class 추가대사_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020062_BF__BATTLE_2__0$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_2()


class 추가대사_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020062_BF__BATTLE_2__1$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_3()


class 추가대사_3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020062_BF__BATTLE_2__2$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어()


class 오브젝트소환_클리어(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='ObjectClear', value=1)
        set_user_value(triggerId=99990004, key='ObjectStart', value=2)
        set_user_value(triggerId=99990005, key='ObjectStart', value=2)
        set_user_value(triggerId=99990006, key='ObjectStart', value=2)


