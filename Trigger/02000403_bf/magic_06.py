""" trigger/02000403_bf/magic_06.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[12000036], stateValue=0):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7006], visible=False)
        self.set_mesh(triggerIds=[1106], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1206], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[206], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[206]):
            return Event_06(self.ctx)


class Event_06(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=716, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[1101,1102,1103,1104,1105], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_06_b(self.ctx)


class Event_06_b(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1103, script='$02000403_BF__MAGIC_06__0$', arg4=3, arg5=1)
        self.set_npc_emotion_sequence(spawnId=1103, sequenceName='Talk_A')
        self.set_conversation(type=1, spawnId=1104, script='$02000403_BF__MAGIC_06__1$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=1103, script='$02000403_BF__MAGIC_06__2$', arg4=3, arg5=7)
        self.set_conversation(type=1, spawnId=1104, script='$02000403_BF__MAGIC_06__8$', arg4=3, arg5=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_06_c(self.ctx)


class Event_06_c(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1104, sequenceName='Talk_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=12000):
            return Event_06_d(self.ctx)


class Event_06_d(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1103,1104,1105,1101,1102])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return Event_06_e(self.ctx)


class Event_06_e(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[702]):
            return Event_06_f(self.ctx)


class Event_06_f(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=702, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[1107,1108], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_06_g(self.ctx)


class Event_06_g(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1107, patrolName='MS2PatrolData_2140')
        self.move_npc(spawnId=1108, patrolName='MS2PatrolData_2141')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return Event_06_h(self.ctx)


class Event_06_h(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1107, script='$02000403_BF__MAGIC_06__3$', arg4=5, arg5=0)
        self.set_conversation(type=1, spawnId=1108, script='$02000403_BF__MAGIC_06__4$', arg4=3, arg5=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=8000):
            return Event_06_i(self.ctx)


class Event_06_i(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1107, patrolName='MS2PatrolData_2142')
        self.set_conversation(type=1, spawnId=1107, script='$02000403_BF__MAGIC_06__5$', arg4=5, arg5=0)
        self.set_conversation(type=1, spawnId=1108, script='$02000403_BF__MAGIC_06__6$', arg4=3, arg5=3)
        self.set_conversation(type=1, spawnId=1107, script='$02000403_BF__MAGIC_06__7$', arg4=3, arg5=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_06_j(self.ctx)


class Event_06_j(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1108, patrolName='MS2PatrolData_2143')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return Event_06_k(self.ctx)


class Event_06_k(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1107,1108])


initial_state = idle
