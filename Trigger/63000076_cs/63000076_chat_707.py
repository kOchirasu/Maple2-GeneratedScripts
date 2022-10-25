""" trigger/63000076_cs/63000076_chat_707.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[707]):
            return 잡담_01_707(self.ctx)


class 잡담_01_707(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=119, msg='$63000076_CS__63000076_CHAT_707__0$', duration=2500, delayTick=0) # 이거 이거 열어봐도 돼요?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_02_707(self.ctx)


class 잡담_02_707(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=119, msg='$63000076_CS__63000076_CHAT_707__1$', duration=2500, delayTick=0) # 안 돼요?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 준비
