""" trigger/52020019_qd/eone.xml """
import common


class Idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60200010], questStates=[1]):
            return Talk(self.ctx)


class Talk(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='무엄하군요! 저리 가세요!', duration=3000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return Idle(self.ctx)


initial_state = Idle
