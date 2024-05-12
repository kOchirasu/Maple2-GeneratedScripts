""" trigger/02000245_bf/trigger_03_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[801], visible=True, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7001], enable=True)
        self.set_skill(triggerIds=[7002], enable=True)
        self.set_skill(triggerIds=[7003], enable=True)
        self.set_skill(triggerIds=[7004], enable=True)
        self.set_skill(triggerIds=[7005], enable=True)
        self.set_skill(triggerIds=[7006], enable=True)
        self.set_skill(triggerIds=[7007], enable=True)
        self.set_skill(triggerIds=[7008], enable=True)
        self.set_skill(triggerIds=[7009], enable=True)
        self.set_skill(triggerIds=[7010], enable=True)
        self.set_skill(triggerIds=[7011], enable=True)
        self.set_skill(triggerIds=[7012], enable=True)
        self.set_skill(triggerIds=[7013], enable=True)
        self.set_skill(triggerIds=[7014], enable=True)
        self.set_skill(triggerIds=[7015], enable=True)
        self.set_skill(triggerIds=[7016], enable=True)
        self.set_skill(triggerIds=[7017], enable=True)
        self.set_skill(triggerIds=[7018], enable=True)
        self.set_skill(triggerIds=[7019], enable=True)
        self.set_skill(triggerIds=[7020], enable=True)
        self.set_effect(triggerIds=[901], visible=True)
        self.set_effect(triggerIds=[902], visible=True)
        self.set_effect(triggerIds=[903], visible=True)
        self.set_effect(triggerIds=[904], visible=True)
        self.set_effect(triggerIds=[905], visible=True)
        self.set_effect(triggerIds=[906], visible=True)
        self.set_effect(triggerIds=[907], visible=True)
        self.set_effect(triggerIds=[908], visible=True)
        self.set_effect(triggerIds=[909], visible=True)
        self.set_effect(triggerIds=[910], visible=True)
        self.set_effect(triggerIds=[911], visible=True)
        self.set_effect(triggerIds=[912], visible=True)
        self.set_effect(triggerIds=[913], visible=True)
        self.set_effect(triggerIds=[914], visible=True)
        self.set_effect(triggerIds=[915], visible=True)
        self.set_effect(triggerIds=[916], visible=True)
        self.set_effect(triggerIds=[917], visible=True)
        self.set_effect(triggerIds=[918], visible=True)
        self.set_effect(triggerIds=[919], visible=True)
        self.set_effect(triggerIds=[920], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[207]):
            return 단계1(self.ctx)


class 단계1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[801], visible=False, arg3=0, delay=0, scale=0)
        self.set_skill(triggerIds=[7001], enable=False)
        self.set_skill(triggerIds=[7002], enable=False)
        self.set_skill(triggerIds=[7003], enable=False)
        self.set_skill(triggerIds=[7004], enable=False)
        self.set_skill(triggerIds=[7005], enable=False)
        self.set_skill(triggerIds=[7006], enable=False)
        self.set_skill(triggerIds=[7007], enable=False)
        self.set_skill(triggerIds=[7008], enable=False)
        self.set_skill(triggerIds=[7009], enable=False)
        self.set_skill(triggerIds=[7010], enable=False)
        self.set_skill(triggerIds=[7011], enable=False)
        self.set_skill(triggerIds=[7012], enable=False)
        self.set_skill(triggerIds=[7013], enable=False)
        self.set_skill(triggerIds=[7014], enable=False)
        self.set_skill(triggerIds=[7015], enable=False)
        self.set_skill(triggerIds=[7016], enable=False)
        self.set_skill(triggerIds=[7017], enable=False)
        self.set_skill(triggerIds=[7018], enable=False)
        self.set_skill(triggerIds=[7019], enable=False)
        self.set_skill(triggerIds=[7020], enable=False)
        self.set_effect(triggerIds=[901], visible=False)
        self.set_effect(triggerIds=[902], visible=False)
        self.set_effect(triggerIds=[903], visible=False)
        self.set_effect(triggerIds=[904], visible=False)
        self.set_effect(triggerIds=[905], visible=False)
        self.set_effect(triggerIds=[906], visible=False)
        self.set_effect(triggerIds=[907], visible=False)
        self.set_effect(triggerIds=[908], visible=False)
        self.set_effect(triggerIds=[909], visible=False)
        self.set_effect(triggerIds=[910], visible=False)
        self.set_effect(triggerIds=[911], visible=False)
        self.set_effect(triggerIds=[912], visible=False)
        self.set_effect(triggerIds=[913], visible=False)
        self.set_effect(triggerIds=[914], visible=False)
        self.set_effect(triggerIds=[915], visible=False)
        self.set_effect(triggerIds=[916], visible=False)
        self.set_effect(triggerIds=[917], visible=False)
        self.set_effect(triggerIds=[918], visible=False)
        self.set_effect(triggerIds=[919], visible=False)
        self.set_effect(triggerIds=[920], visible=False)


initial_state = 대기
