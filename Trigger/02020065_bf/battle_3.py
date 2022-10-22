""" trigger/02020065_bf/battle_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_3_Clear', value=0)
        start_combine_spawn(groupId=[10000603], isStart=False)
        start_combine_spawn(groupId=[10000605], isStart=False)
        set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=0)
        set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=0)
        set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=0)
        set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Start', value=1):
            return 보스_추가대사()


class 보스_추가대사(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_event_ui(type=1, arg2='$02020065_BF__BATTLE_3__0$', arg3='5000')
            return 보스소환()


class 보스소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[921], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[921]):
            return 보스군단_클리어()
        if all_of():
            return 보스_무적페이즈()


class 보스_무적페이즈(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020065_BF__BATTLE_3__1$', arg3='5000')
        set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=1)
        set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=1)
        set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=1)
        set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=1)
        # <action name="SetUserValue" triggerID="99990006" key="Battle_3_SpawnStart" value="1" />
        start_combine_spawn(groupId=[10000603], isStart=True)
        start_combine_spawn(groupId=[10000605], isStart=True)
        set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[921]):
            return 보스군단_클리어()
        if wait_tick(waitTick=5000):
            return 보스_추가대사1()


class 보스_추가대사1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_surprise', duration=5000, script='$02020065_BF__BATTLE_3__2$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[921]):
            return 보스군단_클리어()
        if wait_tick(waitTick=5000):
            return 보스_추가대사2()


class 보스_추가대사2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003533, illust='Bliche_normal', duration=5000, script='$02020065_BF__BATTLE_3__3$')

    def on_tick(self) -> state.State:
        if user_value(key='Battle_3_Start', value=0):
            return 대기()
        if monster_dead(boxIds=[921]):
            return 보스군단_클리어()


class 보스군단_클리어(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Battle_3_Clear', value=1)
        set_user_value(triggerId=99990006, key='Battle_3_SpawnStart', value=0)
        start_combine_spawn(groupId=[10000603], isStart=False)
        start_combine_spawn(groupId=[10000605], isStart=False)
        set_user_value(triggerId=99990011, key='Battle3_TurretSpawn_1', value=0)
        set_user_value(triggerId=99990012, key='Battle3_TurretSpawn_2', value=0)
        set_user_value(triggerId=99990013, key='Battle3_TurretSpawn_3', value=0)
        set_user_value(triggerId=99990014, key='Battle3_TurretSpawn_4', value=0)


