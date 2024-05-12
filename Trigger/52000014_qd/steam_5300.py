""" trigger/52000014_qd/steam_5300.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 딜레이01(self.ctx)


class 딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 발사01(self.ctx)


class 발사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.spawn_monster(spawn_ids=[530], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 발사02(self.ctx)


class 발사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)
        self.spawn_monster(spawn_ids=[531], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 딜레이02(self.ctx)


class 딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=1)
        self.destroy_monster(spawn_ids=[530])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 발사03(self.ctx)


class 발사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=2)
        self.spawn_monster(spawn_ids=[531], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[531])

    def on_tick(self) -> trigger_api.Trigger:
        return 딜레이01(self.ctx)


initial_state = 대기
