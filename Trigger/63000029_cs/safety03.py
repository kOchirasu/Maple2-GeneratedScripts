""" trigger/63000029_cs/safety03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='SafetyStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SafetyStart', value=1):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000029, portalId=12, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9200]):
            return Enter01(self.ctx)


initial_state = Wait
