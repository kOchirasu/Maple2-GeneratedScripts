""" trigger/02000243_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[705,706], visible=True)
        self.set_mesh(triggerIds=[711,712], visible=False)
        self.destroy_monster(spawnIds=[601])
        self.set_effect(triggerIds=[2004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=201, minUsers='1'):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[711,712], visible=True)
        self.create_monster(spawnIds=[601], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601]):
            return 통과딜레이(self.ctx)


class 통과딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=999, type='trigger', achieve='GoldenTower2nd')
        self.set_achievement(triggerId=999, type='trigger', achieve='ClearGoldentowerfirst')
        self.dungeon_clear()
        self.set_timer(timerId='3', seconds=3)
        self.set_mesh(triggerIds=[705,706], visible=False)
        self.set_mesh(triggerIds=[711,712], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[2004], visible=True)
        self.set_timer(timerId='1', seconds=180)


initial_state = 대기
