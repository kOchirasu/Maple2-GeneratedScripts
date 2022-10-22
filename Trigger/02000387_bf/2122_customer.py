""" trigger/02000387_bf/2122_customer.xml """
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
        create_monster(spawnIds=[2122], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=2122, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=2122, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=2122, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9123, spawnIds=[2122]):
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
            return PickItem_30000652()
        if random_condition(rate=1):
            return PickItem_30000680()


#  	30000652 
class PickItem_30000652(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000652)
        add_effect_nif(spawnId=2122, nifPath='Map/Common/Indoor/co_in_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000652()


class DetectItem_30000652(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000652):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000652):
            return WrongItem()


#  	30000680 
class PickItem_30000680(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000680)
        add_effect_nif(spawnId=2122, nifPath='Map/Royalcity/Indoor/ry_in_prop_grill_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000680()


class DetectItem_30000680(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000680):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000680):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=2122)
        set_conversation(type=1, spawnId=2122, script='$02000387_BF__2122_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=2122, patrolName='MS2PatrolData_222')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9302, spawnIds=[2122]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2122])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=2122)
        set_conversation(type=1, spawnId=2122, script='$02000387_BF__2122_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000652):
            return PickItem_30000652()
        if user_value(key='ItemNumber', value=30000680):
            return PickItem_30000680()


