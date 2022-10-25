""" trigger/02020065_bf/battle3_object2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[812], arg2=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Battle3_TurretSpawn_2', value=1):
            return 터렛_활성화(self.ctx)


class 터렛_활성화(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[812], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Battle3_TurretSpawn_2', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[812]):
            return 터렛_비활성화(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 터렛_비활성화(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Battle3_TurretSpawn_2', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[801]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[812], arg2=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Battle3_TurretSpawn_2', value=1):
            return 대기(self.ctx)


initial_state = 대기
