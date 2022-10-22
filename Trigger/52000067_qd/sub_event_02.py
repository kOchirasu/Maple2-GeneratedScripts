""" trigger/52000067_qd/sub_event_02.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7200], visible=False) # 폭발

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return idle_02()


class idle_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[756,755], arg2=True) # 시민
        set_conversation(type=1, spawnId=102, script='$52000067_QD__SUB_EVENT_02__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=101, script='$52000067_QD__SUB_EVENT_02__1$', arg4=3, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ready()


class ready(state.State):
    pass


