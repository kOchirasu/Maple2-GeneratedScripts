""" trigger/99999841/badmob_message.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=901, value=1):
            return 쫄몹1(self.ctx)
        if self.dungeon_variable(varId=902, value=1):
            return 쫄몹2(self.ctx)
        if self.dungeon_variable(varId=903, value=1):
            return 쫄몹3(self.ctx)


class 쫄몹1(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='방해쫄몹1이 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=6000):
            return 대기(self.ctx)


class 쫄몹2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='방해쫄몹2가 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=6000):
            return 대기(self.ctx)


class 쫄몹3(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='방해쫄몹3이 생성되었습니다.\n모두 처치하기 전까지는 자원을 넣을 수 없습니다.', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.dungeon_variable(varId=2, value=1):
            return 종료(self.ctx)
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=6000):
            return 대기(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
