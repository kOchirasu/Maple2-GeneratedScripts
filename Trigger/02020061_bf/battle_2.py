""" trigger/02020061_bf/battle_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='ObjectClear', value=0)
        set_user_value(triggerId=99990004, key='ObjectStart', value=0)
        set_user_value(triggerId=99990005, key='ObjectStart', value=0)
        set_user_value(triggerId=99990006, key='ObjectStart', value=0)
        set_user_value(triggerId=99990007, key='ObjectStart', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=1):
            return 오브젝트소환()


class 오브젝트소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[711,712,713,714], arg2=False)
        set_user_value(triggerId=99990004, key='ObjectStart', value=1)
        set_user_value(triggerId=99990005, key='ObjectStart', value=1)
        set_user_value(triggerId=99990006, key='ObjectStart', value=1)
        set_user_value(triggerId=99990007, key='ObjectStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어()
        if wait_tick(waitTick=5000):
            return 대사용_1()


class 대사용_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020061_BF__BATTLE_2__0$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어()
        if wait_tick(waitTick=5000):
            return 대사용_2()


class 대사용_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020061_BF__BATTLE_2__1$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어()
        if wait_tick(waitTick=5000):
            return 대사용_3()


class 대사용_3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020061_BF__BATTLE_2__2$')

    def on_tick(self) -> state.State:
        if user_value(key='ObjectPhase', value=2):
            return 대기()
        if monster_dead(boxIds=[701]):
            return 오브젝트소환_클리어()


class 오브젝트소환_클리어(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='ObjectClear', value=1)
        set_user_value(triggerId=99990004, key='ObjectStart', value=0)
        set_user_value(triggerId=99990005, key='ObjectStart', value=0)
        set_user_value(triggerId=99990006, key='ObjectStart', value=0)
        set_user_value(triggerId=99990007, key='ObjectStart', value=0)


