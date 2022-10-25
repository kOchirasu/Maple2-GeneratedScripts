""" trigger/52020010_qd/main_a.xml """
import common


class Idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_actor(triggerId=8001, visible=False, initialSequence='Event_01_A')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60200045], questStates=[2]):
            return Event_01(self.ctx)


class Event_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Event_02(self.ctx)


class Event_02(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=0, msg='!!!', duration=1000, delayTick=0)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_actor(triggerId=8001, visible=True, initialSequence='Event_03_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_End(self.ctx)


class Event_End(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=8001, visible=False, initialSequence='Event_03_A')
        self.reset_camera(interpolationTime=1)


initial_state = Idle
