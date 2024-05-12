""" trigger/02010052_bf/torchlight_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[81001], visible=False) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81002], visible=False) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81003], visible=False) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81004], visible=False) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81005], visible=False) # 얼음이 녹는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[101]):
            return burn_state(self.ctx)


class burn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012], visible=False, start_delay=800, interval=100, fade=0) # 벽 해제
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_01__0$', arg3='3000')
        self.set_effect(trigger_ids=[7001], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timer_id='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=200)
        self.set_effect(trigger_ids=[7501], visible=True) # 얼음 녹는 소리
        self.set_effect(trigger_ids=[81001], visible=True) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81002], visible=True) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81003], visible=True) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81004], visible=True) # 얼음이 녹는 이펙트
        self.set_effect(trigger_ids=[81005], visible=True) # 얼음이 녹는 이펙트
        self.set_actor(trigger_id=8101, visible=False, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8102, visible=False, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8103, visible=False, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8104, visible=False, initial_sequence='Dmg_A')
        self.set_actor(trigger_id=8105, visible=False, initial_sequence='Dmg_A')
        self.spawn_monster(spawn_ids=[311,312,313,314,315], auto_target=True) # 얼음이 녹으며 등장하는 몬스터들


initial_state = idle
