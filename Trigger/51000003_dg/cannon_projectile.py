""" trigger/51000003_dg/cannon_projectile.xml """
import trigger_api


# 플레이어 감지
# 큐브스킬형 캐논 발사체
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111,112,113,114,115,116,117,118])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01', value=1):
            return Round_01(self.ctx)
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Round_03', value=1):
            return Round_03(self.ctx)
        if self.user_value(key='Round_04', value=1):
            return Round_04(self.ctx)
        if self.user_value(key='Round_05', value=1):
            return Round_05(self.ctx)
        if self.user_value(key='Round_06', value=1):
            return Round_06(self.ctx)


class Round_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[113], animationEffect=True, animationDelay=600)
        self.create_monster(spawnIds=[118], animationEffect=True, animationDelay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[114], animationEffect=True, animationDelay=700)
        self.create_monster(spawnIds=[117], animationEffect=True, animationDelay=1100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03', value=1):
            return Round_03(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[112], animationEffect=True, animationDelay=800)
        self.create_monster(spawnIds=[116], animationEffect=True, animationDelay=1300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04', value=1):
            return Round_04(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111], animationEffect=True, animationDelay=300)
        self.create_monster(spawnIds=[115], animationEffect=True, animationDelay=900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_05', value=1):
            return Round_05(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[111,112,113,114,115,116,117,118])
        self.create_monster(spawnIds=[101], animationEffect=True, animationDelay=1000)
        self.create_monster(spawnIds=[102], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[103], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[104], animationEffect=True, animationDelay=4000)
        self.create_monster(spawnIds=[105], animationEffect=True, animationDelay=5000)
        self.create_monster(spawnIds=[106], animationEffect=True, animationDelay=6000)
        self.create_monster(spawnIds=[107], animationEffect=True, animationDelay=7000)
        self.create_monster(spawnIds=[108], animationEffect=True, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_06', value=1):
            return Round_check(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[121], animationEffect=True, animationDelay=1000)
        self.create_monster(spawnIds=[122], animationEffect=True, animationDelay=3000)
        self.create_monster(spawnIds=[123], animationEffect=True, animationDelay=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return None # Missing State: Round_06_02
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='cannon_projectile 종료', arg3='1000')
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118])


initial_state = Round_check
