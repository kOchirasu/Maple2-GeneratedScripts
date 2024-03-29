""" trigger/02000387_bf/1101_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001099], state=0) # Greeting
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
        self.create_monster(spawnIds=[1101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9110, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9111, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9112, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9113, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_103')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9113, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9113, spawnIds=[1101]):
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001099], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001099], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001099], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000634(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000690(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000693(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000712(self.ctx)


# 30000634
class PickItem_30000634(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000634)
        self.add_effect_nif(spawnId=1101, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000634(self.ctx)


class DetectItem_30000634(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000634):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000634):
            return WrongItem(self.ctx)


# 30000690
class PickItem_30000690(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000690)
        self.add_effect_nif(spawnId=1101, nifPath='Map/Tria/Indoor/tr_in_prop_sofa_D01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000690(self.ctx)


class DetectItem_30000690(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000690):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000690):
            return WrongItem(self.ctx)


# 30000693
class PickItem_30000693(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000693)
        self.add_effect_nif(spawnId=1101, nifPath='Map/Kerningcity/Indoor/ke_in_prop_massage_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000693(self.ctx)


class DetectItem_30000693(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000693):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000693):
            return WrongItem(self.ctx)


# 30000712
class PickItem_30000712(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000712)
        self.add_effect_nif(spawnId=1101, nifPath='Map/Orient/Indoor/or_in_prop_incense_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000712(self.ctx)


class DetectItem_30000712(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000712):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000712):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=1101)
        self.set_conversation(type=1, spawnId=1101, script='$02000387_BF__1101_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1101, patrolName='MS2PatrolData_111')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9301, spawnIds=[1101]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=1101)
        self.set_conversation(type=1, spawnId=1101, script='$02000387_BF__1101_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000634):
            return PickItem_30000634(self.ctx)
        if self.user_value(key='ItemNumber', value=30000690):
            return PickItem_30000690(self.ctx)
        if self.user_value(key='ItemNumber', value=30000693):
            return PickItem_30000693(self.ctx)
        if self.user_value(key='ItemNumber', value=30000712):
            return PickItem_30000712(self.ctx)


initial_state = Wait
