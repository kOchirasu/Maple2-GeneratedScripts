""" trigger/02000331_bf/spring02.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
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
        self.set_skill(triggerIds=[7021], enable=False)
        self.set_skill(triggerIds=[7022], enable=False)
        self.set_skill(triggerIds=[7023], enable=False)
        self.set_skill(triggerIds=[7024], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[99991]):
            return 스킬발동(self.ctx)


class 스킬발동(common.Trigger):
    def on_enter(self):
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
        self.set_skill(triggerIds=[7021], enable=True)
        self.set_skill(triggerIds=[7022], enable=True)
        self.set_skill(triggerIds=[7023], enable=True)
        self.set_skill(triggerIds=[7024], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대기(self.ctx)


initial_state = 대기
