""" trigger/02000389_bf/error.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Error', value=1):
            return end(self.ctx)
        if self.user_detected(boxIds=[702]):
            return error(self.ctx)


class error(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_random_user(mapId=2000389, portalId=5, triggerId=702, count=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
