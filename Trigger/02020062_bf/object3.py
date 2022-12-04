""" trigger/02020062_bf/object3.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=0)
        self.set_interact_object(triggerIds=[12000109], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=1):
            return 레버3_가이드메시지(self.ctx)


class 레버3_가이드메시지(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[723], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[9013]):
            self.set_event_ui(type=1, arg2='$02020062_BF__OBJECT3__0$', arg3='5000', arg4='9013')
            return 레버3_체크(self.ctx)


class 레버3_체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[713]):
            return 레버3_발동(self.ctx)


class 레버3_발동(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5201], visible=True)
        self.set_interact_object(triggerIds=[12000109], state=1)
        self.set_event_ui(type=1, arg2='$02020062_BF__OBJECT3__1$', arg3='5000', arg4='9013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000109], stateValue=0):
            return 레버3_몬스터등장(self.ctx)


class 레버3_몬스터등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ObjectStart', value=2):
            return 대기(self.ctx)
        if self.monster_dead(boxIds=[701]):
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            return 레버3_재활성(self.ctx)


class 레버3_재활성(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[12000109], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[12000109], stateValue=0):
            return 레버3_재활성_대기(self.ctx)


class 레버3_재활성_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 종료(self.ctx)
        if self.wait_tick(waitTick=20000):
            return 레버3_재활성(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_user_value(triggerId=99990014, key='EliteSpawn', value=2)
        self.destroy_monster(spawnIds=[723], arg2=False)
        self.set_interact_object(triggerIds=[12000109], state=2)


initial_state = 대기
