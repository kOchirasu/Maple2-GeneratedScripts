""" trigger/52100052_qd/04_randomportal.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002088], state=0) # ToWall_True
        self.set_interact_object(triggerIds=[10002089], state=0) # ToRoom_True
        self.set_interact_object(triggerIds=[10002090], state=0) # ToTower_True
        self.set_mesh(triggerIds=[3200], visible=True, arg3=0, delay=0, scale=0) # CurtainBarrier
        self.set_mesh(triggerIds=[3201,3202], visible=True, arg3=0, delay=0, scale=0) # CurtainOpen
        self.set_mesh(triggerIds=[3300], visible=True, arg3=0, delay=0, scale=0) # ToTowerDoorBarrier
        self.set_effect(triggerIds=[5000], visible=False) # DoorOpen
        self.set_actor(triggerId=4000, visible=True, initialSequence='Closed') # NextMap
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # ToWall
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # ToRoom
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False) # ToTower
        self.set_user_value(key='SearchStart', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='SearchStart', value=1):
            return PickRandomPortal(self.ctx)


# 3개의 문 중에서 하나 뽑기
class PickRandomPortal(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=30):
            return ToWall01(self.ctx)
        if self.random_condition(rate=30):
            return ToRoom01(self.ctx)
        if self.random_condition(rate=30):
            return ToTower01(self.ctx)


# 테라스로 나가서 성 외벽으로
class ToWall01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002088], state=1) # ToWall_True
        self.set_user_value(triggerId=6, key='ToRoomFalse', value=1) # ToRoom_False
        self.set_user_value(triggerId=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002088], stateValue=0):
            return ToWall02(self.ctx)


class ToWall02(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3200], visible=False, arg3=0, delay=0, scale=0) # CurtainBarrier
        self.set_mesh(triggerIds=[3201,3202], visible=False, arg3=0, delay=0, scale=3) # CurtainOpen
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=False) # ToWall
        self.set_event_ui(type=1, arg2='$02000396_BF__04_RANDOMPORTAL__0$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ToWallGuide01(self.ctx)


class ToWallGuide01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__0$', arg4=5) # 이슈라
        self.set_skip(state=ToWallGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ToWallGuide01Skip(self.ctx)


class ToWallGuide01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 문을 통해 다른 방으로
class ToRoom01(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002089], state=1) # ToRoom_True
        self.set_user_value(triggerId=5, key='ToWallFalse', value=1) # ToWall_False
        self.set_user_value(triggerId=7, key='ToTowerFalse', value=1) # ToTowerFalse

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002089], stateValue=0):
            return ToRoom02(self.ctx)


class ToRoom02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100052_QD__04_RANDOMPORTAL__1$', arg3='2000', arg4='0')
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=False) # ToRoom

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ToRoomGuide01(self.ctx)


class ToRoomGuide01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__2$', arg4=5) # 이슈라
        self.set_skip(state=ToRoomGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ToRoomGuide01Skip(self.ctx)


class ToRoomGuide01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


# 계단을 통해 탑으로
class ToTower01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=5, key='ToWallFalse', value=1) # ToWall_False
        self.set_user_value(triggerId=6, key='ToRoomFalse', value=1) # ToRoom_False
        self.set_interact_object(triggerIds=[10002090], state=1) # ToTower_True

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002090], stateValue=0):
            return ToTower02(self.ctx)


class ToTower02(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$52100052_QD__04_RANDOMPORTAL__3$', arg3='2000', arg4='0')
        self.set_mesh(triggerIds=[3300], visible=False, arg3=0, delay=0, scale=0) # ToTowerDoorBarrier
        self.set_effect(triggerIds=[5000], visible=True) # DoorOpen
        self.set_actor(triggerId=4000, visible=True, initialSequence='Opened') # NextMap
        self.set_portal(portalId=30, visible=True, enable=True, minimapVisible=False) # ToTower

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ToTowerGuide01(self.ctx)


class ToTowerGuide01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001563, script='$52100052_QD__04_RANDOMPORTAL__4$', arg4=5) # 이슈라
        self.set_skip(state=ToTowerGuide01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ToTowerGuide01Skip(self.ctx)


class ToTowerGuide01Skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=1, key='FindWay', value=1)


initial_state = Wait
