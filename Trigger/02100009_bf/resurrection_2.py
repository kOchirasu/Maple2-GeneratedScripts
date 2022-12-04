""" trigger/02100009_bf/resurrection_2.xml """
import trigger_api


class 유저감지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[100000002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[100000002]):
            return 버프(self.ctx)


class 버프(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[100000002], skillId=50000198, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[100000002], skillId=50000202, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 체력조건달성(self.ctx)


class 체력조건달성(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 몬스터기절_2(self.ctx)

    def on_exit(self):
        self.add_buff(boxIds=[100000002], skillId=50000229, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[100000002], skillId=50000207, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[100000002], skillId=50000216, level=1, isPlayer=True, isSkillSet=False)


class 몬스터기절_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9900, type='trigger', achieve='02100009_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6800):
            return 몬스터부활(self.ctx)


class 몬스터부활(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[100000002], skillId=50000204, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[100000002], skillId=50000198, level=1, isPlayer=True, isSkillSet=False)
        self.add_buff(boxIds=[100000002], skillId=50000202, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 체력조건미달(self.ctx)


class 체력조건미달(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 몬스터부활_2(self.ctx)

    def on_exit(self):
        self.add_buff(boxIds=[100000002], skillId=50000228, level=1, isPlayer=True, isSkillSet=False)


class 몬스터부활_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='MonsterDown2', value=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 체력조건달성(self.ctx)


initial_state = 유저감지
