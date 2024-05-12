""" trigger/63000076_cs/63000076_interact_1393.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[109], animationEffect=True)
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001393], stateValue=0):
            return 화난요정_01_1393(self.ctx)


class 화난요정_01_1393(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[109])
        self.destroy_monster(spawnIds=[110])
        self.destroy_monster(spawnIds=[111])
        self.destroy_monster(spawnIds=[112])
        self.destroy_monster(spawnIds=[113])
        self.destroy_monster(spawnIds=[114])
        self.create_monster(spawnIds=[209], animationEffect=True)
        self.create_monster(spawnIds=[210], animationEffect=True)
        self.create_monster(spawnIds=[211], animationEffect=True)
        self.create_monster(spawnIds=[212], animationEffect=True)
        self.create_monster(spawnIds=[213], animationEffect=True)
        self.create_monster(spawnIds=[214], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[209,210,211,212,213,214]):
            return 화난요정_02_1393(self.ctx)


class 화난요정_02_1393(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 화난요정_03_1393(self.ctx)


class 화난요정_03_1393(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.create_monster(spawnIds=[114], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
