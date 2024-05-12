""" trigger/61000010_me/ladder01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(trigger_ids=[701], visible=False, enable=False)
        self.set_ladder(trigger_ids=[702], visible=False, enable=False)
        self.set_ladder(trigger_ids=[711], visible=False, enable=False)
        self.set_ladder(trigger_ids=[712], visible=False, enable=False)
        self.set_ladder(trigger_ids=[721], visible=False, enable=False)
        self.set_ladder(trigger_ids=[722], visible=False, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        return 랜덤(self.ctx)


class 랜덤(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=34):
            self.set_ladder(trigger_ids=[701], visible=True, enable=True)
            self.set_ladder(trigger_ids=[702], visible=True, enable=True)
            return 종료(self.ctx)
        if self.random_condition(weight=33):
            self.set_ladder(trigger_ids=[711], visible=True, enable=True)
            self.set_ladder(trigger_ids=[712], visible=True, enable=True)
            return 종료(self.ctx)
        if self.random_condition(weight=33):
            self.set_ladder(trigger_ids=[721], visible=True, enable=True)
            self.set_ladder(trigger_ids=[722], visible=True, enable=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
