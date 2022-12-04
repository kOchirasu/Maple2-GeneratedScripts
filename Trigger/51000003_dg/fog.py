""" trigger/51000003_dg/fog.xml """
import trigger_api


# 포그 이펙트
class Round_check(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_effect(triggerIds=[7002], visible=False)
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_effect(triggerIds=[7005], visible=False)
        self.set_effect(triggerIds=[7010], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01', value=1):
            return None # Missing State: Round_01
        if self.user_value(key='Round_02', value=1):
            return Round_02_Ready(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return Round_03_Ready(self.ctx)
        if self.user_value(key='Round_04', value=1):
            return Round_04_Ready(self.ctx)


class Round_02_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return Round_02_Start(self.ctx)


class Round_03_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return Round_03_Start(self.ctx)


class Round_04_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return Round_04_Start(self.ctx)


class Round_05_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return Round_05_Start(self.ctx)


class Round_06_Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=25000):
            return Round_06_Start(self.ctx)


class Round_02_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02', value=0):
            return Round_check(self.ctx)
        if self.wait_tick(waitTick=30000):
            return Round_check(self.ctx)


class Round_03_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03', value=0):
            return Round_check(self.ctx)
        if self.wait_tick(waitTick=30000):
            return Round_check(self.ctx)


class Round_04_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04', value=0):
            return Round_check(self.ctx)
        if self.wait_tick(waitTick=30000):
            return Round_check(self.ctx)


class Round_05_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_05', value=0):
            return Round_check(self.ctx)
        if self.wait_tick(waitTick=30000):
            return Round_check(self.ctx)


class Round_06_Start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_06', value=0):
            return Round_check(self.ctx)
        if self.wait_tick(waitTick=30000):
            return Round_check(self.ctx)


initial_state = Round_check
