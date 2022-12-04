""" trigger/02000292_bf/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001])
        self.destroy_monster(spawnIds=[1002])
        self.destroy_monster(spawnIds=[1003])
        self.destroy_monster(spawnIds=[1004])
        self.destroy_monster(spawnIds=[1005])
        self.destroy_monster(spawnIds=[2001])
        self.destroy_monster(spawnIds=[2002])
        self.destroy_monster(spawnIds=[2003])
        self.destroy_monster(spawnIds=[2004])
        self.destroy_monster(spawnIds=[2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.create_monster(spawnIds=[1005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[1001,1002,1003,1004,1005]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=True) # Dark_Intro_Chord
        self.change_monster(removeSpawnId=1001, addSpawnId=2001)
        self.change_monster(removeSpawnId=1002, addSpawnId=2002)
        self.change_monster(removeSpawnId=1003, addSpawnId=2003)
        self.change_monster(removeSpawnId=1004, addSpawnId=2004)
        self.change_monster(removeSpawnId=1005, addSpawnId=2005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LadderOff01(self.ctx)


class LadderOff01(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002925, textId=20002925, duration=3000)
        self.set_interact_object(triggerIds=[10001061], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001061], stateValue=0):
            return LadderOn01(self.ctx)


class LadderOn01(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[501], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[502], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[503], visible=True, animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
