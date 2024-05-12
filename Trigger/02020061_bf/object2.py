""" trigger/02020061_bf/object2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=0)
        self.set_interact_object(triggerIds=[12000085], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=1):
            return 레버2_체크(self.ctx)


class 레버2_체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[722], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[712]):
            return 레버2_발동(self.ctx)
        if self.user_detected(boxIds=[9012]):
            return 레버2_안내멘트(self.ctx)


class 레버2_안내멘트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02020061_BF__OBJECT2__0$', arg3='5000', arg4='9012')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[712]):
            return 레버2_발동(self.ctx)


class 레버2_발동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5101], visible=True)
        self.set_interact_object(triggerIds=[12000085], state=1)
        self.set_event_ui(type=1, arg2='$02020061_BF__OBJECT2__1$', arg3='5000', arg4='9012')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000085], stateValue=0):
            return 레버2_몬스터등장(self.ctx)


class 레버2_몬스터등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버2_재활성(self.ctx)


class 레버2_재활성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[12000085], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000085], stateValue=0):
            return 레버2_재활성_대기(self.ctx)


class 레버2_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=0):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=10000):
            return 레버2_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=2)
        self.destroy_monster(spawnIds=[722], arg2=False)
        self.set_interact_object(triggerIds=[12000085], state=2)


initial_state = 대기
