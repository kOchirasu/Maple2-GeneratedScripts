""" trigger/02000500_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1099])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=99999, type='trigger', achieve='ClearDeborak') # ClearDeborak 퀘스트
        self.set_portal(portalId=11, visible=True, enable=True, minimapVisible=True)


initial_state = 시작대기중
