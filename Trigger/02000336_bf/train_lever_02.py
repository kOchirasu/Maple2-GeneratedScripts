""" trigger/02000336_bf/train_lever_02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8211,8212,8213,8214], visible=False) # 안보이는 상태
        set_interact_object(triggerIds=[10000897], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000897], arg2=0):
            return 작동_01()


class 작동_01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8211,8212,8213,8214], visible=True, arg4=300, arg5=10) # 빨간 선이
        set_mesh(triggerIds=[8201,8202,8203,8204], visible=False, arg4=300, arg5=10) # 파란 선으로
        set_effect(triggerIds=[7011], visible=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 작동_02()


class 작동_02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8021,8022,8023,8024], visible=False, arg4=0, arg5=10) # 벽은 사라지고
        set_skill(triggerIds=[5807], isEnable=True) # 벽 날리는 스킬
        set_mesh(triggerIds=[8205], visible=False, arg4=30, arg5=0) # 드럼통 폭발
        set_mesh(triggerIds=[8211,8212,8213,8214], visible=False, arg4=0, arg5=10) # 파란 선도 마저 삭제


