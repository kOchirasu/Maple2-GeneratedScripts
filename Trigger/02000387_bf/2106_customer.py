""" trigger/02000387_bf/2106_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001100], state=0) # Greeting
        set_user_value(key='CustomerEnter', value=0)
        set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay()


class CustomerEnterDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CustomerEnter()


class CustomerEnter(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2106], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=2106, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=2106, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=2106, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9123, spawnIds=[2106]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001100], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001100], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001100], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000703()
        if random_condition(rate=1):
            return PickItem_30000704()
        if random_condition(rate=1):
            return PickItem_30000705()
        if random_condition(rate=1):
            return PickItem_30000715()


#  	30000703 
class PickItem_30000703(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000703)
        add_effect_nif(spawnId=2106, nifPath='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000703()


class DetectItem_30000703(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000703):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000703):
            return WrongItem()


#  	30000704 
class PickItem_30000704(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000704)
        add_effect_nif(spawnId=2106, nifPath='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000704()


class DetectItem_30000704(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000704):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000704):
            return WrongItem()


#  	30000705 
class PickItem_30000705(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000705)
        add_effect_nif(spawnId=2106, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000705()


class DetectItem_30000705(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000705):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000705):
            return WrongItem()


#  	30000715 
class PickItem_30000715(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000715)
        add_effect_nif(spawnId=2106, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000715()


class DetectItem_30000715(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000715):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000715):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=2106)
        set_conversation(type=1, spawnId=2106, script='$02000387_BF__2106_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=2106, patrolName='MS2PatrolData_222')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9302, spawnIds=[2106]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2106])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=2106)
        set_conversation(type=1, spawnId=2106, script='$02000387_BF__2106_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000703):
            return PickItem_30000703()
        if user_value(key='ItemNumber', value=30000704):
            return PickItem_30000704()
        if user_value(key='ItemNumber', value=30000705):
            return PickItem_30000705()
        if user_value(key='ItemNumber', value=30000715):
            return PickItem_30000715()


