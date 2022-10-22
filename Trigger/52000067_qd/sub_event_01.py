""" trigger/52000067_qd/sub_event_01.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[751], arg2=True) # 골두스

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__0$', arg4=3, arg5=0)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__1$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__2$', arg4=3, arg5=6)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__3$', arg4=3, arg5=9)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__4$', arg4=3, arg5=12)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__5$', arg4=3, arg5=15)
        set_conversation(type=1, spawnId=751, script='$52000067_QD__SUB_EVENT_01__6$', arg4=3, arg5=18)
        set_conversation(type=1, spawnId=752, script='$52000067_QD__SUB_EVENT_01__7$', arg4=3, arg5=19)
        set_conversation(type=1, spawnId=753, script='$52000067_QD__SUB_EVENT_01__8$', arg4=3, arg5=19)
        set_conversation(type=1, spawnId=754, script='$52000067_QD__SUB_EVENT_01__9$', arg4=3, arg5=20)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start()


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[757,758,761,762], arg2=True) # 시민
        set_conversation(type=1, spawnId=757, script='$52000067_QD__SUB_EVENT_01__10$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=758, script='$52000067_QD__SUB_EVENT_01__11$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=762, script='$52000067_QD__SUB_EVENT_01__12$', arg4=3, arg5=2)
        set_conversation(type=1, spawnId=761, script='$52000067_QD__SUB_EVENT_01__13$', arg4=3, arg5=2)


