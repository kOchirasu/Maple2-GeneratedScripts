""" trigger/02000282_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000424], state=0)
        self.set_interact_object(triggerIds=[10000425], state=0)
        self.set_interact_object(triggerIds=[10000426], state=0)
        self.set_interact_object(triggerIds=[10000433], state=2)
        self.set_interact_object(triggerIds=[10000434], state=2)
        self.set_interact_object(triggerIds=[10000435], state=2)
        self.set_ladder(triggerIds=[341], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[342], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[343], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[351], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[352], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[353], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[361], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[362], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[363], visible=False, animationEffect=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.create_monster(spawnIds=[1003], animationEffect=False)
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.create_monster(spawnIds=[1006], animationEffect=False)
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.create_monster(spawnIds=[1008], animationEffect=False)
        self.create_monster(spawnIds=[1009], animationEffect=False)
        self.create_monster(spawnIds=[1010], animationEffect=False)
        self.create_monster(spawnIds=[1011], animationEffect=False)
        self.create_monster(spawnIds=[1012], animationEffect=False)
        self.create_monster(spawnIds=[1014], animationEffect=False)
        self.create_monster(spawnIds=[1015], animationEffect=False)
        self.create_monster(spawnIds=[1016], animationEffect=False)
        self.create_monster(spawnIds=[1017], animationEffect=False)
        self.create_monster(spawnIds=[1018], animationEffect=False)
        self.create_monster(spawnIds=[1019], animationEffect=False)
        self.create_monster(spawnIds=[1020], animationEffect=False)
        self.create_monster(spawnIds=[1021], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return 번생성4(self.ctx)
        if self.random_condition(rate=33):
            return 번생성5(self.ctx)
        if self.random_condition(rate=34):
            return 번생성6(self.ctx)


class 번생성4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000424], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000424], stateValue=0):
            return 번몬스터4(self.ctx)


class 번몬스터4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2004]):
            self.show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(triggerIds=[341], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[342], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[343], visible=True, animationEffect=True)
            self.set_portal(portalId=4, visible=False, enable=True, minimapVisible=True)
            return 소멸대기(self.ctx)


class 번생성5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000425], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000425], stateValue=0):
            return 번몬스터5(self.ctx)


class 번몬스터5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2005], animationEffect=False)
        self.show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2005]):
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            self.set_ladder(triggerIds=[351], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[352], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[353], visible=True, animationEffect=True)
            self.set_portal(portalId=5, visible=False, enable=True, minimapVisible=True)
            return 소멸대기(self.ctx)


class 번생성6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000426], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000426], stateValue=0):
            return 번몬스터6(self.ctx)


class 번몬스터6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2006]):
            self.show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            self.set_ladder(triggerIds=[361], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[362], visible=True, animationEffect=True)
            self.set_ladder(triggerIds=[363], visible=True, animationEffect=True)
            self.set_portal(portalId=6, visible=False, enable=True, minimapVisible=True)
            return 소멸대기(self.ctx)


class 소멸대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    pass


initial_state = 대기
