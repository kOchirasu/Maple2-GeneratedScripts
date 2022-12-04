""" trigger/52100041_qd/magic_05.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002076], stateValue=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7005], visible=False)
        self.set_mesh(triggerIds=[1105], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1205], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[205], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[205]):
            return Event_05(self.ctx)


class Event_05(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[145,146,147], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_05_b(self.ctx)


class Event_05_b(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=147, patrolName='MS2PatrolData_2136')
        self.set_conversation(type=1, spawnId=147, script='$52100041_QD__MAGIC_05__0$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=145, script='$52100041_QD__MAGIC_05__1$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=146, script='$52100041_QD__MAGIC_05__1$', arg4=3, arg5=5)
        self.set_conversation(type=1, spawnId=147, script='$52100041_QD__MAGIC_05__3$', arg4=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Event_05_c(self.ctx)


class Event_05_c(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[148], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Event_05_d(self.ctx)


class Event_05_d(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=148, patrolName='MS2PatrolData_2137')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05_e(self.ctx)


class Event_05_e(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[145,146,147])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Event_05_f(self.ctx)


class Event_05_f(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[148])


initial_state = idle
