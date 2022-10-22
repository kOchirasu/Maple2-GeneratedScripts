""" trigger/02000177_bf/horus.xml """
from common import *
import state


class Horus(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=710, boxId=1):
            return Horus_move_01()


class Horus_move_01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20001772, textId=20001772, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Horus_01_broken()


class Horus_01_broken(state.State):
    def on_enter(self):
        move_npc(spawnId=999, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Horus_01_End()


class Horus_01_End(state.State):
    def on_enter(self):
        set_skill(triggerIds=[3001], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return Horus_01_End_02()
        if count_users(boxId=711, boxId=1):
            return Horus_move_02()


class Horus_01_End_02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[999])

    def on_tick(self) -> state.State:
        if count_users(boxId=711, boxId=1):
            return Horus_move_02()


class Horus_move_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20001772, textId=20001772, duration=5000)
        create_monster(spawnIds=[998], arg2=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=751, spawnIds=[998]):
            return Horus_02_End()
        if object_interacted(interactIds=[10001060], arg2=2):
            return Horus_move_03()


class Horus_02_End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[998])

    def on_tick(self) -> state.State:
        if count_users(boxId=752, boxId=1):
            return Horus_move_03()


class Horus_move_03(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20001772, textId=20001772, duration=5000)
        create_monster(spawnIds=[997], arg2=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=753, spawnIds=[997]):
            return Horus_03_End()


class Horus_03_End(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[997])


