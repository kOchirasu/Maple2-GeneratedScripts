""" trigger/02100000_bf/monster.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[80001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 유저감지(self.ctx)


class 유저감지(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=True)
        self.set_portal(portalId=19, visible=False, enable=False, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[102]):
            return 몬스터등장(self.ctx)


class 몬스터등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[80001], animationEffect=True)
        self.create_monster(spawnIds=[800011], animationEffect=True)
        self.create_monster(spawnIds=[81001], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[80002], animationEffect=True)
        self.create_monster(spawnIds=[800021], animationEffect=True)
        self.create_monster(spawnIds=[810021], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터사망_2(self.ctx)


class 몬스터사망_2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 몬스터등장_3(self.ctx)


class 몬스터등장_3(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[81001])
        self.destroy_monster(spawnIds=[81002])
        self.destroy_monster(spawnIds=[810021])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 포탈생성(self.ctx)


class 포탈생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[9500001,9500002,9500003,9500004,9500005,9500006,9500007,9500008,9500009,9500010], visible=True, arg3=0, delay=90, scale=1)
        self.set_mesh(triggerIds=[9600001,9600002,9600003,9600004,9600005,9600006,9600007,9600008,9600009,9600010,9600011,9600012,9600013,9600014], visible=True, arg3=0, delay=90, scale=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 길생성(self.ctx)


class 길생성(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[80001], visible=False, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return None


initial_state = 대기
