""" trigger/02000317_bf/bossspawn.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False, arg5=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False, arg5=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False, arg5=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False, arg5=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False, arg5=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False, arg5=False)
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start()

state.DungeonStart = DungeonStart


class Start(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Step_1()


class Step_1(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[1,2,3,4,5,6,7], visible=False) # 다리안보임
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[203], arg2=False)
        create_monster(spawnIds=[204], arg2=False)
        create_monster(spawnIds=[205], arg2=False)
        create_monster(spawnIds=[206], arg2=False)
        create_monster(spawnIds=[207], arg2=False)
        create_monster(spawnIds=[208], arg2=False)
        create_monster(spawnIds=[301], arg2=False)
        create_monster(spawnIds=[302], arg2=False)
        create_monster(spawnIds=[303], arg2=False)
        create_monster(spawnIds=[304], arg2=False)
        create_monster(spawnIds=[305], arg2=False)
        create_monster(spawnIds=[306], arg2=False)
        create_monster(spawnIds=[307], arg2=False)
        create_monster(spawnIds=[401], arg2=False)
        create_monster(spawnIds=[402], arg2=False)
        create_monster(spawnIds=[403], arg2=False)
        create_monster(spawnIds=[404], arg2=False)
        create_monster(spawnIds=[405], arg2=False)
        create_monster(spawnIds=[406], arg2=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return Step_1_B_Ready()
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_1_B_Ready(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[205,208]):
            return Step_1_B()


class Step_1_B(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return Step_1_C()
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_1_C(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301,302]):
            return Step_1_D_Ready()
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_1_D_Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8,9,10,11], visible=False) # 다리안보임

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return Step_1_D()
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_1_D(state.State):
    def on_enter(self):
        show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[405]):
            return Step_1_E()
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_1_E(state.State):
    def on_enter(self):
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return Step_2()


class Step_2(state.State):
    def on_enter(self):
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        create_monster(spawnIds=[100], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[100]):
            return 종료체크()

    def on_exit(self):
        destroy_monster(spawnIds=[100])


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            dungeon_clear()
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)


