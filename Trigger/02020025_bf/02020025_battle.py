""" trigger/02020025_bf/02020025_battle.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(key='Success', value=0)
        set_user_value(triggerId=99999001, key='End', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='battlesetting', value=1):
            return 전투_시작()


class 전투_시작(state.State):
    def on_enter(self):
        dungeon_reset_time(seconds=300)
        set_npc_duel_hp_bar(isOpen=True, spawnId=[201], durationTick=300000, npcHpStep=100)

    def on_tick(self) -> state.State:
        if all_of(feature='FameChallengeBuff_01'):
            dungeon_mission_complete(missionId=24092005)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_02'):
            dungeon_mission_complete(missionId=24092006)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_03'):
            dungeon_mission_complete(missionId=24092010)
            return 전투_종료()
        if monster_dead(boxIds=[201]):
            return 전투_종료()
        if not user_detected(boxIds=[902]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_종료(state.State):
    def on_enter(self):
        dungeon_set_end_time()
        destroy_monster(spawnIds=[-1])
        # <action name="버프를걸어준다" arg1="902" arg2="72000050" arg3="1"/>
        side_npc_talk(npcId=24110001, illust='Conder_normal', duration=4000, script='$02020025_BF__02020025_battle__0$', voice='ko/Npc/00002258')
        set_npc_duel_hp_bar(isOpen=False, spawnId=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료신호()


class 종료신호(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999001, key='End', value=1)

