""" trigger/02000254_bf/elite.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[801], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[802], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[803], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[804], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[805], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[806], visible=False, animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903]):
            return 딜레이1(self.ctx)


class 딜레이1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 탄2(self.ctx)
        if self.monster_dead(boxIds=[106]):
            return 클리어딜레이(self.ctx)


class 탄2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[104])
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 탄3(self.ctx)
        if self.monster_dead(boxIds=[106]):
            return 클리어딜레이(self.ctx)


class 탄3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[105])
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 탄4(self.ctx)
        if self.monster_dead(boxIds=[106]):
            return 클리어딜레이(self.ctx)


class 탄4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[105])
        self.create_monster(spawnIds=[104])
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 탄5(self.ctx)
        if self.monster_dead(boxIds=[106]):
            return 클리어딜레이(self.ctx)


class 탄5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[104])
        self.create_monster(spawnIds=[103])
        self.set_timer(timerId='1', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 탄2(self.ctx)
        if self.monster_dead(boxIds=[106]):
            return 클리어딜레이(self.ctx)


class 클리어딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 클리어(self.ctx)


class 클리어(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 클리어2(self.ctx)


class 클리어2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=14)
        self.set_conversation(type=2, spawnId=11000057, script='$02000254_BF__ELITE__0$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 클리어3(self.ctx)


class 클리어3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)
        self.destroy_monster(spawnIds=[103])
        self.destroy_monster(spawnIds=[104])
        self.destroy_monster(spawnIds=[105])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # self.set_event_ui(type=7, arg2='$02000254_BF__ELITE__1$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 사다리생성(self.ctx)


class 사다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[801], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[802], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[803], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[804], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[805], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[806], visible=True, animationEffect=True)
        self.dungeon_clear()
        self.hide_guide_summary(entityId=20002524)


initial_state = 시작대기중
