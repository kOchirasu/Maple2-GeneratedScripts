""" trigger/02000292_bf/battle02.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[501], visible=True, animationEffect=True)
        set_ladder(triggerIds=[502], visible=True, animationEffect=True)
        set_ladder(triggerIds=[503], visible=True, animationEffect=True)
        destroy_monster(spawnIds=[1006])
        destroy_monster(spawnIds=[1007])
        destroy_monster(spawnIds=[1008])
        destroy_monster(spawnIds=[1009])
        destroy_monster(spawnIds=[1010])
        destroy_monster(spawnIds=[2006])
        destroy_monster(spawnIds=[2007])
        destroy_monster(spawnIds=[2008])
        destroy_monster(spawnIds=[2009])
        destroy_monster(spawnIds=[2010])
        set_effect(triggerIds=[5001], visible=False) # Dark_Intro_Chord
        set_interact_object(triggerIds=[10001061], state=0)

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        create_monster(spawnIds=[1009], arg2=False)
        create_monster(spawnIds=[1010], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1006,1007,1008,1009,1010]):
            return MobBattle01()


class MobBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # Dark_Intro_Chord
        change_monster(removeSpawnId=1006, addSpawnId=2006)
        change_monster(removeSpawnId=1007, addSpawnId=2007)
        change_monster(removeSpawnId=1008, addSpawnId=2008)
        change_monster(removeSpawnId=1009, addSpawnId=2009)
        change_monster(removeSpawnId=1010, addSpawnId=2010)
        set_ladder(triggerIds=[501], visible=False, animationEffect=False)
        set_ladder(triggerIds=[502], visible=False, animationEffect=False)
        set_ladder(triggerIds=[503], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LadderOff01()


class LadderOff01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        set_interact_object(triggerIds=[10001061], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001061], arg2=0):
            return LadderOn01()


class LadderOn01(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[501], visible=True, animationEffect=True)
        set_ladder(triggerIds=[502], visible=True, animationEffect=True)
        set_ladder(triggerIds=[503], visible=True, animationEffect=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


