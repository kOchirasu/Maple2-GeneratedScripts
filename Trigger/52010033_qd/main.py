""" trigger/52010033_qd/main.xml """
from common import *
import state


#  페리온 병원 : 52010033  
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003075,10003076,10003077,10003078,10003079], questStates=[1]):
            return NpcSpawn()


class NpcSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105], arg2=True) # 상처입은 추격대원
        create_monster(spawnIds=[106], arg2=True) # 상처입은 추격대원
        create_monster(spawnIds=[107], arg2=True) # 상처입은 추격대원
        create_monster(spawnIds=[108], arg2=True) # 상처입은 추격대원


