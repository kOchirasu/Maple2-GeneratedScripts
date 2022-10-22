""" trigger/80000006_bonus/meso.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            create_item(spawnIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
            create_item(spawnIds=[9001,9002,9003,9004,9005])
            return 완료()


class 완료(state.State):
    pass


