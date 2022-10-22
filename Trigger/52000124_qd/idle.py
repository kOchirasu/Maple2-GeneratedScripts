""" trigger/52000124_qd/idle.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 이브 (11000069)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100140,60100141,60100142,60100143,60100144,60100145,60100146,60100147,60100148,60100149,60100150,60100151,60100152,60100153,60100154,60100155], questStates=[1]):
            return del()


#  delnpc 
class del(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201,202])


