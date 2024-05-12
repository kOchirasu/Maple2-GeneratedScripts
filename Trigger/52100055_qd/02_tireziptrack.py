""" trigger/52100055_qd/02_tireziptrack.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[100]) # Tire
        self.set_user_value(key='TireSpawn', value=0)
        self.set_interact_object(triggerIds=[10002100], state=0) # MakeTireZipTrack

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TireSpawn', value=1):
            return GuideInteract(self.ctx)


class GuideInteract(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 건너편 탑으로 이동할 수 있는 장치를 찾으세요
        self.show_guide_summary(entityId=20039903, textId=20039903)
        self.set_interact_object(triggerIds=[10002100], state=1) # MakeTireZipTrack

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002100], stateValue=0):
            return TireSpawn(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=20039903)


class TireSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[100], animationEffect=False) # Tire
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039904, textId=20039904, duration=3000) # 가이드 : 타이어에 매달리세요!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return GuideTireHold(self.ctx)


class GuideTireHold(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039905, textId=20039905, duration=2000) # 가이드 : 출발합니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TireMove(self.ctx)


class TireMove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_100')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return TireRemove01(self.ctx)


class TireRemove01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[100])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TireResetDelay(self.ctx)


class TireResetDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TireReset(self.ctx)


class TireReset(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002100], state=1) # MakeTireZipTrack

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002100], stateValue=0):
            return TireSpawnAgain(self.ctx)


class TireSpawnAgain(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[100], animationEffect=False) # Tire

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TireMoveAgain(self.ctx)


class TireMoveAgain(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=100, patrolName='MS2PatrolData_100')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return TireRemove01(self.ctx)


initial_state = Wait
