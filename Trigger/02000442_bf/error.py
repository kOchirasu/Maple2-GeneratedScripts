""" trigger/02000442_bf/error.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Error', value=1):
            return end(self.ctx)
        if self.user_detected(boxIds=[702]):
            return error(self.ctx)


class error(common.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=2000389, portalId=5, triggerId=702, count=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class end(common.Trigger):
    pass


initial_state = idle
