""" trigger/52020039_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000590], questStates=[3]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000600], questStates=[1]):
            return NPC소환(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000600], questStates=[2]):
            return NPC소환(self.ctx)


class NPC소환(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)
        self.create_monster(spawnIds=[106], animationEffect=False)
        self.create_monster(spawnIds=[107], animationEffect=False)
        self.create_monster(spawnIds=[108], animationEffect=False)
        self.create_monster(spawnIds=[109], animationEffect=False)
        self.create_monster(spawnIds=[110], animationEffect=False)
        self.create_monster(spawnIds=[111], animationEffect=False)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.create_monster(spawnIds=[114], animationEffect=False)
        self.create_monster(spawnIds=[115], animationEffect=False)
        self.create_monster(spawnIds=[116], animationEffect=False)
        self.create_monster(spawnIds=[117], animationEffect=False)
        self.create_monster(spawnIds=[118], animationEffect=False)
        self.create_monster(spawnIds=[119], animationEffect=False)
        self.create_monster(spawnIds=[120], animationEffect=False)


initial_state = Ready
