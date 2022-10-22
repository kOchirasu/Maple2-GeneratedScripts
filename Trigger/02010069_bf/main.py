""" trigger/02010069_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Setting(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[33000], visible=False)
        set_effect(triggerIds=[34001], visible=False)
        set_effect(triggerIds=[34002], visible=False)
        set_effect(triggerIds=[34022], visible=False)
        set_effect(triggerIds=[34023], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000817], state=0)
        destroy_monster(spawnIds=[44441,44442,44443])

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[101], sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10000817], state=1)
        show_guide_summary(entityId=20100691, textId=20100691, duration=10000)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000817], arg2=0):
            return 차어나운스1()

state.DungeonStart = DungeonStart


class 차어나운스1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        hide_guide_summary(entityId=20100691)
        set_effect(triggerIds=[32000], visible=True)
        set_effect(triggerIds=[34001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차어나운스2()


class 차어나운스2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[33000], visible=True)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=False, arg3=200, arg4=50, arg5=0)
        move_user(mapId=2010069, portalId=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999997]):
            create_monster(spawnIds=[44441,44442,44443], arg2=False)
            return 연출1()


class 연출1(state.State):
    def on_enter(self):
        select_camera(triggerId=999900, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출22()


class 연출22(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=44441, script='$02010069_BF__MAIN__1$', arg4=3, arg5=1)
        move_npc(spawnId=44441, patrolName='MS2PatrolData2')
        set_skip(state=연출25)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출23()


class 연출23(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=44443, script='$02010069_BF__MAIN__2$', arg4=3, arg5=1)
        move_npc(spawnId=44443, patrolName='MS2PatrolData1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출24()


class 연출24(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=44442, script='$02010069_BF__MAIN__3$', arg4=3, arg5=1)
        move_npc(spawnId=44442, patrolName='MS2PatrolData0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출25()


class 연출25(state.State):
    def on_enter(self):
        remove_balloon_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출2()


class 연출2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=4)
        set_cinematic_ui(type=5)
        set_cinematic_ui(type=6)
        set_effect(triggerIds=[34022], visible=True)
        set_effect(triggerIds=[34023], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출3()


class 연출3(state.State):
    def on_enter(self):
        select_camera(triggerId=999900, enable=False)
        move_user(mapId=2010069, portalId=2)
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출4()


class 연출4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_effect(triggerIds=[34022], visible=False)
        set_effect(triggerIds=[34023], visible=False)


