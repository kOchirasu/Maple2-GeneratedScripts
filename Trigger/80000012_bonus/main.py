""" trigger/80000012_bonus/main.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[199], animationEffect=False) # 웨이브 장치 작동

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            return end(self.ctx)


class end(common.Trigger):
    pass


initial_state = idle
