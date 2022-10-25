""" trigger/99999910/main.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[701]):
            return ready(self.ctx)


class ready(common.Trigger):
    pass


initial_state = idle
