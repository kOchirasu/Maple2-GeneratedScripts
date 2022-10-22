""" trigger/52100053_qd/07_chamberbattle.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=False) # ToNextMap
        set_interact_object(triggerIds=[10002099], state=0) # Chair
        destroy_monster(spawnIds=[940,941,942]) # Mob
        set_breakable(triggerIds=[6200], enabled=False) # Rock
        set_visible_breakable_object(triggerIds=[6200], arg2=False) # Rock
        set_mesh(triggerIds=[3910], visible=True, arg3=0, arg4=0, arg5=0) # RockClosed
        set_mesh(triggerIds=[3920], visible=False, arg3=0, arg4=0, arg5=0) # RockOpened
        set_effect(triggerIds=[5300], visible=False) # StoneGate

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9400]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002099], state=1) # Chair

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return GuideFindPortal()


class GuideFindPortal(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039705, textId=20039705) # 가이드 : 다른 방으로 이동할 단서를 찾으세요

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTrapOn()


class MobTrapOn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[940,941,942], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002099], arg2=0):
            return RockMove01()


class RockMove01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3910], visible=False, arg3=100, arg4=0, arg5=2) # RockClosed
        set_breakable(triggerIds=[6200], enabled=True) # Rock
        set_visible_breakable_object(triggerIds=[6200], arg2=True) # Rock
        set_effect(triggerIds=[5300], visible=True) # StoneGate

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return RockMove02()


class RockMove02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=False) # ToNextMap

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return RockMove03()


class RockMove03(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3920], visible=True, arg3=0, arg4=0, arg5=0) # RockOpened
        set_breakable(triggerIds=[6200], enabled=False) # Rock
        set_visible_breakable_object(triggerIds=[6200], arg2=False) # Rock


