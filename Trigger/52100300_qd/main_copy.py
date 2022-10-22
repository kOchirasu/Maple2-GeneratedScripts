""" trigger/52100300_qd/main_copy.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103,104,105], arg2=True) # 몬스터 등장
        set_ladder(triggerIds=[1011], visible=False, animationEffect=True)
        set_ladder(triggerIds=[1012], visible=False, animationEffect=True)
        set_ladder(triggerIds=[1013], visible=False, animationEffect=True)
        create_monster(spawnIds=[201,202,203,204,205,206,207,208,209], arg2=True) # 마지막 섹터 몬스터 등장
        set_mesh(triggerIds=[29991,29992,29993,29994,29995,29996,29997,29998,29999], visible=False) # 안보이는 상태
        set_effect(triggerIds=[7010], visible=True) # 전원 붙는 소리
        set_effect(triggerIds=[7011], visible=True) # 전원 붙는 소리
        set_effect(triggerIds=[7012], visible=True) # 전원 붙는 소리
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=991, isEnable=False)
        enable_spawn_point_pc(spawnId=992, isEnable=False)
        enable_spawn_point_pc(spawnId=993, isEnable=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=시작_03)
        select_camera_path(pathIds=[80001,80002], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작_03()

    def on_exit(self):
        remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)

state.DungeonStart = DungeonStart


class 시작_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[80003], returnView=True)
        set_event_ui(type=1, arg2='$02010086_BF__MAIN__0$', arg3='3000')
        set_actor(triggerId=1001, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[1002], visible=False, arg4=0, arg5=10) # 벽 해제
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작_04()


class 시작_04(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 전투_01()


class 전투_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[999], arg2=True) # 몬스터 등장
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103,104,105]):
            return 관문_01_개방()


class 관문_01_개방(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        set_actor(triggerId=1003, visible=True, initialSequence='Opened')
        set_actor(triggerId=5001, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=5002, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_mesh(triggerIds=[1004], visible=False, arg4=0, arg5=10) # 벽 해제
        set_effect(triggerIds=[7020], visible=False) # 알람 소리

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 전투_02()


class 전투_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[111,112,113,114,115,116,117,118,119], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115,116,117,118,119]):
            return 관문_02_개방()


class 관문_02_개방(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[1011], visible=True, animationEffect=True)
        set_ladder(triggerIds=[1012], visible=True, animationEffect=True)
        set_ladder(triggerIds=[1013], visible=True, animationEffect=True)
        set_actor(triggerId=5003, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=5004, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=5005, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        set_effect(triggerIds=[7021], visible=False) # 알람 소리
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 전투_03()


class 전투_03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[121,122,123,124,125,126,127,128,129], arg2=True) # 몬스터 등장
        create_monster(spawnIds=[994], arg2=True) # 새틀라이트 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122,123,124,125,126,127,128,129]):
            return 관문_03_개방()
        if count_users(boxId=705, boxId=1):
            return 전투_04()

    def on_exit(self):
        set_interact_object(triggerIds=[10000896], state=1)
        destroy_monster(spawnIds=[994])


class 관문_03_개방(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=991, isEnable=True)
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return 전투_04()


class 전투_04(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[131,132,133,134,135,136,137,138,139], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[131,132,133,134,135,136,137,138,139]):
            return 관문_04_개방()


class 관문_04_개방(state.State):
    def on_enter(self):
        set_actor(triggerId=5006, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=5007, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=1006, visible=True, initialSequence='Opened') # 문 열림
        set_mesh(triggerIds=[1007], visible=False, arg4=0, arg5=10) # 벽 해제
        set_effect(triggerIds=[7022], visible=False) # 알람 소리
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if count_users(boxId=706, boxId=1):
            return 전투_05()


class 전투_05(state.State):
    def on_enter(self):
        set_actor(triggerId=1009, visible=True, initialSequence='Opened') # 문 열림
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[141,142,143,144,145,146,147,148,149], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[141,142,143,144,145,146,147,148,149]):
            return 관문_05_개방()
        if count_users(boxId=707, boxId=1):
            return 전투_06()


class 관문_05_개방(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=991, isEnable=False)
        enable_spawn_point_pc(spawnId=992, isEnable=True)
        set_actor(triggerId=5008, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        set_actor(triggerId=5009, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return 전투_06()


class 전투_06(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[151,152,153,154,155,156,157,158,159], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[151,152,153,154,155,156,157,158,159]):
            return 관문_06_개방_02()


class 관문_06_개방(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002,2003], visible=False, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[2011,2012,2013], visible=True, arg4=300, arg5=10) # 파란 선으로
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 관문_06_개방_02()


class 관문_06_개방_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[161,162,163,164,165,166,167,168,169], arg2=True) # 몬스터 등장
        set_mesh(triggerIds=[2014,2015,2016], visible=False, arg4=30, arg5=0) # 문 폭발
        set_mesh(triggerIds=[2011,2012,2013], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if count_users(boxId=708, boxId=1):
            return 전투_07()


class 전투_07(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        create_monster(spawnIds=[171,172,173,174,175,176,177,178,179], arg2=True) # 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[171,172,173,174,175,176,177,178,179]):
            return 관문_07_개방()


class 관문_07_개방(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=992, isEnable=False)
        enable_spawn_point_pc(spawnId=993, isEnable=True)
        set_mesh(triggerIds=[2021,2022,2023], visible=False, arg4=0, arg5=0) # 관문 개방
        show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206,207,208,209]):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000897], state=1)


