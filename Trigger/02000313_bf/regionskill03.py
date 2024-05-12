""" trigger/02000313_bf/regionskill03.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=13, spawn_ids=[2099]):
            return 스킬작동(self.ctx)


class 스킬작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[301], enable=True)
        self.set_skill(trigger_ids=[302], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(box_id=13, spawn_ids=[2099]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[301], enable=False)
        self.set_skill(trigger_ids=[302], enable=False)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
