""" trigger/02000387_bf/2114_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001100], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2114], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2114, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2114, patrolName='MS2PatrolData_202')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2114, patrolName='MS2PatrolData_203')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9123, spawnIds=[2114]):
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001100], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001100], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001100], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000655(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000708(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000709(self.ctx)


# 30000655
class PickItem_30000655(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000655)
        self.add_effect_nif(spawnId=2114, nifPath='Map/Royalcity/Indoor/ry_in_prop_amp_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000655(self.ctx)


class DetectItem_30000655(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000655):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000655):
            return WrongItem(self.ctx)


# 30000708
class PickItem_30000708(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000708)
        self.add_effect_nif(spawnId=2114, nifPath='Effect/BG/Liftup/co_liftup_piano_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000708(self.ctx)


class DetectItem_30000708(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000708):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000708):
            return WrongItem(self.ctx)


# 30000709
class PickItem_30000709(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000709)
        self.add_effect_nif(spawnId=2114, nifPath='Effect/BG/Liftup/co_liftup_vibraphone_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000709(self.ctx)


class DetectItem_30000709(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000709):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000709):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=2114)
        self.set_conversation(type=1, spawnId=2114, script='$02000387_BF__2114_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2114, patrolName='MS2PatrolData_222')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9302, spawnIds=[2114]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2114])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=2114)
        self.set_conversation(type=1, spawnId=2114, script='$02000387_BF__2114_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000655):
            return PickItem_30000655(self.ctx)
        if self.user_value(key='ItemNumber', value=30000708):
            return PickItem_30000708(self.ctx)
        if self.user_value(key='ItemNumber', value=30000709):
            return PickItem_30000709(self.ctx)


initial_state = Wait
