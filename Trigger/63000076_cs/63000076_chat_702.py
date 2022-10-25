""" trigger/63000076_cs/63000076_chat_702.xml """
import common


class 준비(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[30000375], questStates=[1]):
            return 잡담_01_702(self.ctx)


class 잡담_01_702(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=103, msg='$63000076_CS__63000076_CHAT_702__0$', duration=2000, delayTick=0) # 사람이다! 사람!

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 잡담_02_702(self.ctx)


class 잡담_02_702(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$63000076_CS__63000076_CHAT_702__1$', duration=2500, delayTick=0) # $npcName:11004372$$pp:가,이$ 사람도 초대했나?

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_03_702(self.ctx)


class 잡담_03_702(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=102, msg='$63000076_CS__63000076_CHAT_702__2$', duration=3000, delayTick=0) # $npcName:11004372$$pp:는,은$ 착하니까, 그랬을 수도 있지

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 준비
