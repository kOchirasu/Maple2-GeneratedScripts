""" trigger/02020063_bf/object1.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[711], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_1', value=1):
            return 터렛_활성화(self.ctx)


class 터렛_활성화(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[711], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_1', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[711]):
            return 터렛_비활성화(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 터렛_비활성화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_1', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[711], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TurretSpawn_1', value=0):
            return 대기(self.ctx)


initial_state = 대기
