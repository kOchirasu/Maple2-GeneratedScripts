""" trigger/80000012_bonus/camera_restore.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return camera_restore(self.ctx)


class camera_restore(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return idle(self.ctx)


initial_state = idle
