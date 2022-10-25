""" trigger/63000076_cs/63000076_chat_705.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[705]):
            return 잡담_01_705(self.ctx)


class 잡담_01_705(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=116, msg='$63000076_CS__63000076_CHAT_705__0$', duration=2500, delayTick=0) # 이거 누르면 소리 나요

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_02_705(self.ctx)


class 잡담_02_705(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=117, msg='$63000076_CS__63000076_CHAT_705__1$', duration=2500, delayTick=0) # 소리 들어보고 싶어요

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 준비
