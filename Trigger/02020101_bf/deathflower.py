""" trigger/02020101_bf/deathflower.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='flower', value=1):
            return 랜덤대상선정(self.ctx)


class 랜덤대상선정(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.random_additional_effect(target='pc', boxId=1003, spawnId=0, targetCount=1, tick=3, waitTick=2, targetEffect='Additional/Etc/Eff_Target_Select_Keep.xml', additionalEffectId=62100021)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            self.set_user_value(triggerId=900007, key='flower', value=0)
            return 종료(self.ctx)
        if self.wait_tick(waitTick=2000):
            self.set_user_value(triggerId=900007, key='flower', value=0)
            return 변수초기화(self.ctx)


class 변수초기화(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='flower', value=0):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=1004, skillId=62100021, isPlayer=True)
        self.remove_buff(boxId=1004, skillId=62100022, isPlayer=True)
        self.remove_buff(boxId=1004, skillId=62100023, isPlayer=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
