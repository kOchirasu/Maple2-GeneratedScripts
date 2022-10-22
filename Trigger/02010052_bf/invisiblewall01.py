""" trigger/02010052_bf/invisiblewall01.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112], visible=True, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if count_users(boxId=710, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112], visible=False, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if not count_users(boxId=710, boxId=1):
            return 시작()


