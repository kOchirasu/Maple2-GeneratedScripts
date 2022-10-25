""" trigger/02020110_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901], jobCode=0):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            return 번방1(self.ctx)


class 번방1(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,120], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,120]):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 번방2(self.ctx)


class 번방2(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102,103,104,105,106,107], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[102,103,104,105,106,107]):
            self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
            return 번방3(self.ctx)


class 번방3(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[108,109,110,111,112,113], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[108,109,110,111,112,113]):
            self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)
            return 번방4(self.ctx)


class 번방4(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[114,115,116,117,118,119], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[114,115,116,117,118,119]):
            return 다음블록이동(self.ctx)


class 다음블록이동(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
