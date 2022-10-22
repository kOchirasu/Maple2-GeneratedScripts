""" trigger/02000335_bf/invisiblewall06.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=708, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    pass


