""" trigger/63000006_cs/shake02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 다리흔들기준비(self.ctx)


class 다리흔들기준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[910], enable=False)
        self.set_skill(triggerIds=[911], enable=False)
        self.set_skill(triggerIds=[912], enable=False)
        self.set_skill(triggerIds=[913], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 스킬발동01(self.ctx)


class 스킬발동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=42)
        self.set_skill(triggerIds=[910], enable=True)
        self.set_skill(triggerIds=[911], enable=True)
        self.set_skill(triggerIds=[912], enable=True)
        self.set_skill(triggerIds=[913], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 다리흔들기준비(self.ctx)
        if self.user_detected(boxIds=[9002]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[910], enable=False)
        self.set_skill(triggerIds=[911], enable=False)
        self.set_skill(triggerIds=[912], enable=False)
        self.set_skill(triggerIds=[913], enable=False)


initial_state = 대기
