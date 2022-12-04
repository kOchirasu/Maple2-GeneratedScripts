""" trigger/52000120_qd/03_leftshieldbarrier.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3201], visible=True, arg3=0, delay=0, scale=0) # Invisible_Barrier
        self.destroy_monster(spawnIds=[990,991,992,993,994,995])
        self.set_skill(triggerIds=[7001], enable=False) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return ActivateShiled01(self.ctx)


class ActivateShiled01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[990,991,992,993,994,995], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9201]):
            return Push01(self.ctx)


class Push01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=990, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=991, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=992, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=993, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=994, sequenceName='Attack_01_A')
        self.set_npc_emotion_sequence(spawnId=995, sequenceName='Attack_01_A')
        self.set_skill(triggerIds=[7001], enable=True) # Push

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1333):
            return Reset01(self.ctx)


class Reset01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9201]):
            return Push01(self.ctx)


initial_state = Wait
