""" trigger/02000292_bf/battle03.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[515], visible=True, animationEffect=True)
        self.destroy_monster(spawnIds=[1011])
        self.destroy_monster(spawnIds=[1012])
        self.destroy_monster(spawnIds=[1013])
        self.destroy_monster(spawnIds=[1014])
        self.destroy_monster(spawnIds=[2011])
        self.destroy_monster(spawnIds=[2012])
        self.destroy_monster(spawnIds=[2013])
        self.destroy_monster(spawnIds=[2014])
        self.set_effect(triggerIds=[5002], visible=False) # Dark_Intro_Chord
        self.set_interact_object(triggerIds=[10001062], state=0)

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1011], animationEffect=False)
        self.create_monster(spawnIds=[1012], animationEffect=False)
        self.create_monster(spawnIds=[1013], animationEffect=False)
        self.create_monster(spawnIds=[1014], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[1011,1012,1013,1014]):
            return MobBattle01(self.ctx)


class MobBattle01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5002], visible=True) # Dark_Intro_Chord
        self.change_monster(removeSpawnId=1011, addSpawnId=2011)
        self.change_monster(removeSpawnId=1012, addSpawnId=2012)
        self.change_monster(removeSpawnId=1013, addSpawnId=2013)
        self.change_monster(removeSpawnId=1014, addSpawnId=2014)
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[515], visible=False, animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        self.set_interact_object(triggerIds=[10001062], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001062], stateValue=0):
            return LadderOn01(self.ctx)


class LadderOn01(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[515], visible=True, animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
