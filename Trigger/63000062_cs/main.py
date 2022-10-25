""" trigger/63000062_cs/main.xml """
import common


class 날짜체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 만남(self.ctx)
        if self.day_of_week(dayOfWeeks=[1,2,3,5,6,7], desc='1(일)-7(토)'):
            return 헤어짐(self.ctx)


class 만남(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111,112])
        self.create_monster(spawnIds=[121,122], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.day_of_week(dayOfWeeks=[1,2,3,5,6,7], desc='1(일)-7(토)'):
            return 헤어짐(self.ctx)


class 헤어짐(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[121,122])
        self.create_monster(spawnIds=[111,112], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.day_of_week(dayOfWeeks=[4], desc='1(일)-7(토)'):
            return 만남(self.ctx)


initial_state = 날짜체크
