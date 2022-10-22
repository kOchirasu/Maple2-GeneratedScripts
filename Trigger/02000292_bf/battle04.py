""" trigger/02000292_bf/battle04.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[521], visible=True, animationEffect=True)
        set_ladder(triggerIds=[522], visible=True, animationEffect=True)
        set_ladder(triggerIds=[523], visible=True, animationEffect=True)
        set_ladder(triggerIds=[524], visible=True, animationEffect=True)
        set_ladder(triggerIds=[525], visible=True, animationEffect=True)
        destroy_monster(spawnIds=[1015])
        destroy_monster(spawnIds=[1016])
        destroy_monster(spawnIds=[1017])
        destroy_monster(spawnIds=[1018])
        destroy_monster(spawnIds=[1019])
        destroy_monster(spawnIds=[2015])
        destroy_monster(spawnIds=[2016])
        destroy_monster(spawnIds=[2017])
        destroy_monster(spawnIds=[2018])
        destroy_monster(spawnIds=[2019])
        set_effect(triggerIds=[5003], visible=False) # Dark_Intro_Chord
        set_interact_object(triggerIds=[10001063], state=0)

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1015], arg2=False)
        create_monster(spawnIds=[1016], arg2=False)
        create_monster(spawnIds=[1017], arg2=False)
        create_monster(spawnIds=[1018], arg2=False)
        create_monster(spawnIds=[1019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1015,1016,1017,1018,1019]):
            return MobBattle01()


class MobBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True) # Dark_Intro_Chord
        change_monster(removeSpawnId=1015, addSpawnId=2015)
        change_monster(removeSpawnId=1016, addSpawnId=2016)
        change_monster(removeSpawnId=1017, addSpawnId=2017)
        change_monster(removeSpawnId=1018, addSpawnId=2018)
        change_monster(removeSpawnId=1019, addSpawnId=2019)
        set_ladder(triggerIds=[521], visible=False, animationEffect=False)
        set_ladder(triggerIds=[522], visible=False, animationEffect=False)
        set_ladder(triggerIds=[523], visible=False, animationEffect=False)
        set_ladder(triggerIds=[524], visible=False, animationEffect=False)
        set_ladder(triggerIds=[525], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LadderOff01()


class LadderOff01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        set_interact_object(triggerIds=[10001063], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001063], arg2=0):
            return LadderOn01()


class LadderOn01(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[521], visible=True, animationEffect=True)
        set_ladder(triggerIds=[522], visible=True, animationEffect=True)
        set_ladder(triggerIds=[523], visible=True, animationEffect=True)
        set_ladder(triggerIds=[524], visible=True, animationEffect=True)
        set_ladder(triggerIds=[525], visible=True, animationEffect=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


