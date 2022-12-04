""" trigger/63000076_cs/63000076_interact_1392.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[115], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001392], stateValue=0):
            return 화난요정_01_1392(self.ctx)


class 화난요정_01_1392(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.destroy_monster(spawnIds=[115])
        self.create_monster(spawnIds=[208], animationEffect=True)
        self.create_monster(spawnIds=[215], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[208,215]):
            return 화난요정_02_1392(self.ctx)


class 화난요정_02_1392(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 화난요정_03_1392(self.ctx)


class 화난요정_03_1392(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[115], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
