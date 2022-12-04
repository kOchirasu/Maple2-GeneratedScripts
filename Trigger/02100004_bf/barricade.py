""" trigger/02100004_bf/barricade.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleStart', value=1):
            return 카운트(self.ctx)


class 카운트(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000384_BF__BARRICADE__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=30000):
            return 차단(self.ctx)


class 차단(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='BattleEnd', value=1):
            return 차단해제(self.ctx)


class 차단해제(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)


initial_state = 대기
