""" trigger/02020021_bf/battle.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_ai_extra_data(key='Start', value=0)
        set_user_value(triggerId=99990003, key='TimerReset', value=0)
        set_user_value(triggerId=99990003, key='SpecialTimerReset', value=0)
        set_user_value(key='Success', value=0)
        set_user_value(triggerId=99990001, key='End', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='battlesetting', value=1):
            return 전투_1라운드()


class 전투_1라운드(state.State):
    def on_enter(self):
        dungeon_reset_time(seconds=300)
        set_npc_duel_hp_bar(isOpen=True, spawnId=[201], durationTick=300000, npcHpStep=100)
        set_ai_extra_data(key='Phase', value=1) # <샤텐 AI 제어>

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()
        if check_npc_hp(compare='lowerEqual', value=80, spawnId=201, isRelative=True):
            return 전투_2라운드()


class 전투_2라운드(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__0$', voice='ko/Npc/00002245')
        create_monster(spawnIds=[301], arg2=False) # <독바닥 깔기 몬스터 생성>

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()
        if check_npc_hp(compare='lowerEqual', value=60, spawnId=201, isRelative=True):
            return 전투_3라운드()


class 전투_3라운드(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__1$', voice='ko/Npc/00002246')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투_3라운드_시작()


class 전투_3라운드_시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[301])
        create_monster(spawnIds=[302], arg2=False) # <독바닥 깔기 제어>
        set_ai_extra_data(key='Phase', value=2) # <샤텐 AI 제어>

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()
        if check_npc_hp(compare='lowerEqual', value=40, spawnId=201, isRelative=True):
            return 전투_4라운드()


class 전투_4라운드(state.State):
    def on_enter(self):
        side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__2$', voice='ko/Npc/00002247')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 전투_4라운드_시작()


class 전투_4라운드_시작(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[302])
        create_monster(spawnIds=[303], arg2=False) # <독바닥 깔기 제어>

    def on_tick(self) -> state.State:
        if all_of(feature='FameChallengeBuff_01'):
            dungeon_mission_complete(missionId=24095005)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_02'):
            dungeon_mission_complete(missionId=24095006)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_03'):
            dungeon_mission_complete(missionId=24095010)
            return 전투_종료()
        if monster_dead(boxIds=[201]):
            return 전투_종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_종료(state.State):
    def on_enter(self):
        dungeon_set_end_time()
        destroy_monster(spawnIds=[-1])
        # <action name="버프를걸어준다" arg1="901" arg2="72000050" arg3="1"/>
        set_npc_duel_hp_bar(isOpen=False, spawnId=[201])
        side_npc_talk(npcId=23200085, illust='Schatten_normal', duration=4000, script='$02020021_BF__battle__3$', voice='ko/Npc/00002244')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 종료신호()


class 종료신호(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='End', value=1)


