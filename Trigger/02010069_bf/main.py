""" trigger/02010069_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class Setting(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=True, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[33000], visible=False)
        self.set_effect(triggerIds=[34001], visible=False)
        self.set_effect(triggerIds=[34002], visible=False)
        self.set_effect(triggerIds=[34022], visible=False)
        self.set_effect(triggerIds=[34023], visible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000817], state=0)
        self.destroy_monster(spawnIds=[44441,44442,44443])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[101], sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10000817], state=1)
        self.show_guide_summary(entityId=20100691, textId=20100691, duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000817], stateValue=0):
            return 차어나운스1(self.ctx)


class 차어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.hide_guide_summary(entityId=20100691)
        self.set_effect(triggerIds=[32000], visible=True)
        self.set_effect(triggerIds=[34001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 차어나운스2(self.ctx)


class 차어나운스2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[33000], visible=True)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=False, arg3=200, delay=50, scale=0)
        self.move_user(mapId=2010069, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[999997]):
            self.create_monster(spawnIds=[44441,44442,44443], animationEffect=False)
            return 연출1(self.ctx)


class 연출1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=999900, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출22(self.ctx)


class 연출22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=44441, script='$02010069_BF__MAIN__1$', arg4=3, arg5=1)
        self.move_npc(spawnId=44441, patrolName='MS2PatrolData2')
        self.set_skip(state=연출25)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출23(self.ctx)


class 연출23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=44443, script='$02010069_BF__MAIN__2$', arg4=3, arg5=1)
        self.move_npc(spawnId=44443, patrolName='MS2PatrolData1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출24(self.ctx)


class 연출24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=44442, script='$02010069_BF__MAIN__3$', arg4=3, arg5=1)
        self.move_npc(spawnId=44442, patrolName='MS2PatrolData0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출25(self.ctx)


class 연출25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_balloon_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출2(self.ctx)


class 연출2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.set_cinematic_ui(type=5)
        self.set_cinematic_ui(type=6)
        self.set_effect(triggerIds=[34022], visible=True)
        self.set_effect(triggerIds=[34023], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출3(self.ctx)


class 연출3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=999900, enable=False)
        self.move_user(mapId=2010069, portalId=2)
        self.set_portal(portalId=2, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출4(self.ctx)


class 연출4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[34022], visible=False)
        self.set_effect(triggerIds=[34023], visible=False)


initial_state = Setting
