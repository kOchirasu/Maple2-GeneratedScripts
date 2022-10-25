""" trigger/02000354_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7701], visible=False)
        self.set_effect(triggerIds=[7702], visible=False)
        self.set_effect(triggerIds=[7703], visible=False)
        self.set_effect(triggerIds=[7704], visible=False)
        self.set_effect(triggerIds=[7705], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작_04(self.ctx)


class 시작_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7701], visible=True) # 벽 녹이는 사운드
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012], visible=False, delay=0, scale=10) # 벽 해제

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 시작_05(self.ctx)


class 시작_05(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[11,12,13,14,15,16,17], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[11,12,13,14,15,16,17]):
            return 관문_01_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_01_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7702], visible=True) # 벽 녹이는 사운드
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033], visible=False, delay=0, scale=10) # 벽 해제

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return 관문_02_시작(self.ctx)


class 관문_02_시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[21,22,23,24,25,26,27], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[21,22,23,24,25,26,27]):
            return 관문_02_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_02_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7703], visible=True) # 벽 녹이는 사운드
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066,6067,6068,6069,6070,6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082,6083], visible=False, delay=0, scale=10) # 벽 해제

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return 관문_03_시작(self.ctx)


class 관문_03_시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[31,32,33,34,35,36,37,38,39], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[31,32,33,34,35,36,37,38,39]):
            return 관문_03_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_03_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7704], visible=True) # 벽 녹이는 사운드
        self.set_mesh(triggerIds=[6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123], visible=False, delay=0, scale=10) # 벽 해제
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=705, boxId=1):
            return 관문_04_시작(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_04_시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[41,42,43,44,45,46,47,48], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[341,42,43,44,45,46,47,48]):
            return 관문_04_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_04_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7705], visible=True) # 벽 녹이는 사운드
        self.set_mesh(triggerIds=[6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166], visible=False, delay=0, scale=10) # 벽 해제
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=113, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=706, boxId=1):
            return 관문_05_시작(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=113)


class 관문_05_시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=110, textId=40010) # 적을 모두 처치하세요
        self.create_monster(spawnIds=[51], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[51]):
            return 관문_05_개방(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=110)


class 관문_05_개방(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=112, textId=40009) # 포탈을 타세요
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)

    def on_exit(self):
        self.hide_guide_summary(entityId=112)


initial_state = idle
