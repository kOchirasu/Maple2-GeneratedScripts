""" trigger/02000471_bf/event_05.xml """
import common


class none(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[706]):
            return idle(self.ctx)


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[121,154,122,156,110]):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=706, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[1110,1111,1112,1113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1110, script='$02000471_BF__EVENT_05__0$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=1111, script='$02000471_BF__EVENT_05__1$', arg4=3, arg5=5)
        self.set_conversation(type=1, spawnId=1112, script='$02000471_BF__EVENT_05__2$', arg4=3, arg5=1)
        self.set_conversation(type=1, spawnId=1113, script='$02000471_BF__EVENT_05__3$', arg4=3, arg5=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            return exit(self.ctx)


class exit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1110,1111,1112,1113])


initial_state = none
