""" trigger/02010052_bf/invisiblewall02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230], visible=True, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if count_users(boxId=711, boxId=1):
            return 벽면처리()


class 벽면처리(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230], visible=False, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if not count_users(boxId=711, boxId=1):
            return 시작()


