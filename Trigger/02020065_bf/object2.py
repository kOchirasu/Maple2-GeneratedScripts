""" trigger/02020065_bf/object2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[712], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_2', value=1):
            return 터렛_활성화(self.ctx)


class 터렛_활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[712], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_2', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[712]):
            return 터렛_비활성화(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 터렛_비활성화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_2', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[712], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_2', value=1):
            return 대기(self.ctx)


initial_state = 대기
