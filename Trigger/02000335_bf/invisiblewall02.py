""" trigger/02000335_bf/invisiblewall02.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7021,7022,7023,7024,7025,7026,7027,7028,7029,7030,7031,7032], visible=False, arg4=0, arg5=10) # 벽 해제


