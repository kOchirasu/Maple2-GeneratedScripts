""" trigger/99999910/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return ready()


class ready(state.State):
    pass


