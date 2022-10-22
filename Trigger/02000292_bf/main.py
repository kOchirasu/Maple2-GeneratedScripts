""" trigger/02000292_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Wait(state.State):
    def on_enter(self):
        set_actor(triggerId=101, visible=True, initialSequence='Closed') # Door
        set_mesh(triggerIds=[102,103,104], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBarrier
        set_mesh(triggerIds=[105,106,107,108], visible=True, arg3=0, arg4=0, arg5=0) # EnterBarrierCube

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)
        set_skip(state=CameraWalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1110], arg2=False)
        move_npc(spawnId=1110, patrolName='MS2PatrolData_1110')
        select_camera(triggerId=601, enable=True)
        set_skip(state=CameraWalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk02()


class CameraWalk02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1110, script='$02000292_BF__MAIN__0$', arg4=3, arg5=0)
        set_skip(state=CameraWalk03)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        set_skip()
        select_camera(triggerId=601, enable=False)
        select_camera(triggerId=600, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DungeonOpen()

    def on_exit(self):
        destroy_monster(spawnIds=[1110])


class DungeonOpen(state.State):
    def on_enter(self):
        set_actor(triggerId=101, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[102,103,104], visible=False, arg3=100, arg4=100, arg5=2) # InvisibleBarrier

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return DungeonPlay01()


class DungeonPlay01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002922, textId=20002922, duration=5000)
        set_actor(triggerId=101, visible=False, initialSequence='Opened')
        set_mesh(triggerIds=[105,106,107,108], visible=False, arg3=0, arg4=0, arg5=0) # EnterBarrierCube

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return DungeonPlay02()


class DungeonPlay02(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002924, textId=20002924)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002924)


