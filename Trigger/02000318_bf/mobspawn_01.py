""" trigger/02000318_bf/mobspawn_01.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # EnteranceBarrier
        self.set_mesh(triggerIds=[3001], visible=True, arg3=0, delay=0, scale=0) # 1stBarrier
        self.set_mesh(triggerIds=[3002], visible=True, arg3=0, delay=0, scale=0) # 2ndBarrier
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], visible=True, arg3=0, delay=0, scale=0) # EnteranceBarrier
        self.set_user_value(key='ShipMove', value=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304,305], animationEffect=False)
        self.create_monster(spawnIds=[201,202,203,204,205], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=CameraWalk01)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=False)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$02000318_BF__MOBSPAWN_01__0$', arg3='3000', arg4='0')
        self.set_mesh(triggerIds=[3000], visible=False, arg3=0, delay=0, scale=0) # EnteranceBarrier
        self.set_random_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128], visible=False, meshCount=29, arg4=500, delay=30) # EnteranceBarrier

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Battle01(self.ctx)


class Battle01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031801, textId=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302,303,304,305]):
            return Battle02(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[301,302,303,304,305])


class Battle02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111,112,113,114,115,116,501], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Battle03(self.ctx)


class Battle03(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031801)
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031802, textId=20031802) # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,116]):
            return MoveShip01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[111,112,113,114,115,116,501])


class MoveShip01(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031802)
        self.set_user_value(triggerId=2, key='ShipSet', value=1)
        self.set_mesh(triggerIds=[3001], visible=False, arg3=0, delay=0, scale=0) # 1stBarrier

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ShipMove', value=1):
            return MoveShip02(self.ctx)


class MoveShip02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[103]):
            return Battle11(self.ctx)


class Battle11(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031801, textId=20031801) # 몬스터를 모두 처치하세요

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204,205]):
            return Battle12(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[201,202,203,204,205])


class Battle12(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211,212,213,214,215,216,217,218,219,502,503], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Battle13(self.ctx)


class Battle13(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031801)
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031802, textId=20031802) # 대포를 이용해 올라갈 수 없는 지형 위의 몬스터를 처치하세요

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[211,212,213,214,215,216,217,218,219]):
            return CannonSpawn01(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[211,212,213,214,215,216,217,218,219,502,503])


class CannonSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[401], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return CannonSpawn02(self.ctx)


class CannonSpawn02(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031802)
        self.play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20031804, textId=20031804) # 대포를 이용해 다음 지역으로 이동하세요
        self.set_mesh(triggerIds=[3002], visible=False, arg3=0, delay=0, scale=0) # 2ndBarrier

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20031804)


initial_state = Setting
