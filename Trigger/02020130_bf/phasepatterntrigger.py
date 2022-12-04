""" trigger/02020130_bf/phasepatterntrigger.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='PhaseSumTotal', value=0) # PhaseSumTotal 변수 0으로 초기 세팅
        self.set_user_value(key='PhasePatternTrigger', value=0) # PhasePatternTrigger 변수 0으로 초기 세팅

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=601, boxId=1):
            return 보스3마리_페이즈전환계산(self.ctx)


class 보스3마리_페이즈전환계산(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal', value=3, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_2페이즈(self.ctx)


class 보스3마리_페이즈전환실행_2페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='PhasePatternTrigger', value=2) # PhasePatternTrigger = 2 신호를 보스 3마리한테 보내서 2페이즈로 전환하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal', value=9, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_3페이즈(self.ctx)


class 보스3마리_페이즈전환실행_3페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='PhasePatternTrigger', value=3) # PhasePatternTrigger = 3 신호를 보스 3마리한테 보내서 3페이즈로 전환하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal', value=15, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_4페이즈(self.ctx)


class 보스3마리_페이즈전환실행_4페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='PhasePatternTrigger', value=4) # PhasePatternTrigger = 4 신호를 보스 3마리한테 보내서 4페이즈로 전환하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='PhaseSumTotal', value=18, operator='GreaterEqual'):
            return 보스3마리_페이즈전환실행_5페이즈(self.ctx)


class 보스3마리_페이즈전환실행_5페이즈(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='PhasePatternTrigger', value=5) # PhasePatternTrigger = 5 신호를 보스 3마리한테 보내서 5페이즈로 전환하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
