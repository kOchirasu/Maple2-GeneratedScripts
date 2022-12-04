""" trigger/02000524_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 난이도별보스등장(self.ctx)


class 난이도별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id(dungeonId=23046003):
            return 일반난이도_보스등장(self.ctx)
        if self.dungeon_id(dungeonId=23047003):
            return 어려움난이도_보스등장(self.ctx)
        if self.wait_tick(waitTick=1100):
            return 일반난이도_보스등장(self.ctx)


class 일반난이도_보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[98], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[98]):
            return 클리어처리(self.ctx)


class 어려움난이도_보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[99], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 클리어처리(self.ctx)


class 클리어처리(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            self.dungeon_clear()
            return 종료처리(self.ctx)


class 종료처리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
