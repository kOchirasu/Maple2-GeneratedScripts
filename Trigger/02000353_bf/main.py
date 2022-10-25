""" trigger/02000353_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[6001], visible=False)
        self.set_effect(triggerIds=[6002], visible=False)
        self.set_effect(triggerIds=[6003], visible=False)
        self.set_effect(triggerIds=[6004], visible=False)
        self.set_effect(triggerIds=[6101], visible=False)
        self.set_effect(triggerIds=[6301], visible=False)
        self.set_effect(triggerIds=[6302], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=701, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start(self.ctx)


class Start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작_03(self.ctx)


class 시작_03(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_timer(timerId='2', seconds=2, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 시작_04(self.ctx)


class 시작_04(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[901,902,903], visible=False, delay=0, scale=10) # 벽 해제
        self.set_skill(triggerIds=[2020], enable=True) # 벽 날리는 스킬

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=702, boxId=1):
            return 시작_05(self.ctx)


class 시작_05(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        self.set_effect(triggerIds=[6001], visible=True)
        self.set_effect(triggerIds=[6002], visible=True)
        self.set_effect(triggerIds=[6003], visible=True)
        self.set_effect(triggerIds=[6004], visible=True)
        self.set_effect(triggerIds=[6101], visible=True)
        self.set_actor(triggerId=3001, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3002, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3003, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3004, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3101, visible=False, initialSequence='Dmg_A')
        self.create_monster(spawnIds=[11,12,13,14,15], animationEffect=False) # 기본 배치 될 몬스터 등장
        self.create_monster(spawnIds=[101,102,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[11,12,13,14,15]):
            return 관문_01_개방전(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 관문_01_개방전(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__2$', arg3='2000')
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 관문_01_개방(self.ctx)


class 관문_01_개방(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=관문_02_스킵)
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_01_개방_이벤트_00(self.ctx)


class 관문_01_개방_이벤트_00(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_01_개방_이벤트_01(self.ctx)


class 관문_01_개방_이벤트_01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2001], enable=True) # 벽 날리는 스킬
        self.set_skill(triggerIds=[2002], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_01_개방_이벤트_02(self.ctx)


class 관문_01_개방_이벤트_02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2003], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_01_개방_이벤트_03(self.ctx)


class 관문_01_개방_이벤트_03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2004], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 관문_02_시작(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)


class 관문_02_스킵(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2001], enable=True)
        self.set_skill(triggerIds=[2002], enable=True)
        self.set_skill(triggerIds=[2003], enable=True)
        self.set_skill(triggerIds=[2004], enable=True)
        self.set_skip()
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            self.remove_buff(boxId=199, skillId=70000107)
            return 관문_02_시작(self.ctx)


class 관문_02_시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.select_camera(triggerId=8001, enable=False)
        self.show_guide_summary(entityId=103, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=703, boxId=1):
            return 관문_02_시작_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=103)


class 관문_02_시작_02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6005], visible=True)
        self.set_effect(triggerIds=[6006], visible=True)
        self.set_effect(triggerIds=[6007], visible=True)
        self.set_effect(triggerIds=[6008], visible=True)
        self.set_actor(triggerId=3005, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3006, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3007, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3008, visible=False, initialSequence='Dmg_A')
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        self.create_monster(spawnIds=[21,22,23,24,25,26,27], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[21,22,23,24,25,26,27]):
            return 관문_02_개방전(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 관문_02_개방전(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__3$', arg3='2000')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_02_개방(self.ctx)


class 관문_02_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 관문_02_개방_이벤트_01(self.ctx)


class 관문_02_개방_이벤트_01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2006], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_02_개방_이벤트_02(self.ctx)


class 관문_02_개방_이벤트_02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2007], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_02_개방_이벤트_03(self.ctx)


class 관문_02_개방_이벤트_03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2008], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_03_시작_01(self.ctx)


class 관문_03_시작_01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=103, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=704, boxId=1):
            return 관문_03_시작_02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=103)


class 관문_03_시작_02(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        self.set_effect(triggerIds=[6301], visible=True)
        self.set_effect(triggerIds=[6302], visible=True)
        self.set_actor(triggerId=3301, visible=False, initialSequence='Dmg_A')
        self.set_actor(triggerId=3302, visible=False, initialSequence='Dmg_A')
        self.create_monster(spawnIds=[31,32,33], animationEffect=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[31,32,33]):
            return 관문_03_개방전(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=101)


class 관문_03_개방전(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000353_BF__MAIN__4$', arg3='2000')
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_03_개방(self.ctx)


class 관문_03_개방(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 관문_03_개방_이벤트_01(self.ctx)


class 관문_03_개방_이벤트_01(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2009], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_03_개방_이벤트_02(self.ctx)


class 관문_03_개방_이벤트_02(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2010], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 관문_03_개방_이벤트_03(self.ctx)


class 관문_03_개방_이벤트_03(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2011], enable=True) # 벽 날리는 스킬
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 지역클리어(self.ctx)


class 지역클리어(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Space_PopUp_01')
        self.show_guide_summary(entityId=103, textId=40009) # 포탈로 이동하세요
        self.set_mesh(triggerIds=[6006], visible=False, delay=0, scale=10) # 벽 해제
        self.set_mesh(triggerIds=[6007], visible=True, delay=0, scale=10) # 화살표 표시
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
