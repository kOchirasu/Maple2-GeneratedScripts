""" trigger/63000076_cs/63000076_interact_1395.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[116], animationEffect=False)
        self.create_monster(spawnIds=[117], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001395], stateValue=0):
            return 화난요정_01_1395(self.ctx)


class 화난요정_01_1395(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[116])
        self.destroy_monster(spawnIds=[117])
        self.create_monster(spawnIds=[216], animationEffect=True)
        self.create_monster(spawnIds=[217], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[216,217]):
            return 화난요정_02_1395(self.ctx)


class 화난요정_02_1395(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 화난요정_03_1395(self.ctx)


class 화난요정_03_1395(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[116], animationEffect=False)
        self.create_monster(spawnIds=[117], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
