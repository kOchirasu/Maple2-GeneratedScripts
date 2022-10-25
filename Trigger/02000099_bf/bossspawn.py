""" trigger/02000099_bf/bossspawn.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20000991, textId=20000991, duration=5000)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,2000], animationEffect=False)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=301, enable=False)
        self.remove_buff(boxId=199, skillId=70000107)


class 시작(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20000992, textId=20000992, duration=3000)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작가이드2(self.ctx)


class 시작가이드2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 차등장1(self.ctx)


class 차등장1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetSkillA', value=1):
            self.set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106], visible=False, arg3=0, delay=0, scale=0)
            return 차등장대기2(self.ctx)


class 차등장대기2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 차등장2(self.ctx)


class 차등장2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SetSkillB', value=1):
            self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208], visible=False, arg3=0, delay=0, scale=0)
            return 엘리트등장(self.ctx)


class 엘리트등장(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000]):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entityId=20000993, textId=20000993, duration=5000)
            self.set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], visible=False, arg3=0, delay=0, scale=0)
            return 엘리트처치(self.ctx)


class 엘리트처치(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entityId=20000994, textId=20000994, duration=3000)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 시작대기중
