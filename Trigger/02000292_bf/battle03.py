""" trigger/02000292_bf/battle03.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        set_ladder(triggerIds=[515], visible=True, animationEffect=True)
        destroy_monster(spawnIds=[1011])
        destroy_monster(spawnIds=[1012])
        destroy_monster(spawnIds=[1013])
        destroy_monster(spawnIds=[1014])
        destroy_monster(spawnIds=[2011])
        destroy_monster(spawnIds=[2012])
        destroy_monster(spawnIds=[2013])
        destroy_monster(spawnIds=[2014])
        set_effect(triggerIds=[5002], visible=False) # Dark_Intro_Chord
        set_interact_object(triggerIds=[10001062], state=0)

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1011], arg2=False)
        create_monster(spawnIds=[1012], arg2=False)
        create_monster(spawnIds=[1013], arg2=False)
        create_monster(spawnIds=[1014], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1011,1012,1013,1014]):
            return MobBattle01()


class MobBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True) # Dark_Intro_Chord
        change_monster(removeSpawnId=1011, addSpawnId=2011)
        change_monster(removeSpawnId=1012, addSpawnId=2012)
        change_monster(removeSpawnId=1013, addSpawnId=2013)
        change_monster(removeSpawnId=1014, addSpawnId=2014)
        set_ladder(triggerIds=[511], visible=False, animationEffect=False)
        set_ladder(triggerIds=[512], visible=False, animationEffect=False)
        set_ladder(triggerIds=[513], visible=False, animationEffect=False)
        set_ladder(triggerIds=[514], visible=False, animationEffect=False)
        set_ladder(triggerIds=[515], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LadderOff01()


class LadderOff01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        set_interact_object(triggerIds=[10001062], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001062], arg2=0):
            return LadderOn01()


class LadderOn01(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        set_ladder(triggerIds=[515], visible=True, animationEffect=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


