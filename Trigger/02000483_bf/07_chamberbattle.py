""" trigger/02000483_bf/07_chamberbattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=False) # ToNextMap
        self.set_interact_object(triggerIds=[10002046], state=0) # Chair
        self.destroy_monster(spawnIds=[940,941,942]) # Mob
        self.set_breakable(triggerIds=[6200], enable=False) # Rock
        self.set_visible_breakable_object(triggerIds=[6200], visible=False) # Rock
        self.set_mesh(triggerIds=[3910], visible=True, arg3=0, delay=0, scale=0) # RockClosed
        self.set_mesh(triggerIds=[3920], visible=False, arg3=0, delay=0, scale=0) # RockOpened
        self.set_effect(triggerIds=[5300], visible=False) # StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9400]):
            # 회랑 진입
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return GuideFindPortal(self.ctx)


class GuideFindPortal(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 단서를 찾으세요
        self.show_guide_summary(entityId=20039706, textId=20039706)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTrapOn(self.ctx)


class MobTrapOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[940,941,942], animationEffect=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return MobTrapOnEnd(self.ctx)


class MobTrapOnEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[940,941,942]):
            return SwichOn(self.ctx)


class SwichOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002046], state=1) # LeverForLadder01

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002046], stateValue=0):
            return RockMove01(self.ctx)


class RockMove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3910], visible=False, arg3=100, delay=0, scale=2) # RockClosed
        self.set_breakable(triggerIds=[6200], enable=True) # Rock
        self.set_visible_breakable_object(triggerIds=[6200], visible=True) # Rock
        self.set_effect(triggerIds=[5300], visible=True) # StoneGate

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return RockMove02(self.ctx)


class RockMove02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=False) # ToNextMap

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return RockMove03(self.ctx)


class RockMove03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3920], visible=True, arg3=0, delay=0, scale=0) # RockOpened
        self.set_breakable(triggerIds=[6200], enable=False) # Rock
        self.set_visible_breakable_object(triggerIds=[6200], visible=False) # Rock


initial_state = Wait
