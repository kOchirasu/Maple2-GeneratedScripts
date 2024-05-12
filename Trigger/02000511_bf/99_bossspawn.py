""" trigger/02000511_bf/99_bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[999])
        self.set_portal(portalId=40, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3160,3161,3162,3163,3164], visible=True, arg3=0, delay=0, scale=0) # Barrier
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=False, arg3=0, delay=0, scale=0) # Bridge
        self.set_mesh(triggerIds=[5610,5611,5612], visible=True, arg3=0, delay=0, scale=0) # BlueLight_BossStage
        self.set_mesh_animation(triggerIds=[5610,5611,5612], visible=True, arg3=0, arg4=0) # BlueLight_BossStage
        self.set_effect(triggerIds=[5010], visible=False) # Sound_PortalOn
        self.set_effect(triggerIds=[5600], visible=False) # Sound_IceMelt_BossStage

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=170):
            return BossSpawn(self.ctx)


class BossSpawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # arg2="0" 을 넣으면 보스 등장하자마자 바로 공격 상태가 되는 것을 막을 수 있음
        self.create_monster(spawnIds=[999], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[999]):
            return BossDead(self.ctx)


class BossDead(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[999])
        self.set_effect(triggerIds=[5600], visible=True) # Sound_IceMelt_BossStage
        self.set_mesh(triggerIds=[5610,5611,5612], visible=False, arg3=500, delay=0, scale=5) # BlueLight_BossStage
        self.set_mesh_animation(triggerIds=[5610,5611,5612], visible=False, arg3=0, arg4=0) # BlueLight_BossStage

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BridgeApp(self.ctx)


class BridgeApp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3160,3161,3162,3163,3164], visible=False, arg3=0, delay=0, scale=0) # Barrier
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, arg3=0, delay=100, scale=2) # Bridge
        self.set_effect(triggerIds=[5010], visible=True) # Sound_PortalOn

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return DungeonClear(self.ctx)


class DungeonClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()
        self.set_portal(portalId=40, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
