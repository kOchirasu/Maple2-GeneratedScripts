""" trigger/63000076_cs/63000076_chat_704.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704]):
            return 잡담_01_704(self.ctx)


class 잡담_01_704(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=107, msg='$63000076_CS__63000076_CHAT_704__0$', duration=2000, delayTick=0) # 너 피부 좋아졌다?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잡담_02_704(self.ctx)


class 잡담_02_704(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=105, msg='$63000076_CS__63000076_CHAT_704__1$', duration=2500, delayTick=0) # 요즘 스팀 마사지하고 있거든

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
