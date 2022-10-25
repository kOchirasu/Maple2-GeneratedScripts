""" trigger/02000539_bf/talk.xml """
import common


# 플레이어 감지
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 말풍선1(self.ctx)
        if self.user_detected(boxIds=[704], jobCode=0):
            return 말풍선2(self.ctx)


class 말풍선1(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='$02000539_BF__TALK__0$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=201, msg='$02000539_BF__TALK__1$', duration=3500, delayTick=3500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return idle(self.ctx)


class 말풍선2(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__2$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__3$', duration=3500, delayTick=3500)
        self.add_balloon_talk(spawnId=202, msg='$02000539_BF__TALK__4$', duration=3500, delayTick=7000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return idle(self.ctx)


initial_state = idle
