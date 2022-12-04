""" trigger/84000007_wd/09_fireworks.xml """
import trigger_api


class Staging(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Fireworks', value=1):
            return Volley_Ready(self.ctx)
        if self.user_value(key='Fireworks', value=2):
            return Volley_Ready2(self.ctx)


class Volley_Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$84000007_WD__09_FIREWORKS__0$', arg3='3000', arg4='0')
        # action name="카메라경로를선택한다" arg1="902,903" arg2="1"/

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Volley_Fire(self.ctx)


class Volley_Ready2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$84000007_WD__09_FIREWORKS__1$', arg3='3000', arg4='0')
        # action name="카메라경로를선택한다" arg1="902,903" arg2="1"/

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Volley_Fire(self.ctx)


class Volley_Fire(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=14000):
            return None


initial_state = Staging
