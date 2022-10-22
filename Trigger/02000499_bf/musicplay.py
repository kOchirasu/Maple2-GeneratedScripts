""" trigger/02000499_bf/musicplay.xml """
from common import *
import state


class wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # PlayClarinet
        set_effect(triggerIds=[5103], visible=False) # PlayCello
        set_effect(triggerIds=[5102], visible=False) # PlayViolin
        set_effect(triggerIds=[5104], visible=False) # PlayBox
        set_effect(triggerIds=[5105], visible=False) # PlayBox
        set_interact_object(triggerIds=[11000093], state=1, arg3=False)
        destroy_monster(spawnIds=[210])

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[11000093], arg2=0):
            return ready()


#  
class ready(state.State):
    def on_enter(self):
        write_log(logName='Survival', arg3='MushkingLand_musicPlay') # 로그
        set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCPlayMusic02()


class PCPlayMusic02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=True) # PlayClarinet
        set_effect(triggerIds=[5103], visible=True) # PlayCello
        set_effect(triggerIds=[5102], visible=True) # PlayViolin
        set_effect(triggerIds=[5104], visible=True) # PlayBox
        set_effect(triggerIds=[5105], visible=True) # PlayBox
        create_monster(spawnIds=[210], arg2=False, arg3=0)
        set_npc_emotion_loop(spawnId=201, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=202, sequenceName='Play_A', duration=30500)
        set_npc_emotion_loop(spawnId=203, sequenceName='Play_A', duration=30500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30500):
            return End()


class End(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5101], visible=False) # PlayClarinet
        set_effect(triggerIds=[5103], visible=False) # PlayCello
        set_effect(triggerIds=[5102], visible=False) # PlayViolin
        set_effect(triggerIds=[5104], visible=False) # PlayBox
        set_effect(triggerIds=[5105], visible=False) # PlayBox
        destroy_monster(spawnIds=[210])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait()


