""" trigger/99999911/main.xml """
import trigger_api


# 플레이어 감지
class 최초(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=701, min_users='1'):
            return 시작조건체크(self.ctx)


class 시작조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=10000):
            return 어나운스0(self.ctx)
        if self.count_users(box_id=701, min_users='20'):
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$99999911__MAIN__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', stage=0, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            self.set_mesh(trigger_ids=[301,302,303], visible=False, start_delay=12, interval=0)
            self.set_achievement(trigger_id=101, type='trigger', achieve='dailyquest_start')
            return idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[101], auto_target=True, delay=1)
        self.spawn_monster(spawn_ids=[102], auto_target=True, delay=2)
        self.spawn_monster(spawn_ids=[103], auto_target=True, delay=3)
        self.spawn_monster(spawn_ids=[104], auto_target=True, delay=4)
        self.spawn_monster(spawn_ids=[105], auto_target=True, delay=5)
        self.spawn_monster(spawn_ids=[106], auto_target=True, delay=6)
        self.spawn_monster(spawn_ids=[107], auto_target=True, delay=7)
        self.spawn_monster(spawn_ids=[108], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[301], auto_target=True, delay=1)
        self.spawn_monster(spawn_ids=[302], auto_target=True, delay=2)
        self.spawn_monster(spawn_ids=[303], auto_target=True, delay=3)
        self.spawn_monster(spawn_ids=[304], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[305], auto_target=True, delay=1)
        self.spawn_monster(spawn_ids=[306], auto_target=True, delay=2)
        self.spawn_monster(spawn_ids=[307], auto_target=True, delay=3)
        self.spawn_monster(spawn_ids=[308], auto_target=True, delay=0)
        self.spawn_monster(spawn_ids=[309], auto_target=True, delay=1)
        self.spawn_monster(spawn_ids=[310], auto_target=True, delay=2)
        self.spawn_monster(spawn_ids=[311], auto_target=True, delay=3)
        self.spawn_monster(spawn_ids=[312], auto_target=True, delay=0)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return Round1_Start(self.ctx)


class Round1_Start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(trigger_id=991104, key='Round_02', value=1)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return None # Missing State: random_start


initial_state = 최초
