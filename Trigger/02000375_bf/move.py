""" trigger/02000375_bf/move.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], arg2=True)
        set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enabled=False)
        set_interact_object(triggerIds=[10001024], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001024], arg2=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enabled=True)
        set_event_ui(type=1, arg2='$02000375_BF__move__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=60000):
            return 레버삭제()


class 레버삭제(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], arg2=False)
        set_breakable(triggerIds=[7000,7001,7002,7003,7004,7005,7006,7007,7008,7009,7010,7011,7012,7013,7014,7015,7016,7017,7018,7019,7020,7021,7022,7023], enabled=False)
        set_interact_object(triggerIds=[10001024], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='BattleEnd', value=1):
            return 대기()


class 종료(state.State):
    pass


