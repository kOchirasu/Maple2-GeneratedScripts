""" trigger/02000356_bf/bossspawn.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030], animationEffect=False)
        self.set_interact_object(triggerIds=[10000259,10000260,10000261], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동01(self.ctx)


class 카메라이동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013], visible=False, arg3=0, delay=0, scale=0)
        self.add_buff(boxIds=[102], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20003563, textId=20003563, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(triggerId=303, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라이동02(self.ctx)


class 카메라이동02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=304, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라이동03(self.ctx)


class 카메라이동03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.show_guide_summary(entityId=20003562, textId=20003562, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=False)
        self.remove_buff(boxId=102, skillId=70000107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000259,10000260,10000261], stateValue=2):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1099])
        self.select_camera(triggerId=306, enable=True)
        self.add_buff(boxIds=[102], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20003561, textId=20003561, duration=6000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.select_camera(triggerId=306, enable=False)
            self.remove_buff(boxId=102, skillId=70000107)
            return 종료체크(self.ctx)


class 종료체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_clear()
            self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
