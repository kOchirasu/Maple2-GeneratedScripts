""" trigger/02010086_bf/boss_bomb.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=799, minUsers='1'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[6001], enable=True)
        self.set_skill(triggerIds=[6002], enable=True)
        self.set_skill(triggerIds=[6003], enable=True)
        self.set_skill(triggerIds=[6004], enable=True)
        self.set_effect(triggerIds=[6010], visible=True) # 폭발
        self.set_effect(triggerIds=[6011], visible=True) # 폭발
        self.set_effect(triggerIds=[6012], visible=True) # 폭발


initial_state = 대기
