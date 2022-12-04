""" trigger/02000387_bf/4116_customer.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001102], state=0) # Greeting
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
        self.create_monster(spawnIds=[4116], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9140, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9141, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4116, patrolName='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9142, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4116, patrolName='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9143, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4116, patrolName='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9143, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9143, spawnIds=[4116]):
            return WaitGreeting(self.ctx)


class WaitGreeting(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001102], state=1) # Greeting

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001102], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001102], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000639(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000640(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000703(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000704(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000705(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000715(self.ctx)


# 30000639
class PickItem_30000639(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000639)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000639(self.ctx)


class DetectItem_30000639(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000639):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000639):
            return WrongItem(self.ctx)


# 30000640
class PickItem_30000640(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000640)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000640(self.ctx)


class DetectItem_30000640(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000640):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000640):
            return WrongItem(self.ctx)


# 30000703
class PickItem_30000703(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000703)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000703(self.ctx)


class DetectItem_30000703(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000703):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000703):
            return WrongItem(self.ctx)


# 30000704
class PickItem_30000704(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000704)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000704(self.ctx)


class DetectItem_30000704(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000704):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000704):
            return WrongItem(self.ctx)


# 30000705
class PickItem_30000705(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000705)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000705(self.ctx)


class DetectItem_30000705(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000705):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000705):
            return WrongItem(self.ctx)


# 30000715
class PickItem_30000715(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000715)
        self.add_effect_nif(spawnId=4116, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000715(self.ctx)


class DetectItem_30000715(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000715):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000715):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=4116)
        self.set_conversation(type=1, spawnId=4116, script='$02000387_BF__4116_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4116, patrolName='MS2PatrolData_444')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9304, spawnIds=[4116]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4116])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=4116)
        self.set_conversation(type=1, spawnId=4116, script='$02000387_BF__4116_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000639):
            return PickItem_30000639(self.ctx)
        if self.user_value(key='ItemNumber', value=30000640):
            return PickItem_30000640(self.ctx)
        if self.user_value(key='ItemNumber', value=30000703):
            return PickItem_30000703(self.ctx)
        if self.user_value(key='ItemNumber', value=30000704):
            return PickItem_30000704(self.ctx)
        if self.user_value(key='ItemNumber', value=30000705):
            return PickItem_30000705(self.ctx)
        if self.user_value(key='ItemNumber', value=30000715):
            return PickItem_30000715(self.ctx)


initial_state = Wait
