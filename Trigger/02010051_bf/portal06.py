""" trigger/02010051_bf/portal06.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[900], visible=False)
        self.set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=True, arg3=0, delay=0, scale=0) # Gate Close grating
        self.set_mesh(triggerIds=[1511,1512,1513], visible=False, arg3=0, delay=0, scale=0) # Gate Open grating
        self.set_effect(triggerIds=[914], visible=False) # light
        self.set_interact_object(triggerIds=[10000914], state=0)
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=True, arg3=0, delay=0, scale=0) # grating
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6001], visible=False) # vibrate
        self.set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6005], visible=False) # MainGateOpen vibrate
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='1', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 대화연출준비01(self.ctx)


class 대화연출준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출대화01(self.ctx)


class 연출대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='2', seconds=3)
        self.set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL06__0$', arg4=3)
        self.set_skip(state=연출대화02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 연출대화02대기(self.ctx)


class 연출대화02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출대화02(self.ctx)


class 연출대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=4)
        self.set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL06__1$', arg4=3)
        self.set_skip(state=대화연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 대화연출종료01(self.ctx)


class 대화연출종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 문열기01(self.ctx)


class 문열기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[6005], visible=True) # MainGateOpen vibrate
        self.set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506], visible=False, arg3=0, delay=0, scale=10) # Gate Close grating
        self.set_mesh(triggerIds=[1511,1512,1513], visible=True, arg3=1, delay=0, scale=0) # Gate Open grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 유저입장01(self.ctx)


class 유저입장01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return 가이드준비(self.ctx)


class 가이드준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='10', seconds=7) # VoicePlay

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 가이드시작(self.ctx)


class 가이드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기
        self.set_interact_object(triggerIds=[10000914], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000914], stateValue=0):
            return 포털개방01(self.ctx)


class 포털개방01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='11', seconds=1)
        self.set_effect(triggerIds=[914], visible=True) # light
        self.set_effect(triggerIds=[6000], visible=True) # DoorOpen vibrate
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=False, arg3=0, delay=0, scale=10) # grating

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='11'):
            return 포털개방02(self.ctx)


class 포털개방02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=11, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000835], stateValue=0):
            return 포털폐쇄(self.ctx)


class 포털폐쇄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=11, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606], visible=True, arg3=0, delay=0, scale=2) # grating
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6005], visible=False) # MainGateOpen vibrate


initial_state = 대기
