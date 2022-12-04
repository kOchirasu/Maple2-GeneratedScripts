""" trigger/63000076_cs/63000076_interact_1394.xml """
import trigger_api


class 준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001394], stateValue=0):
            return 화난요정_01_1394(self.ctx)


class 화난요정_01_1394(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.create_monster(spawnIds=[202], animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=True)
        self.create_monster(spawnIds=[204], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203,204]):
            return 화난요정_02_1394(self.ctx)


class 화난요정_02_1394(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 화난요정_03_1394(self.ctx)


class 화난요정_03_1394(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.create_monster(spawnIds=[102], animationEffect=True)
        self.create_monster(spawnIds=[103], animationEffect=True)
        self.create_monster(spawnIds=[104], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 준비
