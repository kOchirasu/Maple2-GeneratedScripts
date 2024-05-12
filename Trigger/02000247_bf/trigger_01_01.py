""" trigger/02000247_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[705,706], visible=True)
        self.set_mesh(triggerIds=[711,712], visible=False)
        self.destroy_monster(spawnIds=[601,602])
        self.set_effect(triggerIds=[2004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=201, minUsers='1'):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[711,712], visible=True)
        self.create_monster(spawnIds=[601,602], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602]):
            return 통과딜레이(self.ctx)


class 통과딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='3000', arg4='0')
        self.set_achievement(triggerId=999, type='trigger', achieve='GoldenTower3rd')
        self.dungeon_clear()
        self.set_timer(timerId='3', seconds=3)
        self.set_mesh(triggerIds=[711,712], visible=False)
        self.set_mesh(triggerIds=[705,706], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[2004], visible=True)


initial_state = 대기
