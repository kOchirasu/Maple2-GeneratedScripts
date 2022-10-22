""" trigger/02000387_bf/2102_customer.xml """
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
        create_monster(spawnIds=[2102], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=2102, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=2102, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=2102, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9123, spawnIds=[2102]):
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
            return PickItem_30000623()
        if random_condition(rate=1):
            return PickItem_30000624()
        if random_condition(rate=1):
            return PickItem_30000625()
        if random_condition(rate=1):
            return PickItem_30000626()
        if random_condition(rate=1):
            return PickItem_30000627()
        if random_condition(rate=1):
            return PickItem_30000629()
        if random_condition(rate=1):
            return PickItem_30000631()
        if random_condition(rate=1):
            return PickItem_30000632()
        if random_condition(rate=1):
            return PickItem_30000633()
        if random_condition(rate=1):
            return PickItem_30000634()
        if random_condition(rate=1):
            return PickItem_30000635()
        if random_condition(rate=1):
            return PickItem_30000636()
        if random_condition(rate=1):
            return PickItem_30000637()
        if random_condition(rate=1):
            return PickItem_30000638()


#  	30000623 
class PickItem_30000623(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000623)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000623()


class DetectItem_30000623(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000623):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000623):
            return WrongItem()


#  	30000624 
class PickItem_30000624(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000624)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000624()


class DetectItem_30000624(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000624):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000624):
            return WrongItem()


#  	30000625 
class PickItem_30000625(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000625)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000625()


class DetectItem_30000625(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000625):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000625):
            return WrongItem()


#  	30000626 
class PickItem_30000626(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000626)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_C02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000626()


class DetectItem_30000626(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000626):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000626):
            return WrongItem()


#  	30000627 
class PickItem_30000627(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000627)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_D03.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000627()


class DetectItem_30000627(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000627):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000627):
            return WrongItem()


#  	30000629 
class PickItem_30000629(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000629)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000629()


class DetectItem_30000629(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000629):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000629):
            return WrongItem()


#  	30000631 
class PickItem_30000631(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000631)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washstand_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000631()


class DetectItem_30000631(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000631):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000631):
            return WrongItem()


#  	30000632 
class PickItem_30000632(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000632)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000632()


class DetectItem_30000632(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000632):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000632):
            return WrongItem()


#  	30000633 
class PickItem_30000633(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000633)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A03.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000633()


class DetectItem_30000633(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000633):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000633):
            return WrongItem()


#  	30000634 
class PickItem_30000634(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000634)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000634()


class DetectItem_30000634(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000634):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000634):
            return WrongItem()


#  	30000635 
class PickItem_30000635(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000635)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000635()


class DetectItem_30000635(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000635):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000635):
            return WrongItem()


#  	30000636 
class PickItem_30000636(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000636)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_toilet_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000636()


class DetectItem_30000636(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000636):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000636):
            return WrongItem()


#  	30000637 
class PickItem_30000637(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000637)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washer_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000637()


class DetectItem_30000637(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000637):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000637):
            return WrongItem()


#  	30000638 
class PickItem_30000638(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000638)
        add_effect_nif(spawnId=2102, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fan_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000638()


class DetectItem_30000638(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000638):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000638):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=2102)
        set_conversation(type=1, spawnId=2102, script='$02000387_BF__2102_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=2102, patrolName='MS2PatrolData_222')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9302, spawnIds=[2102]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=2102)
        set_conversation(type=1, spawnId=2102, script='$02000387_BF__2102_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000623):
            return PickItem_30000623()
        if user_value(key='ItemNumber', value=30000624):
            return PickItem_30000624()
        if user_value(key='ItemNumber', value=30000625):
            return PickItem_30000625()
        if user_value(key='ItemNumber', value=30000626):
            return PickItem_30000626()
        if user_value(key='ItemNumber', value=30000627):
            return PickItem_30000627()
        if user_value(key='ItemNumber', value=30000629):
            return PickItem_30000629()
        if user_value(key='ItemNumber', value=30000631):
            return PickItem_30000631()
        if user_value(key='ItemNumber', value=30000632):
            return PickItem_30000632()
        if user_value(key='ItemNumber', value=30000633):
            return PickItem_30000633()
        if user_value(key='ItemNumber', value=30000634):
            return PickItem_30000634()
        if user_value(key='ItemNumber', value=30000635):
            return PickItem_30000635()
        if user_value(key='ItemNumber', value=30000636):
            return PickItem_30000636()
        if user_value(key='ItemNumber', value=30000637):
            return PickItem_30000637()
        if user_value(key='ItemNumber', value=30000638):
            return PickItem_30000638()


