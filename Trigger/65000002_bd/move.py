""" trigger/65000002_bd/move.xml """
from common import *
import state


class 이동(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=102, boxId=10):
            return 이동()


