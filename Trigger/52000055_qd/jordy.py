""" trigger/52000055_qd/jordy.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[60100120,60100121,60100122,60100123,60100124,60100125,60100126,60100127,60100128,60100129,60100130], questStates=[1]):
            return jordy()
        if quest_user_detected(boxIds=[9000], questIds=[60100235,60100236,60100237,60100238,60100239,60100240], questStates=[2]):
            return jordy()


#  조디 스폰 
class jordy(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=False) # 조디


