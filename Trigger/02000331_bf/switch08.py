""" trigger/02000331_bf/switch08.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7773], visible=False) # 발판 휠 내려옴 사운드
        set_breakable(triggerIds=[5001], enabled=False)
        set_breakable(triggerIds=[5002], enabled=False)
        set_breakable(triggerIds=[5011], enabled=False)
        set_breakable(triggerIds=[5012], enabled=False)
        set_breakable(triggerIds=[5021], enabled=False)
        set_breakable(triggerIds=[5022], enabled=False)
        set_breakable(triggerIds=[5031], enabled=False)
        set_breakable(triggerIds=[5032], enabled=False)
        set_mesh(triggerIds=[40000,40001], visible=False, arg3=0, arg4=0, arg5=0) # TOK용 투명한 매쉬

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000794], arg2=0):
            return 발판내리기()


class 발판내리기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[5001], enabled=True)
        set_breakable(triggerIds=[5002], enabled=True)
        set_breakable(triggerIds=[5011], enabled=True)
        set_breakable(triggerIds=[5012], enabled=True)
        set_breakable(triggerIds=[5021], enabled=True)
        set_breakable(triggerIds=[5022], enabled=True)
        set_breakable(triggerIds=[5031], enabled=True)
        set_breakable(triggerIds=[5032], enabled=True)
        set_effect(triggerIds=[7773], visible=True) # 발판 내려올 때 휠 사운드
        set_mesh(triggerIds=[40000,40001], visible=True, arg3=0, arg4=0, arg5=0) # TOK용 투명한 매쉬

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=16000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[5001], enabled=False)
        set_breakable(triggerIds=[5002], enabled=False)
        set_breakable(triggerIds=[5011], enabled=False)
        set_breakable(triggerIds=[5012], enabled=False)
        set_breakable(triggerIds=[5021], enabled=False)
        set_breakable(triggerIds=[5022], enabled=False)
        set_breakable(triggerIds=[5031], enabled=False)
        set_breakable(triggerIds=[5032], enabled=False)
        set_effect(triggerIds=[7773], visible=False) # 발판 휠 내려옴 사운드
        set_mesh(triggerIds=[40000,40001], visible=False, arg3=0, arg4=0, arg5=0) # TOK용 투명한 매쉬


