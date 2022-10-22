""" trigger/02000335_bf/invisiblewall05.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=707, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7061,7062,7063,7064,7065,7066,7067,7068,7069,7070], visible=False, arg4=0, arg5=10) # 벽 해제


