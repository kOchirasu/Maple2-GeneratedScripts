""" trigger/99999910/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701]):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    pass


initial_state = idle
