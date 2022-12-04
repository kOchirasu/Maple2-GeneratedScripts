""" trigger/80000012_bonus/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[199], animationEffect=False) # 웨이브 장치 작동

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='60'):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
