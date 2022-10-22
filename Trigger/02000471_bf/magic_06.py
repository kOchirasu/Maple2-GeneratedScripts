""" trigger/02000471_bf/magic_06.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040315, key='10002024clear', value=0)
        set_user_value(triggerId=2040321, key='10002024clear', value=0)
        set_user_value(triggerId=2040322, key='10002024clear', value=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002024], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7006], visible=False)
        set_mesh(triggerIds=[1106], visible=False, arg3=0, arg4=200, arg5=15)
        set_mesh(triggerIds=[1206], visible=True, arg3=0, arg4=200, arg5=15)
        create_monster(spawnIds=[206], arg2=False)
        add_buff(boxIds=[206], skillId=70002051, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[206]):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040315, key='10002024clear', value=1)
        set_user_value(triggerId=2040321, key='10002024clear', value=1)
        set_user_value(triggerId=2040322, key='10002024clear', value=1)
        set_achievement(triggerId=716, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[1101,1102,1103,1104,1105], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_06_b()


class Event_06_b(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1103, script='$02000471_BF__MAGIC_06__0$', arg4=3, arg5=1)
        set_npc_emotion_sequence(spawnId=1103, sequenceName='Talk_A')
        set_conversation(type=1, spawnId=1104, script='$02000471_BF__MAGIC_06__1$', arg4=3, arg5=4)
        set_conversation(type=1, spawnId=1103, script='$02000471_BF__MAGIC_06__2$', arg4=3, arg5=7)
        set_conversation(type=1, spawnId=1104, script='$02000471_BF__MAGIC_06__3$', arg4=3, arg5=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06_c()


class Event_06_c(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=1104, sequenceName='Talk_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return Event_06_d()


class Event_06_d(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1103,1104,1105,1101,1102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return Event_06_e()


class Event_06_e(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return Event_06_f()


class Event_06_f(state.State):
    def on_enter(self):
        set_achievement(triggerId=702, type='trigger', achieve='Hauntedmansion')
        create_monster(spawnIds=[1107,1108], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Event_06_g()


class Event_06_g(state.State):
    def on_enter(self):
        move_npc(spawnId=1107, patrolName='MS2PatrolData_2140')
        move_npc(spawnId=1108, patrolName='MS2PatrolData_2141')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=11000):
            return Event_06_h()


class Event_06_h(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1107, script='$02000471_BF__MAGIC_06__4$', arg4=5, arg5=0)
        set_conversation(type=1, spawnId=1108, script='$02000471_BF__MAGIC_06__5$', arg4=3, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Event_06_i()


class Event_06_i(state.State):
    def on_enter(self):
        move_npc(spawnId=1107, patrolName='MS2PatrolData_2142')
        set_conversation(type=1, spawnId=1107, script='$02000471_BF__MAGIC_06__6$', arg4=5, arg5=0)
        set_conversation(type=1, spawnId=1108, script='$02000471_BF__MAGIC_06__7$', arg4=3, arg5=3)
        set_conversation(type=1, spawnId=1107, script='$02000471_BF__MAGIC_06__8$', arg4=3, arg5=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Event_06_j()


class Event_06_j(state.State):
    def on_enter(self):
        move_npc(spawnId=1108, patrolName='MS2PatrolData_2143')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return Event_06_k()


class Event_06_k(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1107,1108])


