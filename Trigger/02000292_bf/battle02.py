""" trigger/02000292_bf/battle02.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[501], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[502], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[503], visible=True, animationEffect=True)
        self.destroy_monster(spawnIds=[1006])
        self.destroy_monster(spawnIds=[1007])
        self.destroy_monster(spawnIds=[1008])
        self.destroy_monster(spawnIds=[1009])
        self.destroy_monster(spawnIds=[1010])
        self.destroy_monster(spawnIds=[2006])
        self.destroy_monster(spawnIds=[2007])
        self.destroy_monster(spawnIds=[2008])
        self.destroy_monster(spawnIds=[2009])
        self.destroy_monster(spawnIds=[2010])
        self.set_effect(triggerIds=[5001], visible=False) # Dark_Intro_Chord
        self.set_interact_object(triggerIds=[10001061], state=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1006], animationEffect=False)
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.create_monster(spawnIds=[1008], animationEffect=False)
        self.create_monster(spawnIds=[1009], animationEffect=False)
        self.create_monster(spawnIds=[1010], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[1006,1007,1008,1009,1010]):
            return MobBattle01(self.ctx)


class MobBattle01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # Dark_Intro_Chord
        self.change_monster(removeSpawnId=1006, addSpawnId=2006)
        self.change_monster(removeSpawnId=1007, addSpawnId=2007)
        self.change_monster(removeSpawnId=1008, addSpawnId=2008)
        self.change_monster(removeSpawnId=1009, addSpawnId=2009)
        self.change_monster(removeSpawnId=1010, addSpawnId=2010)
        self.set_ladder(triggerIds=[501], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[502], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[503], visible=False, animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        self.set_interact_object(triggerIds=[10001061], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001061], stateValue=0):
            return LadderOn01(self.ctx)


class LadderOn01(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[501], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[502], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[503], visible=True, animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
