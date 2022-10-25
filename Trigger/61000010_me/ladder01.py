""" trigger/61000010_me/ladder01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[701], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[702], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[711], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[712], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[721], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[722], visible=False, animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 랜덤(self.ctx)


class 랜덤(common.Trigger):
    def on_tick(self) -> common.Trigger:
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


class 종료(common.Trigger):
    pass


initial_state = 대기
