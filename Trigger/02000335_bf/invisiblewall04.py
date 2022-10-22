""" trigger/02000335_bf/invisiblewall04.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=706, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7051,7052,7053,7054,7055,7056,7057,7058,7059,7060], visible=False, arg4=0, arg5=10) # 벽 해제


