""" trigger/63000038_cs/move.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enabled=False)
        set_interact_object(triggerIds=[10001024], state=0)

    def on_tick(self) -> state.State:
        if user_value(key='Setlever', value=1):
            return 레버반응대기()


class 레버반응대기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=26300382, textId=26300382)
        set_interact_object(triggerIds=[10001024], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001024], arg2=0):
            hide_guide_summary(entityId=26300382)
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enabled=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료()


class 종료(state.State):
    pass


