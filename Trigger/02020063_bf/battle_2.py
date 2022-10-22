""" trigger/02020063_bf/battle_2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_2_Clear', value=0)
        start_combine_spawn(groupId=[10000600], isStart=False) # 거대화 보급 상자
        start_combine_spawn(groupId=[10000601], isStart=False)
        start_combine_spawn(groupId=[10000602], isStart=False)
        set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
        set_user_value(triggerId=99990008, key='TurretSpawn_2', value=0)
        set_user_value(triggerId=99990009, key='TurretSpawn_3', value=0)
        set_user_value(triggerId=99990010, key='TurretSpawn_4', value=0)
        set_user_value(triggerId=99990015, key='TurretSpawn_5', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=1):
            return 포탑소환_1()


class 포탑소환_1(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[10000600], isStart=True) # 상자 소환 1
        set_user_value(triggerId=99990007, key='TurretSpawn_1', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_1()
        if monster_dead(boxIds=[711]):
            set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2()


class 추가대사_1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020063_BF__BATTLE_2__0$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_2()
        if monster_dead(boxIds=[711]):
            set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2()


class 추가대사_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__1$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=0):
            return 대기()
        if wait_tick(waitTick=5000):
            return 추가대사_3()
        if monster_dead(boxIds=[711]):
            set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2()


class 추가대사_3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020063_BF__BATTLE_2__2$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_4()
        if user_value(key='Battle_2_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[711]):
            set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
            return 포탑소환_2()


class 추가대사_4(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020063_BF__BATTLE_2__3$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[711]):
            return 포탑소환_2()


class 포탑소환_2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__4$')
        set_user_value(triggerId=99990008, key='TurretSpawn_2', value=1)
        set_user_value(triggerId=99990009, key='TurretSpawn_3', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[712,713]):
            return 포탑소환_3()
        if user_value(key='Battle_2_Start', value=0):
            return 대기()


class 포탑소환_3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020063_BF__BATTLE_2__5$')
        set_user_value(triggerId=99990010, key='TurretSpawn_4', value=1)
        set_user_value(triggerId=99990015, key='TurretSpawn_5', value=1)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[714,715]):
            return 종료대기()
        if user_value(key='Battle_2_Start', value=0):
            return 대기()


class 종료대기(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_smile', duration=5000, script='$02020063_BF__BATTLE_2__6$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 포탑소환_클리어()
        if user_value(key='Battle_2_Start', value=0):
            return 대기()


class 포탑소환_클리어(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_2_Clear', value=1)
        set_user_value(triggerId=99990005, key='Battle_2_SpawnStart', value=0)
        start_combine_spawn(groupId=[10000600], isStart=False)
        set_user_value(triggerId=99990007, key='TurretSpawn_1', value=0)
        set_user_value(triggerId=99990008, key='TurretSpawn_2', value=0)
        set_user_value(triggerId=99990009, key='TurretSpawn_3', value=0)
        set_user_value(triggerId=99990010, key='TurretSpawn_4', value=0)
        set_user_value(triggerId=99990015, key='TurretSpawn_5', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_2_Start', value=0):
            return 대기()


