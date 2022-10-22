""" trigger/02000292_bf/battle05.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[117,118,119,120], visible=False, arg3=0, arg4=0, arg5=2)
        destroy_monster(spawnIds=[1020])
        destroy_monster(spawnIds=[1021])
        destroy_monster(spawnIds=[1022])
        destroy_monster(spawnIds=[1023])
        destroy_monster(spawnIds=[1024])
        destroy_monster(spawnIds=[2020])
        destroy_monster(spawnIds=[2021])
        destroy_monster(spawnIds=[2022])
        destroy_monster(spawnIds=[2023])
        destroy_monster(spawnIds=[2024])
        set_effect(triggerIds=[5004], visible=False) # Dark_Intro_Chord

    def on_tick(self) -> state.State:
        if check_user():
            return MobSpawn01()


class MobSpawn01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1020], arg2=False)
        create_monster(spawnIds=[1021], arg2=False)
        create_monster(spawnIds=[1022], arg2=False)
        create_monster(spawnIds=[1023], arg2=False)
        create_monster(spawnIds=[1024], arg2=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[1020,1021,1022,1023,1024]):
            return MobBattle01()


class MobBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True) # Dark_Intro_Chord
        change_monster(removeSpawnId=1020, addSpawnId=2015)
        change_monster(removeSpawnId=1021, addSpawnId=2016)
        change_monster(removeSpawnId=1022, addSpawnId=2017)
        change_monster(removeSpawnId=1023, addSpawnId=2018)
        change_monster(removeSpawnId=1024, addSpawnId=2019)
        create_monster(spawnIds=[1025], arg2=False)
        set_mesh(triggerIds=[117,118,119,120], visible=True, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BlockOn01()


class BlockOn01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002923, textId=20002923)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1025]):
            return BlockOff01()


class BlockOff01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002923)
        set_mesh(triggerIds=[117,118,119,120], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Quit()


class Quit(state.State):
    pass


