""" trigger/02000037_bf/trigger_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=True, arg3=0, delay=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[2000]):
            return 발판(self.ctx)
        if self.monster_in_combat(boxIds=[2001]):
            return 발판(self.ctx)


class 발판(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=False, arg3=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2500):
            return 포털등장(self.ctx)


class 포털등장(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000,2001]):
            return 발록죽음(self.ctx)


class 발록죽음(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], visible=True, arg3=0, delay=200)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
