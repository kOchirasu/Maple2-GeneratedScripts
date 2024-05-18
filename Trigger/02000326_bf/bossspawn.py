""" trigger/02000326_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1099])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1099]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=99999, type='trigger', achieve='ClearDeborak') # ClearDeborak 퀘스트
        self.set_portal(portal_id=11, visible=True, enable=True, minimap_visible=True)


initial_state = 시작대기중
