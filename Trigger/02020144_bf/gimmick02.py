""" trigger/02020144_bf/gimmick02.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Plant', value=1):
            return 몬스터소환(self.ctx)
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304], animationEffect=False) # 21430006 네펜투스

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 힌트(self.ctx)


class 힌트(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=4000):
            return 알림(self.ctx)


class 알림(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=25000):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[301,302,303,304]):
            self.set_user_value(triggerId=900004, key='Plant', value=0)
            return 대기(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[301,302,303,304], arg2=False)
        self.set_user_value(triggerId=900004, key='Plant', value=0)
        # <action name="SetUserValue" triggerID="900009" key="Seed" value="0" />

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
