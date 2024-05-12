""" trigger/51000003_dg/cannon_projectile.xml """
import trigger_api


"""
플레이어 감지
큐브스킬형 캐논 발사체
"""
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112,113,114,115,116,117,118])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_01') >= 1:
            return Round_01(self.ctx)
        if self.user_value(key='Round_02') >= 1:
            return Round_02(self.ctx)
        if self.user_value(key='Round_03') >= 1:
            return Round_03(self.ctx)
        if self.user_value(key='Round_04') >= 1:
            return Round_04(self.ctx)
        if self.user_value(key='Round_05') >= 1:
            return Round_05(self.ctx)
        if self.user_value(key='Round_06') >= 1:
            return Round_06(self.ctx)


class Round_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[113], auto_target=True, delay=600)
        self.spawn_monster(spawn_ids=[118], auto_target=True, delay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02') >= 1:
            return Round_02(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[114], auto_target=True, delay=700)
        self.spawn_monster(spawn_ids=[117], auto_target=True, delay=1100)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03') >= 1:
            return Round_03(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[112], auto_target=True, delay=800)
        self.spawn_monster(spawn_ids=[116], auto_target=True, delay=1300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04') >= 1:
            return Round_04(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[111], auto_target=True, delay=300)
        self.spawn_monster(spawn_ids=[115], auto_target=True, delay=900)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_05') >= 1:
            return Round_05(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[111,112,113,114,115,116,117,118])
        self.spawn_monster(spawn_ids=[101], auto_target=True, delay=1000)
        self.spawn_monster(spawn_ids=[102], auto_target=True, delay=2000)
        self.spawn_monster(spawn_ids=[103], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[104], auto_target=True, delay=4000)
        self.spawn_monster(spawn_ids=[105], auto_target=True, delay=5000)
        self.spawn_monster(spawn_ids=[106], auto_target=True, delay=6000)
        self.spawn_monster(spawn_ids=[107], auto_target=True, delay=7000)
        self.spawn_monster(spawn_ids=[108], auto_target=True, delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_06') >= 1:
            return Round_check(self.ctx)
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class Round_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[121], auto_target=True, delay=1000)
        self.spawn_monster(spawn_ids=[122], auto_target=True, delay=3000)
        self.spawn_monster(spawn_ids=[123], auto_target=True, delay=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return None # Missing State: Round_06_02
        if self.user_value(key='Reset') >= 1:
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='cannon_projectile 종료', arg3='1000')
        self.destroy_monster(spawn_ids=[101,102,103,104,105,106,107,108,111,112,113,114,115,116,117,118])


initial_state = Round_check
