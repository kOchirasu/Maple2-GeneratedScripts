""" trigger/02000292_bf/battle04.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[521], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[522], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[523], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[524], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[525], visible=True, animationEffect=True)
        self.destroy_monster(spawnIds=[1015])
        self.destroy_monster(spawnIds=[1016])
        self.destroy_monster(spawnIds=[1017])
        self.destroy_monster(spawnIds=[1018])
        self.destroy_monster(spawnIds=[1019])
        self.destroy_monster(spawnIds=[2015])
        self.destroy_monster(spawnIds=[2016])
        self.destroy_monster(spawnIds=[2017])
        self.destroy_monster(spawnIds=[2018])
        self.destroy_monster(spawnIds=[2019])
        self.set_effect(triggerIds=[5003], visible=False) # Dark_Intro_Chord
        self.set_interact_object(triggerIds=[10001063], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1015], animationEffect=False)
        self.create_monster(spawnIds=[1016], animationEffect=False)
        self.create_monster(spawnIds=[1017], animationEffect=False)
        self.create_monster(spawnIds=[1018], animationEffect=False)
        self.create_monster(spawnIds=[1019], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[1015,1016,1017,1018,1019]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5003], visible=True) # Dark_Intro_Chord
        self.change_monster(removeSpawnId=1015, addSpawnId=2015)
        self.change_monster(removeSpawnId=1016, addSpawnId=2016)
        self.change_monster(removeSpawnId=1017, addSpawnId=2017)
        self.change_monster(removeSpawnId=1018, addSpawnId=2018)
        self.change_monster(removeSpawnId=1019, addSpawnId=2019)
        self.set_ladder(triggerIds=[521], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[522], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[523], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[524], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[525], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002921, textId=20002921, duration=5000)
        self.set_interact_object(triggerIds=[10001063], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001063], stateValue=0):
            return LadderOn01(self.ctx)


class LadderOn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[521], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[522], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[523], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[524], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[525], visible=True, animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
