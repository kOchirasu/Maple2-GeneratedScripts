""" trigger/52100300_qd/main_copy.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102,103,104,105], animationEffect=True) # 몬스터 등장
        self.set_ladder(triggerIds=[1011], visible=False, animationEffect=True)
        self.set_ladder(triggerIds=[1012], visible=False, animationEffect=True)
        self.set_ladder(triggerIds=[1013], visible=False, animationEffect=True)
        self.create_monster(spawnIds=[201,202,203,204,205,206,207,208,209], animationEffect=True) # 마지막 섹터 몬스터 등장
        self.set_mesh(triggerIds=[29991,29992,29993,29994,29995,29996,29997,29998,29999], visible=False) # 안보이는 상태
        self.set_effect(triggerIds=[7010], visible=True) # 전원 붙는 소리
        self.set_effect(triggerIds=[7011], visible=True) # 전원 붙는 소리
        self.set_effect(triggerIds=[7012], visible=True) # 전원 붙는 소리
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=991, isEnable=False)
        self.enable_spawn_point_pc(spawnId=992, isEnable=False)
        self.enable_spawn_point_pc(spawnId=993, isEnable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=701, minUsers='1'):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=시작_03)
        self.select_camera_path(pathIds=[80001,80002], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작_03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 시작_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[80003], returnView=True)
        self.set_event_ui(type=1, arg2='$02010086_BF__MAIN__0$', arg3='3000')
        self.set_actor(triggerId=1001, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[1002], visible=False, delay=0, scale=10) # 벽 해제
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작_04(self.ctx)


class 시작_04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=702, minUsers='1'):
            return 전투_01(self.ctx)


class 전투_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[999], animationEffect=True) # 몬스터 등장
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103,104,105]):
            return 관문_01_개방(self.ctx)


class 관문_01_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.
        self.set_actor(triggerId=1003, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=5001, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=5002, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_mesh(triggerIds=[1004], visible=False, delay=0, scale=10) # 벽 해제
        self.set_effect(triggerIds=[7020], visible=False) # 알람 소리

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=703, minUsers='1'):
            return 전투_02(self.ctx)


class 전투_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[111,112,113,114,115,116,117,118,119], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,116,117,118,119]):
            return 관문_02_개방(self.ctx)


class 관문_02_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[1011], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[1012], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[1013], visible=True, animationEffect=True)
        self.set_actor(triggerId=5003, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=5004, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=5005, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.set_effect(triggerIds=[7021], visible=False) # 알람 소리
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=704, minUsers='1'):
            return 전투_03(self.ctx)


class 전투_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[121,122,123,124,125,126,127,128,129], animationEffect=True) # 몬스터 등장
        self.create_monster(spawnIds=[994], animationEffect=True) # 새틀라이트 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[121,122,123,124,125,126,127,128,129]):
            return 관문_03_개방(self.ctx)
        if self.count_users(boxId=705, minUsers='1'):
            return 전투_04(self.ctx)

    def on_exit(self) -> None:
        self.set_interact_object(triggerIds=[10000896], state=1)
        self.destroy_monster(spawnIds=[994])


class 관문_03_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=991, isEnable=True)
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=705, minUsers='1'):
            return 전투_04(self.ctx)


class 전투_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[131,132,133,134,135,136,137,138,139], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[131,132,133,134,135,136,137,138,139]):
            return 관문_04_개방(self.ctx)


class 관문_04_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=5006, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=5007, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=1006, visible=True, initialSequence='Opened') # 문 열림
        self.set_mesh(triggerIds=[1007], visible=False, delay=0, scale=10) # 벽 해제
        self.set_effect(triggerIds=[7022], visible=False) # 알람 소리
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=706, minUsers='1'):
            return 전투_05(self.ctx)


class 전투_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=1009, visible=True, initialSequence='Opened') # 문 열림
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[141,142,143,144,145,146,147,148,149], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[141,142,143,144,145,146,147,148,149]):
            return 관문_05_개방(self.ctx)
        if self.count_users(boxId=707, minUsers='1'):
            return 전투_06(self.ctx)


class 관문_05_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=991, isEnable=False)
        self.enable_spawn_point_pc(spawnId=992, isEnable=True)
        self.set_actor(triggerId=5008, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.set_actor(triggerId=5009, visible=True, initialSequence='sf_quest_light_A01_Off') # 알람 꺼
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, minUsers='1'):
            return 전투_06(self.ctx)


class 전투_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[151,152,153,154,155,156,157,158,159], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[151,152,153,154,155,156,157,158,159]):
            return 관문_06_개방_02(self.ctx)


class 관문_06_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2001,2002,2003], visible=False, delay=300, scale=10) # 빨간 선이
        self.set_mesh(triggerIds=[2011,2012,2013], visible=True, delay=300, scale=10) # 파란 선으로
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 관문_06_개방_02(self.ctx)


class 관문_06_개방_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[161,162,163,164,165,166,167,168,169], animationEffect=True) # 몬스터 등장
        self.set_mesh(triggerIds=[2014,2015,2016], visible=False, delay=30, scale=0) # 문 폭발
        self.set_mesh(triggerIds=[2011,2012,2013], visible=False, delay=0, scale=10) # 파란 선도 마저 삭제
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=708, minUsers='1'):
            return 전투_07(self.ctx)


class 전투_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[171,172,173,174,175,176,177,178,179], animationEffect=True) # 몬스터 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[171,172,173,174,175,176,177,178,179]):
            return 관문_07_개방(self.ctx)


class 관문_07_개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawnId=992, isEnable=False)
        self.enable_spawn_point_pc(spawnId=993, isEnable=True)
        self.set_mesh(triggerIds=[2021,2022,2023], visible=False, delay=0, scale=0) # 관문 개방
        self.show_guide_summary(entityId=106, textId=20003362, duration=3000) # 다음 구역으로 이동할 수 있습니다.

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205,206,207,208,209]):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000897], state=1)


initial_state = idle
