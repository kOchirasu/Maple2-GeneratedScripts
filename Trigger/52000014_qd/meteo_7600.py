""" trigger/52000014_qd/meteo_7600.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[7600,7601,7602,7603,7604,7605,7606,7607,7608,7609], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 랜덤생성01()


class 랜덤생성01(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 패턴01생성01()
        if random_condition(rate=25):
            return 패턴02생성01()
        if random_condition(rate=25):
            return 패턴03생성01()
        if random_condition(rate=25):
            return 패턴04생성01()


#   패턴01 
class 패턴01생성01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_mesh(triggerIds=[7600], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 패턴01낙하01()


class 패턴01낙하01(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=1)
        set_mesh(triggerIds=[7600], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 패턴01생성02()


class 패턴01생성02(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=1)
        set_mesh(triggerIds=[7602], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 패턴01낙하02()


class 패턴01낙하02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=1)
        set_mesh(triggerIds=[7602], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 패턴01생성03()


class 패턴01생성03(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1)
        set_mesh(triggerIds=[7607], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 패턴01낙하03()


class 패턴01낙하03(state.State):
    def on_enter(self):
        set_timer(timerId='6', seconds=1)
        set_mesh(triggerIds=[7607], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return 딜레이랜덤01()


#   패턴02 
class 패턴02생성01(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=1)
        set_mesh(triggerIds=[7602], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 패턴02낙하01()


class 패턴02낙하01(state.State):
    def on_enter(self):
        set_timer(timerId='12', seconds=1)
        set_mesh(triggerIds=[7602], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='12'):
            return 패턴02생성02()


class 패턴02생성02(state.State):
    def on_enter(self):
        set_timer(timerId='13', seconds=1)
        set_mesh(triggerIds=[7604], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='13'):
            return 패턴02낙하02()


class 패턴02낙하02(state.State):
    def on_enter(self):
        set_timer(timerId='14', seconds=1)
        set_mesh(triggerIds=[7604], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='14'):
            return 패턴02생성03()


class 패턴02생성03(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=1)
        set_mesh(triggerIds=[7608], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 패턴02낙하03()


class 패턴02낙하03(state.State):
    def on_enter(self):
        set_timer(timerId='16', seconds=1)
        set_mesh(triggerIds=[7608], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='16'):
            return 딜레이랜덤01()


#   패턴03 
class 패턴03생성01(state.State):
    def on_enter(self):
        set_timer(timerId='21', seconds=1)
        set_mesh(triggerIds=[7609], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='21'):
            return 패턴03낙하01()


class 패턴03낙하01(state.State):
    def on_enter(self):
        set_timer(timerId='22', seconds=1)
        set_mesh(triggerIds=[7609], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='22'):
            return 패턴03생성02()


class 패턴03생성02(state.State):
    def on_enter(self):
        set_timer(timerId='23', seconds=1)
        set_mesh(triggerIds=[7606], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='23'):
            return 패턴03낙하02()


class 패턴03낙하02(state.State):
    def on_enter(self):
        set_timer(timerId='24', seconds=1)
        set_mesh(triggerIds=[7606], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='24'):
            return 패턴03생성03()


class 패턴03생성03(state.State):
    def on_enter(self):
        set_timer(timerId='25', seconds=1)
        set_mesh(triggerIds=[7603], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='25'):
            return 패턴03낙하03()


class 패턴03낙하03(state.State):
    def on_enter(self):
        set_timer(timerId='26', seconds=1)
        set_mesh(triggerIds=[7603], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='26'):
            return 패턴03생성04()


class 패턴03생성04(state.State):
    def on_enter(self):
        set_timer(timerId='27', seconds=1)
        set_mesh(triggerIds=[7608], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='27'):
            return 패턴03낙하04()


class 패턴03낙하04(state.State):
    def on_enter(self):
        set_timer(timerId='28', seconds=1)
        set_mesh(triggerIds=[7608], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='28'):
            return 딜레이랜덤01()


#   패턴04 
class 패턴04생성01(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=1)
        set_mesh(triggerIds=[7601], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 패턴04낙하01()


class 패턴04낙하01(state.State):
    def on_enter(self):
        set_timer(timerId='32', seconds=1)
        set_mesh(triggerIds=[7601], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='32'):
            return 패턴04생성02()


class 패턴04생성02(state.State):
    def on_enter(self):
        set_timer(timerId='33', seconds=1)
        set_mesh(triggerIds=[7604], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='33'):
            return 패턴04낙하02()


class 패턴04낙하02(state.State):
    def on_enter(self):
        set_timer(timerId='34', seconds=1)
        set_mesh(triggerIds=[7604], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='34'):
            return 패턴04생성03()


class 패턴04생성03(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=1)
        set_mesh(triggerIds=[7608], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 패턴04낙하03()


class 패턴04낙하03(state.State):
    def on_enter(self):
        set_timer(timerId='36', seconds=1)
        set_mesh(triggerIds=[7608], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='36'):
            return 패턴04생성04()


class 패턴04생성04(state.State):
    def on_enter(self):
        set_timer(timerId='37', seconds=1)
        set_mesh(triggerIds=[7609], visible=True, arg3=0, arg4=0, arg5=1000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='37'):
            return 패턴04낙하04()


class 패턴04낙하04(state.State):
    def on_enter(self):
        set_timer(timerId='38', seconds=1)
        set_mesh(triggerIds=[7609], visible=False, arg3=0, arg4=0, arg5=500)

    def on_tick(self) -> state.State:
        if time_expired(timerId='38'):
            return 딜레이랜덤01()


class 딜레이랜덤01(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=25):
            return 딜레이01()
        if random_condition(rate=25):
            return 딜레이02()
        if random_condition(rate=25):
            return 딜레이03()
        if random_condition(rate=25):
            return 딜레이04()


class 딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='100', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100'):
            return 초기화()


class 딜레이02(state.State):
    def on_enter(self):
        set_timer(timerId='101', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='101'):
            return 초기화()


class 딜레이03(state.State):
    def on_enter(self):
        set_timer(timerId='102', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='102'):
            return 초기화()


class 딜레이04(state.State):
    def on_enter(self):
        set_timer(timerId='103', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='103'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_timer(timerId='200', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='200'):
            return 랜덤생성01()


