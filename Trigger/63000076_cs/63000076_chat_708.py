""" trigger/63000076_cs/63000076_chat_708.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[708]):
            return 잡담_01_708(self.ctx)


class 잡담_01_708(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=108, msg='$63000076_CS__63000076_CHAT_708__0$', duration=2500, delayTick=0) # 너도 $npcName:11004372$가 불러서 왔어?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_02_708(self.ctx)


class 잡담_02_708(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=115, msg='$63000076_CS__63000076_CHAT_708__1$', duration=2500, delayTick=0) # 아니, 너 따라 왔어

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_03_708(self.ctx)


class 잡담_03_708(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=108, msg='$63000076_CS__63000076_CHAT_708__2$', duration=2500, delayTick=0) # 아하…

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 준비
