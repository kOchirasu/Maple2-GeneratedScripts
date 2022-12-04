""" trigger/66200001_gd/07_gameguide.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GameGuide', value=1):
            return GameGuide_20(self.ctx)


class GameGuide_20(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=19, startDelay=1, interval=0) # 20sec

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NormalGameGuide_01(self.ctx)


# Normal GameGuide
class NormalGameGuide_01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620104, textId=26620104, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_02(self.ctx)


class NormalGameGuide_02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620105, textId=26620105, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_03(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620104, textId=26620104, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return NormalGameGuide_04(self.ctx)
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


class NormalGameGuide_04(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=26620105, textId=26620105, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return Reset(self.ctx)


# Reset
class Reset(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='GameGuide', value=0)
        self.reset_timer(timerId='1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Wait
