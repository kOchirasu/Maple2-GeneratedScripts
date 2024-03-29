""" trigger/63000076_cs/63000076_chat_703.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[703], questIds=[30000375], questStates=[1]):
            return 잡담_01_703(self.ctx)


class 잡담_01_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=109, msg='$63000076_CS__63000076_CHAT_703__0$', duration=2500, delayTick=0) # $npcName:11004372$$pp:는,은$ 왜 안 와?

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_02_703(self.ctx)


class 잡담_02_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=113, msg='$63000076_CS__63000076_CHAT_703__1$', duration=2500, delayTick=0) # 보채지 마

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_03_703(self.ctx)


class 잡담_03_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=109, msg='$63000076_CS__63000076_CHAT_703__2$', duration=2500, delayTick=0) # 얼른 달콤한 거 먹고 싶어

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 잡담_04_703(self.ctx)


class 잡담_04_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=110, msg='$63000076_CS__63000076_CHAT_703__3$', duration=2000, delayTick=0) # 나도 달콤한 거!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 잡담_05_703(self.ctx)


class 잡담_05_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=112, msg='$63000076_CS__63000076_CHAT_703__3$', duration=2000, delayTick=0) # 나도 달콤한 거!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잡담_06_703(self.ctx)


class 잡담_06_703(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=111, msg='$63000076_CS__63000076_CHAT_703__5$', duration=2000, delayTick=0) # 나도!
        self.add_balloon_talk(spawnId=114, msg='$63000076_CS__63000076_CHAT_703__5$', duration=2000, delayTick=0) # 나도!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
