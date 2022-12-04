""" trigger/52000014_qd/meteo_7400.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[7400,7401,7402,7403,7404,7405,7406,7407,7408,7409], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 랜덤생성01(self.ctx)


class 랜덤생성01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 패턴01생성01(self.ctx)
        if self.random_condition(rate=25):
            return 패턴02생성01(self.ctx)
        if self.random_condition(rate=25):
            return 패턴03생성01(self.ctx)
        if self.random_condition(rate=25):
            return 패턴04생성01(self.ctx)


# 패턴01
class 패턴01생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_mesh(triggerIds=[7400], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 패턴01낙하01(self.ctx)


class 패턴01낙하01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=1)
        self.set_mesh(triggerIds=[7400], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 패턴01생성02(self.ctx)


class 패턴01생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=1)
        self.set_mesh(triggerIds=[7402], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 패턴01낙하02(self.ctx)


class 패턴01낙하02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=1)
        self.set_mesh(triggerIds=[7402], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 패턴01생성03(self.ctx)


class 패턴01생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=1)
        self.set_mesh(triggerIds=[7407], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 패턴01낙하03(self.ctx)


class 패턴01낙하03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='6', seconds=1)
        self.set_mesh(triggerIds=[7407], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='6'):
            return 딜레이랜덤01(self.ctx)


# 패턴02
class 패턴02생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='11', seconds=1)
        self.set_mesh(triggerIds=[7402], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 패턴02낙하01(self.ctx)


class 패턴02낙하01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='12', seconds=1)
        self.set_mesh(triggerIds=[7402], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='12'):
            return 패턴02생성02(self.ctx)


class 패턴02생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='13', seconds=1)
        self.set_mesh(triggerIds=[7405], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='13'):
            return 패턴02낙하02(self.ctx)


class 패턴02낙하02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='14', seconds=1)
        self.set_mesh(triggerIds=[7405], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='14'):
            return 패턴02생성03(self.ctx)


class 패턴02생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='15'):
            return 패턴02낙하03(self.ctx)


class 패턴02낙하03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='16', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='16'):
            return 딜레이랜덤01(self.ctx)


# 패턴03
class 패턴03생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='21', seconds=1)
        self.set_mesh(triggerIds=[7409], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='21'):
            return 패턴03낙하01(self.ctx)


class 패턴03낙하01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='22', seconds=1)
        self.set_mesh(triggerIds=[7409], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='22'):
            return 패턴03생성02(self.ctx)


class 패턴03생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='23', seconds=1)
        self.set_mesh(triggerIds=[7406], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='23'):
            return 패턴03낙하02(self.ctx)


class 패턴03낙하02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='24', seconds=1)
        self.set_mesh(triggerIds=[7406], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='24'):
            return 패턴03생성03(self.ctx)


class 패턴03생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='25', seconds=1)
        self.set_mesh(triggerIds=[7403], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='25'):
            return 패턴03낙하03(self.ctx)


class 패턴03낙하03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='26', seconds=1)
        self.set_mesh(triggerIds=[7403], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='26'):
            return 패턴03생성04(self.ctx)


class 패턴03생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='27', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='27'):
            return 패턴03낙하04(self.ctx)


class 패턴03낙하04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='28', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='28'):
            return 딜레이랜덤01(self.ctx)


# 패턴04
class 패턴04생성01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='31', seconds=1)
        self.set_mesh(triggerIds=[7401], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='31'):
            return 패턴04낙하01(self.ctx)


class 패턴04낙하01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='32', seconds=1)
        self.set_mesh(triggerIds=[7401], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='32'):
            return 패턴04생성02(self.ctx)


class 패턴04생성02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='33', seconds=1)
        self.set_mesh(triggerIds=[7404], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='33'):
            return 패턴04낙하02(self.ctx)


class 패턴04낙하02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='34', seconds=1)
        self.set_mesh(triggerIds=[7404], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='34'):
            return 패턴04생성03(self.ctx)


class 패턴04생성03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='35'):
            return 패턴04낙하03(self.ctx)


class 패턴04낙하03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='36', seconds=1)
        self.set_mesh(triggerIds=[7408], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='36'):
            return 패턴04생성04(self.ctx)


class 패턴04생성04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='37', seconds=1)
        self.set_mesh(triggerIds=[7409], visible=True, arg3=0, delay=0, scale=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='37'):
            return 패턴04낙하04(self.ctx)


class 패턴04낙하04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='38', seconds=1)
        self.set_mesh(triggerIds=[7409], visible=False, arg3=0, delay=0, scale=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='38'):
            return 딜레이랜덤01(self.ctx)


class 딜레이랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=25):
            return 딜레이01(self.ctx)
        if self.random_condition(rate=25):
            return 딜레이02(self.ctx)
        if self.random_condition(rate=25):
            return 딜레이03(self.ctx)
        if self.random_condition(rate=25):
            return 딜레이04(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='100', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100'):
            return 초기화(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='101', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='101'):
            return 초기화(self.ctx)


class 딜레이03(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='102', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='102'):
            return 초기화(self.ctx)


class 딜레이04(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='103', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='103'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='200', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='200'):
            return 랜덤생성01(self.ctx)


initial_state = 대기
