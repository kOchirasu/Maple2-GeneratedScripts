""" trigger/02020063_bf/object5.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[715], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_5', value=1):
            return 터렛_활성화(self.ctx)


class 터렛_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[715], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_5', value=0):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[715]):
            return 터렛_비활성화(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            return 종료(self.ctx)


class 터렛_비활성화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_5', value=0):
            return 대기(self.ctx)
        if self.monster_dead(spawn_ids=[801]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[715], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_5', value=1):
            return 대기(self.ctx)


initial_state = 대기
