""" trigger/65010003_bd/bush_03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=1001003, skillId=70000075)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=1001003, boxId=1, operator='Equal'):
            return 버프발동(self.ctx)


class 버프발동(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1001003], skillId=70000075, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 버프발동(self.ctx)
        if self.count_users(boxId=1001003, boxId=1, operator='Greater'):
            return 대기(self.ctx)
        if not self.user_detected(boxIds=[1001003]):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
