""" trigger/02010051_bf/portal03.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6000], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6001], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6002], visible=False) # DoorOpen vibrate
        self.set_effect(triggerIds=[6003], visible=False) # DoorOpen vibrate
        self.set_portal(portalId=50, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[837], visible=False) # light
        self.set_mesh(triggerIds=[2000,2001,2002,2003], visible=True, arg3=0, delay=0, scale=0) # invisible barrier
        self.set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105], visible=True, arg3=0, delay=0, scale=0) # invisible barrier
        self.set_mesh(triggerIds=[2200], visible=True, arg3=0, delay=0, scale=0) # fence
        self.set_mesh(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=False, arg3=0, delay=0, scale=0) # stairs
        self.set_mesh(triggerIds=[13001,13002,13003,13004,13005,13006,13007,13008,13009,13010,13011,13012,13013,13014,13015,13016,13017,13018,13019,13020,13021,13022,13023,13024,13025,13026,13027,13028,13029,13030,13031,13032,13033,13034,13035,13036,13037,13038,13039], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000837], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9012]):
            return 입장딜레이01(self.ctx)


class 입장딜레이01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_mesh(triggerIds=[2000,2001,2002,2003], visible=False, arg3=0, delay=0, scale=0) # invisible barrier
        self.set_mesh(triggerIds=[2100,2101,2102,2103,2104,2105], visible=False, arg3=0, delay=0, scale=0) # invisible barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 가이드준비01(self.ctx)


class 가이드준비01(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20105101, textId=20105101, duration=4000) # 길 찾기

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000837], stateValue=0):
            return 포털개방01(self.ctx)


class 포털개방01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=7, key='timercheck', value=1)
        self.set_timer(timerId='10', seconds=2)
        self.set_portal(portalId=50, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[6003], visible=True) # vibrate
        self.set_effect(triggerIds=[837], visible=True) # light
        self.set_random_mesh(triggerIds=[5000,5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=True, meshCount=10, arg4=50, delay=50) # stairs
        self.set_mesh(triggerIds=[13001,13002,13003,13004,13005,13006,13007,13008,13009,13010,13011,13012,13013,13014,13015,13016,13017,13018,13019,13020,13021,13022,13023,13024,13025,13026,13027,13028,13029,13030,13031,13032,13033,13034,13035,13036,13037,13038,13039], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[2200], visible=False, arg3=0, delay=0, scale=10) # fence

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='10'):
            return 대화연출준비01(self.ctx)


class 대화연출준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출대화01(self.ctx)


class 연출대화01(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='20', seconds=3)
        self.set_conversation(type=2, spawnId=11001319, script='$02010051_BF__PORTAL03__0$', arg4=3)
        self.set_skip(state=대화연출종료01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='20'):
            return 대화연출종료01(self.ctx)


class 대화연출종료01(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6003], visible=False) # vibrate


initial_state = 대기
