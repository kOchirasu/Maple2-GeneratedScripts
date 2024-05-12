""" trigger/52000014_qd/meteo_7800.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7800,7801,7802,7803,7804,7805,7806,7807,7808,7809], visible=False, start_delay=0, interval=0, fade=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 시작딜레이01(self.ctx)


class 시작딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='201', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='201'):
            return 랜덤생성01(self.ctx)


class 랜덤생성01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25):
            return 패턴01생성01(self.ctx)
        if self.random_condition(weight=25):
            return 패턴02생성01(self.ctx)
        if self.random_condition(weight=25):
            return 패턴03생성01(self.ctx)
        if self.random_condition(weight=25):
            return 패턴04생성01(self.ctx)


# 패턴01
class 패턴01생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_mesh(trigger_ids=[7801], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 패턴01낙하01(self.ctx)


class 패턴01낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.set_mesh(trigger_ids=[7801], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 패턴01생성02(self.ctx)


class 패턴01생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=1)
        self.set_mesh(trigger_ids=[7805], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 패턴01낙하02(self.ctx)


class 패턴01낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=1)
        self.set_mesh(trigger_ids=[7805], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 패턴01생성03(self.ctx)


class 패턴01생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=1)
        self.set_mesh(trigger_ids=[7807], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 패턴01낙하03(self.ctx)


class 패턴01낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='6', seconds=1)
        self.set_mesh(trigger_ids=[7807], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='6'):
            return 딜레이랜덤01(self.ctx)


# 패턴02
class 패턴02생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=1)
        self.set_mesh(trigger_ids=[7808], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 패턴02낙하01(self.ctx)


class 패턴02낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=1)
        self.set_mesh(trigger_ids=[7808], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 패턴02생성02(self.ctx)


class 패턴02생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=1)
        self.set_mesh(trigger_ids=[7804], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 패턴02낙하02(self.ctx)


class 패턴02낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=1)
        self.set_mesh(trigger_ids=[7804], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 패턴02생성03(self.ctx)


class 패턴02생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='15', seconds=1)
        self.set_mesh(trigger_ids=[7802], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='15'):
            return 패턴02낙하03(self.ctx)


class 패턴02낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='16', seconds=1)
        self.set_mesh(trigger_ids=[7802], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='16'):
            return 딜레이랜덤01(self.ctx)


# 패턴03
class 패턴03생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=1)
        self.set_mesh(trigger_ids=[7809], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return 패턴03낙하01(self.ctx)


class 패턴03낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=1)
        self.set_mesh(trigger_ids=[7809], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return 패턴03생성02(self.ctx)


class 패턴03생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='23', seconds=1)
        self.set_mesh(trigger_ids=[7803], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='23'):
            return 패턴03낙하02(self.ctx)


class 패턴03낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='24', seconds=1)
        self.set_mesh(trigger_ids=[7803], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='24'):
            return 패턴03생성03(self.ctx)


class 패턴03생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=1)
        self.set_mesh(trigger_ids=[7804], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return 패턴03낙하03(self.ctx)


class 패턴03낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=1)
        self.set_mesh(trigger_ids=[7804], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return 패턴03생성04(self.ctx)


class 패턴03생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=1)
        self.set_mesh(trigger_ids=[7806], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='27'):
            return 패턴03낙하04(self.ctx)


class 패턴03낙하04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='28', seconds=1)
        self.set_mesh(trigger_ids=[7806], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='28'):
            return 딜레이랜덤01(self.ctx)


# 패턴04
class 패턴04생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=1)
        self.set_mesh(trigger_ids=[7802], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 패턴04낙하01(self.ctx)


class 패턴04낙하01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=1)
        self.set_mesh(trigger_ids=[7802], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='32'):
            return 패턴04생성02(self.ctx)


class 패턴04생성02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='33', seconds=1)
        self.set_mesh(trigger_ids=[7807], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='33'):
            return 패턴04낙하02(self.ctx)


class 패턴04낙하02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='34', seconds=1)
        self.set_mesh(trigger_ids=[7807], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='34'):
            return 패턴04생성03(self.ctx)


class 패턴04생성03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=1)
        self.set_mesh(trigger_ids=[7803], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 패턴04낙하03(self.ctx)


class 패턴04낙하03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='36', seconds=1)
        self.set_mesh(trigger_ids=[7803], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='36'):
            return 패턴04생성04(self.ctx)


class 패턴04생성04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='37', seconds=1)
        self.set_mesh(trigger_ids=[7808], visible=True, start_delay=0, interval=0, fade=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='37'):
            return 패턴04낙하04(self.ctx)


class 패턴04낙하04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='38', seconds=1)
        self.set_mesh(trigger_ids=[7808], visible=False, start_delay=0, interval=0, fade=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='38'):
            return 딜레이랜덤01(self.ctx)


class 딜레이랜덤01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=25):
            return 딜레이01(self.ctx)
        if self.random_condition(weight=25):
            return 딜레이02(self.ctx)
        if self.random_condition(weight=25):
            return 딜레이03(self.ctx)
        if self.random_condition(weight=25):
            return 딜레이04(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return 초기화(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='101', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='101'):
            return 초기화(self.ctx)


class 딜레이03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='102', seconds=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='102'):
            return 초기화(self.ctx)


class 딜레이04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='103', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='103'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='200', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='200'):
            return 랜덤생성01(self.ctx)


initial_state = 대기
