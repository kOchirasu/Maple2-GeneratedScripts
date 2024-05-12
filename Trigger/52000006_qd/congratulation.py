""" trigger/52000006_qd/congratulation.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[200], visible=False)
        self.set_effect(triggerIds=[201], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 축하대기1(self.ctx)


class 축하대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.bonus_game_reward_detected(boxId=101, arg2=True):
            return 축하1(self.ctx)


class 축하1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[200], visible=True)
        self.set_effect(triggerIds=[201], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 축하2(self.ctx)


class 축하2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=100, script='$52000006_QD__CONGRATULATION__0$')
        self.set_conversation(type=1, spawnId=101, script='$52000006_QD__CONGRATULATION__1$')
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 완료(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(triggerIds=[200], visible=False)
        self.set_effect(triggerIds=[201], visible=False)


class 완료(trigger_api.Trigger):
    pass


initial_state = 대기
