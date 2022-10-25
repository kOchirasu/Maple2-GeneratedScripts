""" trigger/02000499_bf/musicplay.xml """
import common


class wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # PlayClarinet
        self.set_effect(triggerIds=[5103], visible=False) # PlayCello
        self.set_effect(triggerIds=[5102], visible=False) # PlayViolin
        self.set_effect(triggerIds=[5104], visible=False) # PlayBox
        self.set_effect(triggerIds=[5105], visible=False) # PlayBox
        self.set_interact_object(triggerIds=[11000093], state=1, arg3=False)
        self.destroy_monster(spawnIds=[210])

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[11000093], stateValue=0):
            return ready(self.ctx)


# 
class ready(common.Trigger):
    def on_enter(self):
        self.write_log(logName='Survival', event='MushkingLand_musicPlay') # 로그
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCPlayMusic02(self.ctx)


class PCPlayMusic02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # PlayClarinet
        self.set_effect(triggerIds=[5103], visible=True) # PlayCello
        self.set_effect(triggerIds=[5102], visible=True) # PlayViolin
        self.set_effect(triggerIds=[5104], visible=True) # PlayBox
        self.set_effect(triggerIds=[5105], visible=True) # PlayBox
        self.create_monster(spawnIds=[210], animationEffect=False, animationDelay=0)
        self.set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        self.set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30500):
            return End(self.ctx)


class End(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # PlayClarinet
        self.set_effect(triggerIds=[5103], visible=False) # PlayCello
        self.set_effect(triggerIds=[5102], visible=False) # PlayViolin
        self.set_effect(triggerIds=[5104], visible=False) # PlayBox
        self.set_effect(triggerIds=[5105], visible=False) # PlayBox
        self.destroy_monster(spawnIds=[210])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return wait(self.ctx)


initial_state = wait
