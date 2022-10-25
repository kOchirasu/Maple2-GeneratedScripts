""" trigger/63000018_cs/chat02.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return Chat01(self.ctx)


class Chat01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=201, script='$63000018_CS__CHAT02__0$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=202, script='$63000018_CS__CHAT02__1$', arg4=4, arg5=4)
        self.set_conversation(type=1, spawnId=201, script='$63000018_CS__CHAT02__2$', arg4=4, arg5=8)
        self.set_conversation(type=1, spawnId=202, script='$63000018_CS__CHAT02__3$', arg4=4, arg5=12)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=16000):
            return Delay02(self.ctx)


class Delay02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=12000):
            return Delay01(self.ctx)


class Quit(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


initial_state = Wait
