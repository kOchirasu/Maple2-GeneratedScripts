""" trigger/02000403_bf/magic_01.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[12000031], stateValue=0):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False)
        self.set_mesh(triggerIds=[1101], visible=False, arg3=0, delay=200, scale=15)
        self.set_mesh(triggerIds=[1201], visible=True, arg3=0, delay=200, scale=15)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            return Event_01(self.ctx)


class Event_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=711, type='trigger', achieve='Hauntedmansion')
        self.create_monster(spawnIds=[161,162,163], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Event_01_b(self.ctx)


class Event_01_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=161, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=162, sequenceName='Bore_A')
        self.set_npc_emotion_sequence(spawnId=163, sequenceName='Bore_A')
        self.set_conversation(type=1, spawnId=161, script='$02000403_BF__MAGIC_01__0$', arg4=3, arg5=2)
        self.set_conversation(type=1, spawnId=162, script='$02000403_BF__MAGIC_01__1$', arg4=3, arg5=4)
        self.set_conversation(type=1, spawnId=163, script='$02000403_BF__MAGIC_01__2$', arg4=3, arg5=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return Event_01_c(self.ctx)


class Event_01_c(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[161,162,163])


initial_state = idle
