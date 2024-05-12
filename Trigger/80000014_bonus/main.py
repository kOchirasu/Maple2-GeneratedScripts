""" trigger/80000014_bonus/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001337], state=1)
        self.set_interact_object(triggerIds=[10001338], state=2)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3002,3003,3004], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3101,3102,3201,3202,3301,3302,3401,3402,3601,3602,3603,3604], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            # self.set_timer(timerId='30', seconds=600, startDelay=1, interval=1, vOffset=80)
            return 랜덤A(self.ctx)


class 랜덤A(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤B(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤B(self.ctx)


class 랜덤B(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3201], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤C(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3202], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤C(self.ctx)


class 랜덤C(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3301], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤D(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3302], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤D(self.ctx)


class 랜덤D(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3401], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤E(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3402], visible=True, arg3=0, delay=0, scale=0)
            return 랜덤E(self.ctx)


class 랜덤E(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3601,3602], visible=True, arg3=0, delay=0, scale=0)
            return 시작(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3603,3604], visible=True, arg3=0, delay=0, scale=0)
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$80000014_bonus__main__0$', arg3='5000')
        self.score_board_create(type='ScoreBoardTopCenter', maxScore=0)
        self.score_board_set_score(score=0)
        self.spawn_item_range(rangeIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019], randomPickCount=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_npc_range(rangeIds=[2001], isAutoTargeting=False, score=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.set_mesh(triggerIds=[3000,3001], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[3002,3003,3004], visible=True, arg3=0, delay=0, scale=0)
            return 정산(self.ctx)


class 정산(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.score_board_compare(operator='GreaterEqual', score=18000):
            self.debug_string(value='18000 이상')
            self.set_achievement(triggerId=199, type='trigger', achieve='HighScoreTreasureMap01')
            self.set_achievement(triggerId=199, type='trigger', achieve='TimerunTreasureMap01')
            # self.set_event_ui(type=7, arg2='미션 성공! 참 잘했어요!', arg3='2500')
            return 반응대기(self.ctx)
        if self.score_board_compare(operator='Less', score=18000):
            self.debug_string(value='18000 미만')
            self.set_achievement(triggerId=199, type='trigger', achieve='TimerunTreasureMap01')
            # self.set_event_ui(type=7, arg2='미션 성공!', arg3='2500')
            return 반응대기(self.ctx)
        if self.wait_tick(waitTick=500):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10001338], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001338], stateValue=0):
            self.set_achievement(triggerId=199, type='trigger', achieve='TreasureMap01')
            self.dungeon_clear()
            self.score_board_remove()
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
