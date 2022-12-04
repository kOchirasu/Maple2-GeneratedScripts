""" trigger/02100004_bf/randomspawner.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RoundStart', value=1):
            return 랜덤스폰(self.ctx)


class 랜덤스폰(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999992, key='RoundStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=10):
            return 중복체크01(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크02(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크03(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크04(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크05(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크06(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크08(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크09(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크10(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크11(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크12(self.ctx)
        if self.random_condition(rate=10):
            return 중복체크13(self.ctx)


class 중복체크01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned01', value=0):
            self.set_user_value(triggerId=999101, key='NpcSpawn01', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned01', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned02', value=0):
            self.set_user_value(triggerId=999102, key='NpcSpawn02', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned02', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned03', value=0):
            self.set_user_value(triggerId=999103, key='NpcSpawn03', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned03', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned04', value=0):
            self.set_user_value(triggerId=999104, key='NpcSpawn04', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned04', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크05(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned05', value=0):
            self.set_user_value(triggerId=999105, key='NpcSpawn05', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned05', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크06(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned06', value=0):
            self.set_user_value(triggerId=999106, key='NpcSpawn06', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned06', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크08(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned08', value=0):
            self.set_user_value(triggerId=999108, key='NpcSpawn08', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned08', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크09(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned09', value=0):
            self.set_user_value(triggerId=999109, key='NpcSpawn09', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned09', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned10', value=0):
            self.set_user_value(triggerId=999110, key='NpcSpawn10', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned10', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned11', value=0):
            self.set_user_value(triggerId=999111, key='NpcSpawn11', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned11', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned12', value=0):
            self.set_user_value(triggerId=999112, key='NpcSpawn12', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned12', value=1):
            return 랜덤스폰(self.ctx)


class 중복체크13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawned13', value=0):
            self.set_user_value(triggerId=999113, key='NpcSpawn13', value=1)
            return 대기(self.ctx)
        if self.user_value(key='NpcSpawned13', value=1):
            return 랜덤스폰(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작
