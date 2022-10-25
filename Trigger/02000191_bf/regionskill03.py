""" trigger/02000191_bf/regionskill03.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=203, spawnIds=[900]):
            return 스킬작동(self.ctx)


class 스킬작동(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[301], enable=True)
        self.set_skill(triggerIds=[302], enable=True)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=203, spawnIds=[900]):
            return 트리거초기화(self.ctx)


class 트리거초기화(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[301], enable=False)
        self.set_skill(triggerIds=[302], enable=False)
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
