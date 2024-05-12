""" trigger/02000292_bf/battle05.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[117,118,119,120], visible=False, arg3=0, delay=0, scale=2)
        self.destroy_monster(spawnIds=[1020])
        self.destroy_monster(spawnIds=[1021])
        self.destroy_monster(spawnIds=[1022])
        self.destroy_monster(spawnIds=[1023])
        self.destroy_monster(spawnIds=[1024])
        self.destroy_monster(spawnIds=[2020])
        self.destroy_monster(spawnIds=[2021])
        self.destroy_monster(spawnIds=[2022])
        self.destroy_monster(spawnIds=[2023])
        self.destroy_monster(spawnIds=[2024])
        self.set_effect(triggerIds=[5004], visible=False) # Dark_Intro_Chord

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return MobSpawn01(self.ctx)


class MobSpawn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1020], animationEffect=False)
        self.create_monster(spawnIds=[1021], animationEffect=False)
        self.create_monster(spawnIds=[1022], animationEffect=False)
        self.create_monster(spawnIds=[1023], animationEffect=False)
        self.create_monster(spawnIds=[1024], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[1020,1021,1022,1023,1024]):
            return MobBattle01(self.ctx)


class MobBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=True) # Dark_Intro_Chord
        self.change_monster(removeSpawnId=1020, addSpawnId=2015)
        self.change_monster(removeSpawnId=1021, addSpawnId=2016)
        self.change_monster(removeSpawnId=1022, addSpawnId=2017)
        self.change_monster(removeSpawnId=1023, addSpawnId=2018)
        self.change_monster(removeSpawnId=1024, addSpawnId=2019)
        self.create_monster(spawnIds=[1025], animationEffect=False)
        self.set_mesh(triggerIds=[117,118,119,120], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BlockOn01(self.ctx)


class BlockOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002923, textId=20002923)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1025]):
            return BlockOff01(self.ctx)


class BlockOff01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20002923)
        self.set_mesh(triggerIds=[117,118,119,120], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
