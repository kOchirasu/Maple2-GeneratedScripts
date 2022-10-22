""" trigger/02010052_bf/xray_01.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20400,20401,20402,20403,20404,20405,20406,20407,20408,20409,20410,20411,20412,20413,20414,20415,20416,20417,20418,20419,20420,20421,20422,20423,20424,20425,20426,20427,20428,20429,20430], visible=True, arg3=0, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if count_users(boxId=706, boxId=1):
            return xray()


class xray(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[20400,20401,20402,20403,20404,20405,20406,20407,20408,20409,20410,20411,20412,20413,20414,20415,20416,20417,20418,20419,20420,20421,20422,20423,20424,20425,20426,20427,20428,20429,20430], visible=False, arg3=0, arg4=0, arg5=3) # 벽 해제

    def on_tick(self) -> state.State:
        if not count_users(boxId=706, boxId=1):
            return idle()


