""" trigger/52010033_qd/main.xml """
import common


# 페리온 병원 : 52010033
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003075,10003076,10003077,10003078,10003079], questStates=[1]):
            return NpcSpawn(self.ctx)


class NpcSpawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[105], animationEffect=True) # 상처입은 추격대원
        self.create_monster(spawnIds=[106], animationEffect=True) # 상처입은 추격대원
        self.create_monster(spawnIds=[107], animationEffect=True) # 상처입은 추격대원
        self.create_monster(spawnIds=[108], animationEffect=True) # 상처입은 추격대원


initial_state = idle
