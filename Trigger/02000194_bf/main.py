""" trigger/02000194_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10001054], state=2)
        self.set_interact_object(triggerIds=[10001055], state=2)
        self.set_interact_object(triggerIds=[10001056], state=2)
        self.set_interact_object(triggerIds=[10001057], state=2)
        self.set_interact_object(triggerIds=[11000004], state=2)
        self.set_mesh(triggerIds=[3005,3006,3007], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3301,3302,3303,3304], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 던전시작(self.ctx)


class 던전시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20001941, textId=20001941, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10001054], state=1)
        self.set_interact_object(triggerIds=[10001055], state=1)
        self.set_interact_object(triggerIds=[10001056], state=1)
        self.set_interact_object(triggerIds=[10001057], state=1)
        self.create_monster(spawnIds=[1001,1002,1003,1004,2000], animationEffect=False)
        self.select_camera(triggerId=301, enable=True)
        self.add_buff(boxIds=[101], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.set_skip(state=시작)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작(self.ctx)

    def on_exit(self) -> None:
        self.select_camera(triggerId=301, enable=False)
        self.set_mesh(triggerIds=[3005,3006,3007], visible=False, arg3=0, delay=0, scale=0)
        self.remove_buff(boxId=101, skillId=70000107)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20001942, textId=20001942, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작2(self.ctx)


class 시작2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001054], stateValue=0):
            self.set_mesh(triggerIds=[3101,3102,3103,3104], visible=False, arg3=0, delay=0, scale=0)
            return 오브젝트2(self.ctx)


class 오브젝트2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001055], stateValue=0):
            self.set_mesh(triggerIds=[3201,3202,3203], visible=False, arg3=0, delay=0, scale=0)
            return 오브젝트3(self.ctx)


class 오브젝트3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001056], stateValue=0):
            self.set_mesh(triggerIds=[3301,3302,3303,3304], visible=False, arg3=0, delay=0, scale=0)
            return 오브젝트4(self.ctx)


class 오브젝트4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001057], stateValue=0):
            self.show_guide_summary(entityId=20001944, textId=20001944, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
