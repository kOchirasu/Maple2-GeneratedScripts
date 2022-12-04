""" trigger/02000523_bf/regionskill01.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=201, spawnIds=[900]):
            return 스킬작동(self.ctx)


class 스킬작동(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[302], enable=True)
        self.set_skill(triggerIds=[303], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=201, spawnIds=[900]):
            return 트리거초기화(self.ctx)


class 트리거초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[302], enable=False)
        self.set_skill(triggerIds=[303], enable=False)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
