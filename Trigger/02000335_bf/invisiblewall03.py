""" trigger/02000335_bf/invisiblewall03.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7040,7041,7042,7043,7044,7045,7046,7047,7048,7049,7050], visible=False, arg4=0, arg5=10) # 벽 해제


