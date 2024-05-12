""" trigger/51000003_dg/normal_projectile.xml """
import trigger_api


# 플레이어 감지
# 직사형 일반발사체
class Round_check(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])

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
            return None # Missing State: Round_05
        if self.user_value(key='Round_06', value=1):
            return None # Missing State: Round_06


class Round_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[354], animationEffect=True, animationDelay=700)
        self.create_monster(spawnIds=[355], animationEffect=True, animationDelay=1400)
        self.create_monster(spawnIds=[362], animationEffect=True, animationDelay=2100)
        self.create_monster(spawnIds=[361], animationEffect=True, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_02', value=1):
            return Round_02(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[352], animationEffect=True, animationDelay=2000)
        self.create_monster(spawnIds=[360], animationEffect=True, animationDelay=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_03', value=1):
            return Round_03(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[359], animationEffect=True, animationDelay=0)
        self.create_monster(spawnIds=[351], animationEffect=True, animationDelay=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Round_04', value=1):
            return Round_04(self.ctx)
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class Round_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[353], animationEffect=True, animationDelay=1000)
        self.create_monster(spawnIds=[358], animationEffect=True, animationDelay=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Reset', value=1):
            return End(self.ctx)


class End(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=1, arg2='normal_projectile 종료', arg3='1000')
        self.destroy_monster(spawnIds=[301,302,303,304,305,306,307,308,309,310,311,312,351,352,353,354,355,356,357,358,359,360,361,362])


initial_state = Round_check
