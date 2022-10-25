""" trigger/63000017_cs/chat01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


class Delay01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return Chat01(self.ctx)


class Chat01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__0$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__1$', arg4=4, arg5=5)
        self.set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__2$', arg4=4, arg5=10)
        self.set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__3$', arg4=4, arg5=16)
        self.set_conversation(type=1, spawnId=103, script='$63000017_CS__CHAT01__4$', arg4=4, arg5=20)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=25000):
            return Delay02(self.ctx)


class Delay02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Chat02(self.ctx)


class Chat02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=101, script='$63000017_CS__CHAT01__5$', arg4=4, arg5=0)
        self.set_conversation(type=1, spawnId=102, script='$63000017_CS__CHAT01__6$', arg4=4, arg5=6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Delay03(self.ctx)


class Delay03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=5000):
            return Delay01(self.ctx)


class Quit(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9900]):
            return Delay01(self.ctx)


initial_state = Wait
