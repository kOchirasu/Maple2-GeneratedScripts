""" trigger/02000251_bf/trigger_01_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[705,706], visible=True)
        self.set_mesh(triggerIds=[711,712], visible=False)
        self.destroy_monster(spawnIds=[601,602,603,604])
        self.set_effect(triggerIds=[3004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=201, minUsers='1'):
            return 몹생성(self.ctx)


class 몹생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[711,712], visible=True)
        self.create_monster(spawnIds=[601,602,603,604], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603,604]):
            return 통과딜레이(self.ctx)


class 통과딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)
        # self.set_event_ui(type=7, arg2='$02000251_BF__TRIGGER_01_01__0$', arg3='3000', arg4='0')
        self.set_achievement(triggerId=1000, type='trigger', achieve='goldenTower')
        # self.create_item(spawnIds=[9001], triggerId=998)
        self.dungeon_clear()
        self.set_mesh(triggerIds=[705,706], visible=False)
        self.set_mesh(triggerIds=[711,712], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 통과(self.ctx)


class 통과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3004], visible=True)


initial_state = 대기
