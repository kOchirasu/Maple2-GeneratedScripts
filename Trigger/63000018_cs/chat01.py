""" trigger/63000018_cs/chat01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101,102], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return Chat01(self.ctx)


class Chat01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000018_CS__CHAT01__0$', time=4, arg5=0)
        self.set_dialogue(type=1, spawn_id=102, script='$63000018_CS__CHAT01__1$', time=4, arg5=4)
        self.set_dialogue(type=1, spawn_id=101, script='$63000018_CS__CHAT01__2$', time=4, arg5=8)
        self.set_dialogue(type=1, spawn_id=102, script='$63000018_CS__CHAT01__3$', time=4, arg5=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=16000):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9900]):
            return Quit(self.ctx)
        if self.wait_tick(wait_tick=20000):
            return Delay01(self.ctx)


class Quit(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9900]):
            return Delay01(self.ctx)


initial_state = Wait
