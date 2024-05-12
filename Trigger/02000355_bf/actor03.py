""" trigger/02000355_bf/actor03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[603], visible=False)
        self.set_actor(triggerId=203, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1301]):
            return 몬스터소환대기(self.ctx)
        if self.user_detected(boxIds=[1302]):
            return 몬스터소환대기(self.ctx)
        if self.user_detected(boxIds=[1303]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2003], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 더미해제(self.ctx)


class 더미해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=203, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2003]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
