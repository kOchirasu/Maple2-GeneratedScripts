""" trigger/02000055_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[14]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=12, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[91], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[91]):
            return 종료체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[91])


class 종료체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=12, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=13, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
