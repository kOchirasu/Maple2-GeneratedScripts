""" trigger/02020101_bf/deathflowernotice.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='notice', value=1):
            return 경고(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)


class 경고(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020101_BF__DEATHFLOWERNOTICE__0$', arg3='3000')
        self.set_user_value(triggerId=900005, key='notice', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.user_value(key='notice', value=0):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=900005, key='notice', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
