""" trigger/99999927/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return ready()


class ready(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=99910120, level=1, arg4=False, arg5=False)
        set_gravity(gravity=-25)
        create_monster(spawnIds=[201], arg2=True)


