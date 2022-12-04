""" trigger/63000018_cs/chat03.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=20000):
            return Chat01(self.ctx)


class Chat01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=301, script='$63000018_CS__CHAT03__0$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=302, script='$63000018_CS__CHAT03__1$', arg4=4, arg5=4)
        self.set_conversation(type=1, spawnId=301, script='$63000018_CS__CHAT03__2$', arg4=4, arg5=8)
        self.set_conversation(type=1, spawnId=302, script='$63000018_CS__CHAT03__3$', arg4=4, arg5=12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=16000):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=4000):
            return Delay01(self.ctx)


class Quit(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


initial_state = Wait
