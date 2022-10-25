""" trigger/02000351_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[31,32], animationEffect=False)
        self.create_monster(spawnIds=[11,12,13,14,15,16,17], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.create_monster(spawnIds=[21,22,23,24,25,26,27,28,29], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.set_interact_object(triggerIds=[10000818], state=0)
        self.set_effect(triggerIds=[9000001], visible=False)
        self.set_effect(triggerIds=[9000002], visible=False)
        self.set_effect(triggerIds=[9000003], visible=False)
        self.set_effect(triggerIds=[9000004], visible=False)
        self.set_effect(triggerIds=[9000005], visible=False)
        self.set_effect(triggerIds=[9000006], visible=False)
        self.set_effect(triggerIds=[9000007], visible=False)
        self.set_effect(triggerIds=[9000008], visible=False)
        self.set_effect(triggerIds=[9000009], visible=False)
        self.set_effect(triggerIds=[9000010], visible=False)
        self.set_mesh(triggerIds=[6007], visible=False, delay=0, scale=10) # 화살표 표시 안함

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=Start)
        self.select_camera_path(pathIds=[80001,80002], returnView=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Start(self.ctx)

    def on_exit(self):
        self.remove_cinematic_talk() # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class Start(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000351_BF__MAIN__0$', arg3='3000')
        self.select_camera_path(pathIds=[80003], returnView=True)
        self.set_mesh(triggerIds=[6900], visible=False, delay=0, scale=10)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 관문_01_개방(self.ctx)


class 관문_01_개방(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000818], state=1)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return 관문_02_개방(self.ctx)


class 관문_02_개방(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=111, textId=20000080) # 스위치를 정지하세요
        self.set_interact_object(triggerIds=[10000819], state=1)
        self.set_interact_object(triggerIds=[10000820], state=1)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return 관문_03_시작(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=111)


class 관문_03_시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[33], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[31,32]):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.set_mesh(triggerIds=[6006], visible=False, delay=0, scale=10)
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)

    def on_exit(self):
        self.hide_guide_summary(entityId=112)


initial_state = idle
