""" trigger/02000331_bf/spring02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)
        set_skill(triggerIds=[7004], isEnable=False)
        set_skill(triggerIds=[7005], isEnable=False)
        set_skill(triggerIds=[7006], isEnable=False)
        set_skill(triggerIds=[7007], isEnable=False)
        set_skill(triggerIds=[7008], isEnable=False)
        set_skill(triggerIds=[7009], isEnable=False)
        set_skill(triggerIds=[7010], isEnable=False)
        set_skill(triggerIds=[7011], isEnable=False)
        set_skill(triggerIds=[7012], isEnable=False)
        set_skill(triggerIds=[7013], isEnable=False)
        set_skill(triggerIds=[7014], isEnable=False)
        set_skill(triggerIds=[7015], isEnable=False)
        set_skill(triggerIds=[7016], isEnable=False)
        set_skill(triggerIds=[7017], isEnable=False)
        set_skill(triggerIds=[7018], isEnable=False)
        set_skill(triggerIds=[7019], isEnable=False)
        set_skill(triggerIds=[7020], isEnable=False)
        set_skill(triggerIds=[7021], isEnable=False)
        set_skill(triggerIds=[7022], isEnable=False)
        set_skill(triggerIds=[7023], isEnable=False)
        set_skill(triggerIds=[7024], isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99991]):
            return 스킬발동()


class 스킬발동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=True)
        set_skill(triggerIds=[7002], isEnable=True)
        set_skill(triggerIds=[7003], isEnable=True)
        set_skill(triggerIds=[7004], isEnable=True)
        set_skill(triggerIds=[7005], isEnable=True)
        set_skill(triggerIds=[7006], isEnable=True)
        set_skill(triggerIds=[7007], isEnable=True)
        set_skill(triggerIds=[7008], isEnable=True)
        set_skill(triggerIds=[7009], isEnable=True)
        set_skill(triggerIds=[7010], isEnable=True)
        set_skill(triggerIds=[7011], isEnable=True)
        set_skill(triggerIds=[7012], isEnable=True)
        set_skill(triggerIds=[7013], isEnable=True)
        set_skill(triggerIds=[7014], isEnable=True)
        set_skill(triggerIds=[7015], isEnable=True)
        set_skill(triggerIds=[7016], isEnable=True)
        set_skill(triggerIds=[7017], isEnable=True)
        set_skill(triggerIds=[7018], isEnable=True)
        set_skill(triggerIds=[7019], isEnable=True)
        set_skill(triggerIds=[7020], isEnable=True)
        set_skill(triggerIds=[7021], isEnable=True)
        set_skill(triggerIds=[7022], isEnable=True)
        set_skill(triggerIds=[7023], isEnable=True)
        set_skill(triggerIds=[7024], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 대기()


