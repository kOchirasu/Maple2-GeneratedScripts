""" trigger/02020019_bf/02020019_battle.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_user_value(triggerId=99990004, key='TimerReset', value=0)
        set_user_value(key='Success', value=0)
        set_user_value(triggerId=99990001, key='End', value=0)
        set_user_value(triggerId=99990003, key='5Phase', value=0)
        debug_string(feature='Develop', value='이건 Develop 환경에서 나오는 스트링 입니다.')

    def on_tick(self) -> state.State:
        if user_value(key='battlesetting', value=1):
            return 전투_1라운드세팅()


class 전투_1라운드세팅(state.State):
    def on_enter(self):
        dungeon_reset_time(seconds=300)
        show_round_ui(round=1, duration=3000)
        set_event_ui(type=0, arg2='1,5')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__0$', voice='ko/Npc/00002116')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_1라운드시작()


class 전투_1라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 전투_1라운드종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_1라운드종료(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24093001)
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_2라운드세팅()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_2라운드세팅(state.State):
    def on_enter(self):
        show_round_ui(round=2, duration=3000)
        set_event_ui(type=0, arg2='2,5')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__1$', voice='ko/Npc/00002121')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_2라운드시작()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_2라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[211], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211]):
            return 전투_2라운드종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_2라운드종료(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24093002)
        destroy_monster(spawnIds=[211])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_3라운드세팅()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_3라운드세팅(state.State):
    def on_enter(self):
        show_round_ui(round=3, duration=3000)
        set_event_ui(type=0, arg2='3,5')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__2$', voice='ko/Npc/00002241')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_3라운드시작()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_3라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[221,222,223,224,225,226,227], arg2=True)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=221, isRelative=True):
            return 전투_3라운드버프()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_3라운드버프(state.State):
    def on_enter(self):
        side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__3$', voice='ko/Npc/00002117')
        add_buff(boxIds=[221], skillId=49219001, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[221,222,223,224,225,226,227]):
            return 전투_3라운드종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_3라운드종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[221,222,223,224,225,226,227])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_4라운드세팅()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_4라운드세팅(state.State):
    def on_enter(self):
        show_round_ui(round=4, duration=3000)
        set_event_ui(type=0, arg2='4,5')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__4$', voice='ko/Npc/00002242')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_4라운드시작()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_4라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[231,232,233,234,235,236,237], arg2=True)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__5$', voice='ko/Npc/00002243')
        set_ai_extra_data(key='Autofire', value=1) # <대포 쏘기 시작 AI에 신호쏴주기>

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=231, isRelative=True):
            return 전투_4라운드버프()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_4라운드버프(state.State):
    def on_enter(self):
        side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__6$', voice='ko/Npc/00002118')
        add_buff(boxIds=[231], skillId=49219001, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[231,232,233,234,235,236,237]):
            return 전투_4라운드종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_4라운드종료(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=24093003)
        destroy_monster(spawnIds=[231,232,233,234,235,236,237])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 전투_5라운드세팅()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_5라운드세팅(state.State):
    def on_enter(self):
        show_round_ui(round=5, duration=3000)
        set_event_ui(type=0, arg2='5,5')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_B', duration=4800)
        side_npc_talk(npcId=24100001, illust='Neirin_normal', duration=5000, script='$02020019_BF__02020019_battle__7$', voice='ko/Npc/00002122')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=99990003, key='5Phase', value=1)
            return 전투_5라운드시작()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_5라운드시작(state.State):
    def on_enter(self):
        create_monster(spawnIds=[241,242,243,244,245,246,247,248], arg2=True)

    def on_tick(self) -> state.State:
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=241, isRelative=True):
            return 전투_5라운드버프()
        if check_npc_hp(compare='lowerEqual', value=50, spawnId=242, isRelative=True):
            return 전투_5라운드버프()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_5라운드버프(state.State):
    def on_enter(self):
        side_npc_talk(npcId=24100001, illust='Neirin_serious', duration=5000, script='$02020019_BF__02020019_battle__8$', voice='ko/Npc/00002119')
        add_buff(boxIds=[241], skillId=49219001, level=1, arg4=True)
        add_buff(boxIds=[242], skillId=49219001, level=1, arg4=True)

    def on_tick(self) -> state.State:
        if all_of(feature='FameChallengeBuff_01'):
            dungeon_mission_complete(missionId=24093004)
            dungeon_mission_complete(missionId=24093005)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_02'):
            dungeon_mission_complete(missionId=24093004)
            dungeon_mission_complete(missionId=24093006)
            return 전투_종료()
        if all_of(feature='FameChallengeBuff_03'):
            dungeon_mission_complete(missionId=24093004)
            dungeon_mission_complete(missionId=24093007)
            return 전투_종료()
        if monster_dead(boxIds=[241,242,243,244,245,246,247,248]):
            dungeon_mission_complete(missionId=24093004)
            return 전투_종료()
        if not user_detected(boxIds=[901]):
            return 전투_종료()
        if dungeon_check_play_time(playSeconds=300):
            return 전투_종료()


class 전투_종료(state.State):
    def on_enter(self):
        dungeon_set_end_time()
        dungeon_close_timer()
        set_ai_extra_data(key='Autofire', value=0) # <대포 쏘기 중지 AI에 신호쏴주기>
        set_event_ui(type=0, arg2='0,0')
        init_npc_rotation(spawnIds=[102,103])
        destroy_monster(spawnIds=[201])
        destroy_monster(spawnIds=[211])
        destroy_monster(spawnIds=[221,222,223,224,225,226,227])
        destroy_monster(spawnIds=[231,232,233,234,235,236,237])
        destroy_monster(spawnIds=[241,242,243,244,245,246,247,248]) # <네이린이랑 대포가 NPC이기 때문에 선택적으로 소멸시킴>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료신호()


class 종료신호(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='End', value=1)


