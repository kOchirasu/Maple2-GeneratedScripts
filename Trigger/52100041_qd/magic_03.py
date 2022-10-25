""" trigger/52100041_qd/magic_03.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002074], stateValue=0):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7003], visible=False)
        self.set_mesh(triggerIds=[1103], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1203], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[203]):
            return Event_03(self.ctx)


class Event_03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[165,166,167,168,169], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=165, sequenceName='Down_Idle_A', duration=600000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_03_b(self.ctx)


class Event_03_b(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=168, patrolName='MS2PatrolData_2138')
        self.set_npc_emotion_loop(spawnId=165, sequenceName='Down_Idle_A', duration=600000)
        self.set_conversation(type=1, spawnId=165, script='$52100041_QD__MAGIC_03__0$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=169, script='$52100041_QD__MAGIC_03__1$', arg4=3, arg5=2)
        self.set_conversation(type=1, spawnId=168, script='$52100041_QD__MAGIC_03__2$', arg4=3, arg5=1)
        self.set_conversation(type=1, spawnId=168, script='$52100041_QD__MAGIC_03__3$', arg4=3, arg5=6)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11000):
            return Event_03_c(self.ctx)


class Event_03_c(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[165,166,167,168,169])


initial_state = idle
