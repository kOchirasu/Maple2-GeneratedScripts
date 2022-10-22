""" trigger/52100055_qd/02_tireziptrack.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[100]) # Tire
        set_user_value(key='TireSpawn', value=0)
        set_interact_object(triggerIds=[10002100], state=0) # MakeTireZipTrack

    def on_tick(self) -> state.State:
        if user_value(key='TireSpawn', value=1):
            return GuideInteract()


class GuideInteract(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039903, textId=20039903) # 가이드 : 건너편 탑으로 이동할 수 있는 장치를 찾으세요
        set_interact_object(triggerIds=[10002100], state=1) # MakeTireZipTrack

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002100], arg2=0):
            return TireSpawn()

    def on_exit(self):
        hide_guide_summary(entityId=20039903)


class TireSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100], arg2=False) # Tire
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039904, textId=20039904, duration=3000) # 가이드 : 타이어에 매달리세요!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return GuideTireHold()


class GuideTireHold(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039905, textId=20039905, duration=2000) # 가이드 : 출발합니다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TireMove()


class TireMove(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return TireRemove01()


class TireRemove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[100])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return TireResetDelay()


class TireResetDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TireReset()


class TireReset(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002100], state=1) # MakeTireZipTrack

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002100], arg2=0):
            return TireSpawnAgain()


class TireSpawnAgain(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100], arg2=False) # Tire

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return TireMoveAgain()


class TireMoveAgain(state.State):
    def on_enter(self):
        move_npc(spawnId=100, patrolName='MS2PatrolData_100')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return TireRemove01()


