""" trigger/80000012_bonus/camera_restore.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return camera_restore(self.ctx)


class camera_restore(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8001, enable=True)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return idle(self.ctx)


initial_state = idle
