""" trigger/02000281_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301,302], visible=True, arg3=0, delay=0)
        self.set_interact_object(triggerIds=[10000414], state=0)
        self.set_ladder(triggerIds=[321], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[322], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[323], visible=False, animationEffect=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015], animationEffect=False)
        self.set_interact_object(triggerIds=[10000414], state=1)
        self.select_camera(triggerId=3001, enable=True)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라대기(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 카메라대기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002810, textId=20002810, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=3002, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 생성(self.ctx)

    def on_exit(self):
        self.remove_buff(boxId=199, skillId=70000107)
        self.select_camera(triggerId=3002, enable=False)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301,302], visible=False, arg3=0, delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000414], stateValue=0):
            return 보스(self.ctx)


class 보스(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.show_guide_summary(entityId=20002816, textId=20002816, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2002]):
            self.show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(triggerIds=[321], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[322], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[323], visible=True, animationEffect=True)
            self.set_portal(portalId=2, visible=False, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
