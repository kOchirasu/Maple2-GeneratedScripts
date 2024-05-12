""" trigger/02000331_bf/switch08.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7773], visible=False) # 발판 휠 내려옴 사운드
        self.set_breakable(triggerIds=[5001], enable=False)
        self.set_breakable(triggerIds=[5002], enable=False)
        self.set_breakable(triggerIds=[5011], enable=False)
        self.set_breakable(triggerIds=[5012], enable=False)
        self.set_breakable(triggerIds=[5021], enable=False)
        self.set_breakable(triggerIds=[5022], enable=False)
        self.set_breakable(triggerIds=[5031], enable=False)
        self.set_breakable(triggerIds=[5032], enable=False)
        self.set_mesh(triggerIds=[40000,40001], visible=False, arg3=0, delay=0, scale=0) # TOK용 투명한 매쉬

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000794], stateValue=0):
            # 3rd 스위치04
            return 발판내리기(self.ctx)


class 발판내리기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[5001], enable=True)
        self.set_breakable(triggerIds=[5002], enable=True)
        self.set_breakable(triggerIds=[5011], enable=True)
        self.set_breakable(triggerIds=[5012], enable=True)
        self.set_breakable(triggerIds=[5021], enable=True)
        self.set_breakable(triggerIds=[5022], enable=True)
        self.set_breakable(triggerIds=[5031], enable=True)
        self.set_breakable(triggerIds=[5032], enable=True)
        self.set_effect(triggerIds=[7773], visible=True) # 발판 내려올 때 휠 사운드
        self.set_mesh(triggerIds=[40000,40001], visible=True, arg3=0, delay=0, scale=0) # TOK용 투명한 매쉬

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=16000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_breakable(triggerIds=[5001], enable=False)
        self.set_breakable(triggerIds=[5002], enable=False)
        self.set_breakable(triggerIds=[5011], enable=False)
        self.set_breakable(triggerIds=[5012], enable=False)
        self.set_breakable(triggerIds=[5021], enable=False)
        self.set_breakable(triggerIds=[5022], enable=False)
        self.set_breakable(triggerIds=[5031], enable=False)
        self.set_breakable(triggerIds=[5032], enable=False)
        self.set_effect(triggerIds=[7773], visible=False) # 발판 휠 내려옴 사운드
        self.set_mesh(triggerIds=[40000,40001], visible=False, arg3=0, delay=0, scale=0) # TOK용 투명한 매쉬


initial_state = 대기
