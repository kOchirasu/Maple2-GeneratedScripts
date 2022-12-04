""" trigger/66200001_gd/08_cheerupskill.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CheerUpTimer', value=1):
            return CheerUpTimer_20(self.ctx)


class CheerUpTimer_20(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20, startDelay=1, interval=0) # 20sec

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=16000):
            return GiveCheerUp(self.ctx)


class GiveCheerUp(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9001], skillId=70000086, level=1, isPlayer=False, isSkillSet=False) # 할 수 있어 버프

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='CheerUpTimer', value=0)
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
