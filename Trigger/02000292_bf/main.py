""" trigger/02000292_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=101, visible=True, initialSequence='Closed') # Door
        self.set_mesh(triggerIds=[102,103,104], visible=True, arg3=0, delay=0, scale=0) # InvisibleBarrier
        self.set_mesh(triggerIds=[105,106,107,108], visible=True, arg3=0, delay=0, scale=0) # EnterBarrierCube

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return CameraWalk01(self.ctx)


class CameraWalk01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1110], animationEffect=False)
        self.move_npc(spawnId=1110, patrolName='MS2PatrolData_1110')
        self.select_camera(triggerId=601, enable=True)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraWalk02(self.ctx)


class CameraWalk02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1110, script='$02000292_BF__MAIN__0$', arg4=3, arg5=0)
        self.set_skip(state=CameraWalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CameraWalk03(self.ctx)


class CameraWalk03(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.select_camera(triggerId=601, enable=False)
        self.select_camera(triggerId=600, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonOpen(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1110])


class DungeonOpen(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=101, visible=True, initialSequence='Opened')
        self.set_mesh(triggerIds=[102,103,104], visible=False, arg3=100, delay=100, scale=2) # InvisibleBarrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return DungeonPlay01(self.ctx)


class DungeonPlay01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002922, textId=20002922, duration=5000)
        self.set_actor(triggerId=101, visible=False, initialSequence='Opened')
        self.set_mesh(triggerIds=[105,106,107,108], visible=False, arg3=0, delay=0, scale=0) # EnterBarrierCube

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return DungeonPlay02(self.ctx)


class DungeonPlay02(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002924, textId=20002924)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002924)


initial_state = Wait
