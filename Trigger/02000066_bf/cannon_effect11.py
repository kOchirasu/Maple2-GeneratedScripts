""" trigger/02000066_bf/cannon_effect11.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[811], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[121]):
            return 이펙트대기(self.ctx)


class 이펙트대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=121, spawnIds=[8011]):
            return 이펙트on(self.ctx)


class 이펙트on(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[811], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[8011]):
            return 대기시간(self.ctx)
        if not self.user_detected(boxIds=[121]):
            return 대기시간(self.ctx)


class 대기시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[811], visible=False)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 시작(self.ctx)


initial_state = 시작
