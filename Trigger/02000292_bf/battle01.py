""" trigger/02000292_bf/battle01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        destroy_monster(spawnIds=[1002])
        destroy_monster(spawnIds=[1003])
        destroy_monster(spawnIds=[1004])
        destroy_monster(spawnIds=[1005])
        destroy_monster(spawnIds=[2001])
        destroy_monster(spawnIds=[2002])
        destroy_monster(spawnIds=[2003])
        destroy_monster(spawnIds=[2004])
        destroy_monster(spawnIds=[2005])

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1001,1002,1003,1004,1005]):
            return MobBattle01()


class MobBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True) # Dark_Intro_Chord
        change_monster(removeSpawnId=1001, addSpawnId=2001)
        change_monster(removeSpawnId=1002, addSpawnId=2002)
        change_monster(removeSpawnId=1003, addSpawnId=2003)
        change_monster(removeSpawnId=1004, addSpawnId=2004)
        change_monster(removeSpawnId=1005, addSpawnId=2005)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LadderOff01()


class LadderOff01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002925, textId=20002925, duration=3000)
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


