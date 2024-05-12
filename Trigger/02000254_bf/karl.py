""" trigger/02000254_bf/karl.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[450], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[904]):
            return 말풍선(self.ctx)
        if self.monster_in_combat(boxIds=[106]):
            return 종료(self.ctx)


class 말풍선(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='8', seconds=8)
        self.set_effect(triggerIds=[450], visible=True)
        self.set_conversation(type=1, spawnId=107, script='$02000254_BF__KARL__0$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='8'):
            return 시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
