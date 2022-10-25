""" trigger/65000002_bd/bush_05.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=1001005, skillId=70000075)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=1001005, boxId=1, operator='Equal'):
            return 버프발동(self.ctx)


class 버프발동(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1001005], skillId=70000075, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 버프발동(self.ctx)
        if self.count_users(boxId=1001005, boxId=1, operator='Greater'):
            return 대기(self.ctx)
        if not self.user_detected(boxIds=[1001005]):
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
