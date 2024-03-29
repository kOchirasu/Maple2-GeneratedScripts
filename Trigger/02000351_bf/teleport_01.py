""" trigger/02000351_bf/teleport_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=1):
            return start_sound(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[9000005], visible=True) # TeleportSound EFfect On


class start_sound(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return idle(self.ctx)

    def on_exit(self):
        self.set_effect(triggerIds=[9000005], visible=False) # TeleportSound EFfect On


initial_state = idle
