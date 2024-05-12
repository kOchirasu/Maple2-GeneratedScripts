""" trigger/02000488_bf/99_bossspawn.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[999])
        self.set_portal(portal_id=40, visible=False, enable=False, minimap_visible=False)
        self.set_mesh(trigger_ids=[3160,3161,3162,3163,3164], visible=True, start_delay=0, interval=0, fade=0) # Barrier
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, start_delay=0, interval=0, fade=0) # Bridge
        self.set_mesh(trigger_ids=[5610,5611,5612], visible=True, start_delay=0, interval=0, fade=0) # BlueLight_BossStage
        self.set_mesh_animation(trigger_ids=[5610,5611,5612], visible=True, start_delay=0, interval=0) # BlueLight_BossStage
        self.set_effect(trigger_ids=[5010], visible=False) # Sound_PortalOn
        self.set_effect(trigger_ids=[5600], visible=False) # Sound_IceMelt_BossStage

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return BossSpawn(self.ctx)


class BossSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        self.spawn_monster(spawn_ids=[999], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[999]):
            return BossDead(self.ctx)


class BossDead(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[999])
        self.set_effect(trigger_ids=[5600], visible=True) # Sound_IceMelt_BossStage
        self.set_mesh(trigger_ids=[5610,5611,5612], visible=False, start_delay=500, interval=0, fade=5) # BlueLight_BossStage
        self.set_mesh_animation(trigger_ids=[5610,5611,5612], visible=False, start_delay=0, interval=0) # BlueLight_BossStage

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return BridgeApp(self.ctx)


class BridgeApp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3160,3161,3162,3163,3164], visible=False, start_delay=0, interval=0, fade=0) # Barrier
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, start_delay=0, interval=100, fade=2) # Bridge
        self.set_effect(trigger_ids=[5010], visible=True) # Sound_PortalOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return DungeonClear(self.ctx)


class DungeonClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portal_id=40, visible=True, enable=True, minimap_visible=True)


initial_state = Wait
