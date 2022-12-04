""" trigger/99999840/debuffactive.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=811, value=1):
            return 이동속도감소(self.ctx)
        if self.dungeon_variable(varId=812, value=1):
            return 공격력감소(self.ctx)
        if self.dungeon_variable(varId=813, value=1):
            return 체력감소(self.ctx)


class 이동속도감소(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=811, value=0)
        self.set_event_ui(type=1, arg2='이동속도 감소 디버프에 걸립니다.', arg3='5000')
        self.add_buff(boxIds=[9001], skillId=70002581, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


class 공격력감소(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=812, value=0)
        self.set_event_ui(type=1, arg2='공격력 감소 디버프에 걸립니다.', arg3='5000')
        self.add_buff(boxIds=[9001], skillId=70002591, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


class 체력감소(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=813, value=0)
        self.set_event_ui(type=1, arg2='체력 감소 디버프에 걸립니다.', arg3='5000')
        self.add_buff(boxIds=[9001], skillId=70002601, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 대기(self.ctx)


initial_state = 대기
