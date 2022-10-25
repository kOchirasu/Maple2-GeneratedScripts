""" trigger/99999840/team1_box1.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=901, value=0)
        self.set_interact_object(triggerIds=[10002175], state=0, arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=911, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=912, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=913, value=1):
            return 종료(self.ctx)
        if self.user_value(key='Start', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002175], state=1, arg3=False)
        self.set_interact_object(triggerIds=[10002176], state=1, arg3=False)
        self.set_interact_object(triggerIds=[10002177], state=1, arg3=False)
        self.set_interact_object(triggerIds=[10002178], state=1, arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=911, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=912, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=913, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002175], stateValue=0):
            return 애디셔널_중첩1(self.ctx)


class 애디셔널_중첩1(common.Trigger):
    def on_enter(self):
        self.dungeon_variable(varId=901, value=1)
        self.add_buff(boxIds=[9001], skillId=70002511, level=1, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=911, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=912, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=913, value=1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=100):
            return 애디셔널_중첩2(self.ctx)


class 애디셔널_중첩2(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9001], skillId=70002511, level=1, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 애디셔널_중첩3(self.ctx)


class 애디셔널_중첩3(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9001], skillId=70002511, level=1, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 대기(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002175], state=0, arg3=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BadMob', value=1):
            return 대기(self.ctx)


initial_state = 대기
