""" trigger/02000471_bf/event_05.xml """
from common import *
import state


class none(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706]):
            return idle()


class idle(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,154,122,156,110]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_achievement(triggerId=706, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[1110,1111,1112,1113], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return start()


class start(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1110, script='$02000471_BF__EVENT_05__0$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=1111, script='$02000471_BF__EVENT_05__1$', arg4=3, arg5=5)
        set_conversation(type=1, spawnId=1112, script='$02000471_BF__EVENT_05__2$', arg4=3, arg5=1)
        set_conversation(type=1, spawnId=1113, script='$02000471_BF__EVENT_05__3$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return exit()


class exit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1110,1111,1112,1113])


