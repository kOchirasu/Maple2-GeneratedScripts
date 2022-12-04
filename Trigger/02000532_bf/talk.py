""" trigger/02000532_bf/talk.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=216, msg='$02000532_BF__TALK__0$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return None # Missing State: 


initial_state = idle
