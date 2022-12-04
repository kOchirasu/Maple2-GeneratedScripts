""" trigger/52100041_qd/magic_04.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002075], stateValue=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7004], visible=False)
        self.set_mesh(triggerIds=[1104], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1204], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[204], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[204]):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[144], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_04_b(self.ctx)


class Event_04_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=144, script='$52100041_QD__MAGIC_04__0$', arg4=2, arg5=2)
        self.set_conversation(type=1, spawnId=144, script='$52100041_QD__MAGIC_04__1$', arg4=4, arg5=5)
        self.move_npc(spawnId=144, patrolName='MS2PatrolData_2134')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return Event_04_c(self.ctx)


class Event_04_c(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=144, script='$52100041_QD__MAGIC_04__2$', arg4=3, arg5=1)
        self.set_conversation(type=1, spawnId=144, script='$52100041_QD__MAGIC_04__3$', arg4=3, arg5=4)
        self.move_npc(spawnId=144, patrolName='MS2PatrolData_2135')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return Event_04_d(self.ctx)


class Event_04_d(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[144])


initial_state = idle
