""" trigger/61000010_me/ladder01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[701], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[702], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[711], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[712], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[721], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[722], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 랜덤(self.ctx)


class 랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=34):
            self.set_ladder(triggerIds=[701], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[702], visible=True, animationEffect=True)
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            self.set_ladder(triggerIds=[711], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[712], visible=True, animationEffect=True)
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            self.set_ladder(triggerIds=[721], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[722], visible=True, animationEffect=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
