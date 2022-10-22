""" trigger/02000387_bf/2002_customer.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001093], state=0) # Greeting
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
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03()
        if not npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01()


class Patrol01(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData_201')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay()


class Patrol02Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol02()


class Patrol02(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay()


class Patrol03Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Patrol03()


class Patrol03(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData_203')

    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay()


class PatrolEndDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PatrolEnd()


class PatrolEnd(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9123, spawnIds=[2002]):
            return WaitGreeting()


class WaitGreeting(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001093], state=1) # Greeting

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001093], arg2=0):
            return OrderRandomPick()

    def on_exit(self):
        set_interact_object(triggerIds=[10001093], state=2) # Greeting


#  고객 주문 랜덤
class OrderRandomPick(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return PickItem_30000617()
        if random_condition(rate=1):
            return PickItem_30000618()
        if random_condition(rate=1):
            return PickItem_30000619()
        if random_condition(rate=1):
            return PickItem_30000620()
        if random_condition(rate=1):
            return PickItem_30000621()
        if random_condition(rate=1):
            return PickItem_30000622()
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
            return PickItem_30000628()
        if random_condition(rate=1):
            return PickItem_30000629()
        if random_condition(rate=1):
            return PickItem_30000630()
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
        if random_condition(rate=1):
            return PickItem_30000639()
        if random_condition(rate=1):
            return PickItem_30000640()
        if random_condition(rate=1):
            return PickItem_30000641()
        if random_condition(rate=1):
            return PickItem_30000642()
        if random_condition(rate=1):
            return PickItem_30000643()
        if random_condition(rate=1):
            return PickItem_30000644()
        if random_condition(rate=1):
            return PickItem_30000645()
        if random_condition(rate=1):
            return PickItem_30000646()
        if random_condition(rate=1):
            return PickItem_30000647()
        if random_condition(rate=1):
            return PickItem_30000648()
        if random_condition(rate=1):
            return PickItem_30000649()
        if random_condition(rate=1):
            return PickItem_30000650()
        if random_condition(rate=1):
            return PickItem_30000651()
        if random_condition(rate=1):
            return PickItem_30000652()
        if random_condition(rate=1):
            return PickItem_30000653()
        if random_condition(rate=1):
            return PickItem_30000654()
        if random_condition(rate=1):
            return PickItem_30000655()
        if random_condition(rate=1):
            return PickItem_30000656()
        if random_condition(rate=1):
            return PickItem_30000657()
        if random_condition(rate=1):
            return PickItem_30000658()
        if random_condition(rate=1):
            return PickItem_30000659()
        if random_condition(rate=1):
            return PickItem_30000660()
        if random_condition(rate=1):
            return PickItem_30000661()
        if random_condition(rate=1):
            return PickItem_30000662()
        if random_condition(rate=1):
            return PickItem_30000663()
        if random_condition(rate=1):
            return PickItem_30000664()
        if random_condition(rate=1):
            return PickItem_30000665()
        if random_condition(rate=1):
            return PickItem_30000666()
        if random_condition(rate=1):
            return PickItem_30000667()
        if random_condition(rate=1):
            return PickItem_30000668()
        if random_condition(rate=1):
            return PickItem_30000669()
        if random_condition(rate=1):
            return PickItem_30000670()
        if random_condition(rate=1):
            return PickItem_30000671()
        if random_condition(rate=1):
            return PickItem_30000672()
        if random_condition(rate=1):
            return PickItem_30000673()
        if random_condition(rate=1):
            return PickItem_30000674()
        if random_condition(rate=1):
            return PickItem_30000675()
        if random_condition(rate=1):
            return PickItem_30000676()
        if random_condition(rate=1):
            return PickItem_30000677()
        if random_condition(rate=1):
            return PickItem_30000678()
        if random_condition(rate=1):
            return PickItem_30000679()
        if random_condition(rate=1):
            return PickItem_30000680()
        if random_condition(rate=1):
            return PickItem_30000681()
        if random_condition(rate=1):
            return PickItem_30000682()
        if random_condition(rate=1):
            return PickItem_30000683()
        if random_condition(rate=1):
            return PickItem_30000684()
        if random_condition(rate=1):
            return PickItem_30000685()
        if random_condition(rate=1):
            return PickItem_30000686()
        if random_condition(rate=1):
            return PickItem_30000687()
        if random_condition(rate=1):
            return PickItem_30000688()
        if random_condition(rate=1):
            return PickItem_30000689()
        if random_condition(rate=1):
            return PickItem_30000690()
        if random_condition(rate=1):
            return PickItem_30000691()
        if random_condition(rate=1):
            return PickItem_30000692()
        if random_condition(rate=1):
            return PickItem_30000693()
        if random_condition(rate=1):
            return PickItem_30000694()
        if random_condition(rate=1):
            return PickItem_30000695()
        if random_condition(rate=1):
            return PickItem_30000696()
        if random_condition(rate=1):
            return PickItem_30000697()
        if random_condition(rate=1):
            return PickItem_30000698()
        if random_condition(rate=1):
            return PickItem_30000699()
        if random_condition(rate=1):
            return PickItem_30000700()
        if random_condition(rate=1):
            return PickItem_30000701()
        if random_condition(rate=1):
            return PickItem_30000702()
        if random_condition(rate=1):
            return PickItem_30000703()
        if random_condition(rate=1):
            return PickItem_30000704()
        if random_condition(rate=1):
            return PickItem_30000705()
        if random_condition(rate=1):
            return PickItem_30000706()
        if random_condition(rate=1):
            return PickItem_30000707()
        if random_condition(rate=1):
            return PickItem_30000708()
        if random_condition(rate=1):
            return PickItem_30000709()
        if random_condition(rate=1):
            return PickItem_30000710()
        if random_condition(rate=1):
            return PickItem_30000711()
        if random_condition(rate=1):
            return PickItem_30000712()
        if random_condition(rate=1):
            return PickItem_30000713()
        if random_condition(rate=1):
            return PickItem_30000714()
        if random_condition(rate=1):
            return PickItem_30000715()
        if random_condition(rate=1):
            return PickItem_30000716()


#  	30000617 
class PickItem_30000617(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000617)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Field/co_fi_prop_game_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000617()


class DetectItem_30000617(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000617):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000617):
            return WrongItem()


#  	30000618 
class PickItem_30000618(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000618)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Field/co_fi_prop_game_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000618()


class DetectItem_30000618(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000618):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000618):
            return WrongItem()


#  	30000619 
class PickItem_30000619(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000619)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Field/co_fi_prop_lamp_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000619()


class DetectItem_30000619(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000619):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000619):
            return WrongItem()


class PickItem_30000620(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000620)
        add_effect_nif(spawnId=2002, nifPath='Map/Henesys/Indoor/he_in_prop_fireplace_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000620()


class DetectItem_30000620(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000620):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000620):
            return WrongItem()


#  	30000621 
class PickItem_30000621(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000621)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_sandbag_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000621()


class DetectItem_30000621(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000621):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000621):
            return WrongItem()


#  	30000622 
class PickItem_30000622(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000622)
        add_effect_nif(spawnId=2002, nifPath='Map/Iceland/Indoor/ic_in_prop_snowball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000622()


class DetectItem_30000622(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000622):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000622):
            return WrongItem()


#  	30000623 
class PickItem_30000623(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000623)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_bath_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_shower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_C02.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_D03.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000627()


class DetectItem_30000627(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000627):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000627):
            return WrongItem()


#  	30000628 
class PickItem_30000628(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000628)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_display_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000628()


class DetectItem_30000628(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000628):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000628):
            return WrongItem()


#  	30000629 
class PickItem_30000629(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000629)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fridge_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000629()


class DetectItem_30000629(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000629):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000629):
            return WrongItem()


#  	30000630 
class PickItem_30000630(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000630)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_display_C02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000630()


class DetectItem_30000630(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000630):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000630):
            return WrongItem()


#  	30000631 
class PickItem_30000631(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000631)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washstand_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_sink_A03.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_tv_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_toilet_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_washer_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_fan_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000638()


class DetectItem_30000638(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000638):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000638):
            return WrongItem()


#  	30000639 
class PickItem_30000639(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000639)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_machine_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000639()


class DetectItem_30000639(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000639):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000639):
            return WrongItem()


#  	30000640 
class PickItem_30000640(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000640)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_cutter_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000640()


class DetectItem_30000640(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000640):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000640):
            return WrongItem()


#  	30000641 
class PickItem_30000641(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000641)
        add_effect_nif(spawnId=2002, nifPath='Map/Henesys/Indoor/he_in_prop_kettle_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000641()


class DetectItem_30000641(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000641):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000641):
            return WrongItem()


#  	30000642 
class PickItem_30000642(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000642)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_locker_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000642()


class DetectItem_30000642(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000642):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000642):
            return WrongItem()


#  	30000643 
class PickItem_30000643(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000643)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_locker_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000643()


class DetectItem_30000643(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000643):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000643):
            return WrongItem()


#  	30000644 
class PickItem_30000644(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000644)
        add_effect_nif(spawnId=2002, nifPath='Map/Iceland/Indoor/ic_in_cubric_box_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000644()


class DetectItem_30000644(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000644):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000644):
            return WrongItem()


#  	30000645 
class PickItem_30000645(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000645)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Field/tr_fi_prop_swing_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000645()


class DetectItem_30000645(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000645):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000645):
            return WrongItem()


#  	30000646 
class PickItem_30000646(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000646)
        add_effect_nif(spawnId=2002, nifPath='Map/UGC/Indoor/ugc_in_funct_cook_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000646()


class DetectItem_30000646(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000646):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000646):
            return WrongItem()


#  	30000647 
class PickItem_30000647(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000647)
        add_effect_nif(spawnId=2002, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000647()


class DetectItem_30000647(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000647):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000647):
            return WrongItem()


#  	30000648 
class PickItem_30000648(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000648)
        add_effect_nif(spawnId=2002, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000648()


class DetectItem_30000648(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000648):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000648):
            return WrongItem()


#  	30000649 
class PickItem_30000649(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000649)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_mirror_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000649()


class DetectItem_30000649(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000649):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000649):
            return WrongItem()


#  	30000650 
class PickItem_30000650(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000650)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_easel_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000650()


class DetectItem_30000650(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000650):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000650):
            return WrongItem()


#  	30000651 
class PickItem_30000651(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000651)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_wardrop_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000651()


class DetectItem_30000651(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000651):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000651):
            return WrongItem()


#  	30000652 
class PickItem_30000652(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000652)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Indoor/co_in_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000652()


class DetectItem_30000652(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000652):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000652):
            return WrongItem()


#  	30000653 
class PickItem_30000653(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000653)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_tray_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000653()


class DetectItem_30000653(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000653):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000653):
            return WrongItem()


#  	30000654 
class PickItem_30000654(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000654)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_sofa_E01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000654()


class DetectItem_30000654(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000654):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000654):
            return WrongItem()


#  	30000655 
class PickItem_30000655(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000655)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_amp_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000655()


class DetectItem_30000655(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000655):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000655):
            return WrongItem()


#  	30000656 
class PickItem_30000656(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000656)
        add_effect_nif(spawnId=2002, nifPath='Map/SF/Indoor/sf_in_prop_bed_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000656()


class DetectItem_30000656(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000656):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000656):
            return WrongItem()


#  	30000657 
class PickItem_30000657(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000657)
        add_effect_nif(spawnId=2002, nifPath='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000657()


class DetectItem_30000657(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000657):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000657):
            return WrongItem()


#  	30000658 
class PickItem_30000658(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000658)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_ringer_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000658()


class DetectItem_30000658(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000658):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000658):
            return WrongItem()


#  	30000659 
class PickItem_30000659(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000659)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Indoor/co_in_prop_guestbook_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000659()


class DetectItem_30000659(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000659):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000659):
            return WrongItem()


#  	30000660 
class PickItem_30000660(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000660)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_display_B02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000660()


class DetectItem_30000660(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000660):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000660):
            return WrongItem()


#  	30000661 
class PickItem_30000661(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000661)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_cubric_fishtank_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000661()


class DetectItem_30000661(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000661):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000661):
            return WrongItem()


#  	30000662 
class PickItem_30000662(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000662)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_basketball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000662()


class DetectItem_30000662(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000662):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000662):
            return WrongItem()


#  	30000663 
class PickItem_30000663(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000663)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_running_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000663()


class DetectItem_30000663(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000663):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000663):
            return WrongItem()


#  	30000664 
class PickItem_30000664(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000664)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_trampoline_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000664()


class DetectItem_30000664(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000664):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000664):
            return WrongItem()


#  	30000665 
class PickItem_30000665(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000665)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_baseballcart_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000665()


class DetectItem_30000665(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000665):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000665):
            return WrongItem()


#  	30000666 
class PickItem_30000666(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000666)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_basketball_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000666()


class DetectItem_30000666(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000666):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000666):
            return WrongItem()


#  	30000667 
class PickItem_30000667(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000667)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_handball_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000667()


class DetectItem_30000667(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000667):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000667):
            return WrongItem()


#  	30000668 
class PickItem_30000668(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000668)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_cranegame_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000668()


class DetectItem_30000668(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000668):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000668):
            return WrongItem()


#  	30000669 
class PickItem_30000669(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000669)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_chandelier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000669()


class DetectItem_30000669(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000669):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000669):
            return WrongItem()


#  	30000670 
class PickItem_30000670(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000670)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_goalpost_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000670()


class DetectItem_30000670(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000670):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000670):
            return WrongItem()


#  	30000671 
class PickItem_30000671(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000671)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_photosticker_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000671()


class DetectItem_30000671(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000671):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000671):
            return WrongItem()


#  	30000672 
class PickItem_30000672(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000672)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_pingpong_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000672()


class DetectItem_30000672(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000672):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000672):
            return WrongItem()


#  	30000673 
class PickItem_30000673(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000673)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_pooltable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000673()


class DetectItem_30000673(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000673):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000673):
            return WrongItem()


#  	30000674 
class PickItem_30000674(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000674)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_pump_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000674()


class DetectItem_30000674(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000674):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000674):
            return WrongItem()


#  	30000675 
class PickItem_30000675(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000675)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_sewingmachine_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000675()


class DetectItem_30000675(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000675):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000675):
            return WrongItem()


#  	30000676 
class PickItem_30000676(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000676)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_soccertable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000676()


class DetectItem_30000676(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000676):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000676):
            return WrongItem()


#  	30000677 
class PickItem_30000677(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000677)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Field/ry_fi_prop_plane_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000677()


class DetectItem_30000677(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000677):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000677):
            return WrongItem()


#  	30000678 
class PickItem_30000678(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000678)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Field/ry_fi_prop_hammock_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000678()


class DetectItem_30000678(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000678):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000678):
            return WrongItem()


#  	30000679 
class PickItem_30000679(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000679)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Field/ry_fi_prop_yacht_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000679()


class DetectItem_30000679(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000679):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000679):
            return WrongItem()


#  	30000680 
class PickItem_30000680(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000680)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_grill_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000680()


class DetectItem_30000680(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000680):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000680):
            return WrongItem()


#  	30000681 
class PickItem_30000681(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000681)
        add_effect_nif(spawnId=2002, nifPath='Map/Orient/Field/or_fi_prop_seesaw_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000681()


class DetectItem_30000681(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000681):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000681):
            return WrongItem()


#  	30000682 
class PickItem_30000682(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000682)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_display_E01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000682()


class DetectItem_30000682(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000682):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000682):
            return WrongItem()


#  	30000683 
class PickItem_30000683(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000683)
        add_effect_nif(spawnId=2002, nifPath='Map/Orient/Field/or_fi_prop_ship_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000683()


class DetectItem_30000683(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000683):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000683):
            return WrongItem()


#  	30000684 
class PickItem_30000684(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000684)
        add_effect_nif(spawnId=2002, nifPath='Map/Ludibrium/Field/lu_fi_prop_rocket_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000684()


class DetectItem_30000684(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000684):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000684):
            return WrongItem()


#  	30000685 
class PickItem_30000685(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000685)
        add_effect_nif(spawnId=2002, nifPath='Map/Lith/Field/li_fi_prop_anchor_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000685()


class DetectItem_30000685(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000685):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000685):
            return WrongItem()


#  	30000686 
class PickItem_30000686(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000686)
        add_effect_nif(spawnId=2002, nifPath='Map/Lith/Field/li_fi_prop_tube_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000686()


class DetectItem_30000686(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000686):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000686):
            return WrongItem()


#  	30000687 
class PickItem_30000687(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000687)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_beanbag_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000687()


class DetectItem_30000687(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000687):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000687):
            return WrongItem()


#  	30000688 
class PickItem_30000688(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000688)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_surgerylamp_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000688()


class DetectItem_30000688(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000688):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000688):
            return WrongItem()


#  	30000689 
class PickItem_30000689(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000689)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_surgery_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000689()


class DetectItem_30000689(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000689):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000689):
            return WrongItem()


#  	30000690 
class PickItem_30000690(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000690)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_sofa_D01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000690()


class DetectItem_30000690(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000690):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000690):
            return WrongItem()


#  	30000691 
class PickItem_30000691(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000691)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_paintbag_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000691()


class DetectItem_30000691(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000691):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000691):
            return WrongItem()


#  	30000692 
class PickItem_30000692(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000692)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_dresser_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000692()


class DetectItem_30000692(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000692):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000692):
            return WrongItem()


#  	30000693 
class PickItem_30000693(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000693)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_massage_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000693()


class DetectItem_30000693(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000693):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000693):
            return WrongItem()


#  	30000694 
class PickItem_30000694(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000694)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Indoor/ke_in_prop_catower_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000694()


class DetectItem_30000694(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000694):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000694):
            return WrongItem()


#  	30000695 
class PickItem_30000695(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000695)
        add_effect_nif(spawnId=2002, nifPath='Npc/Etc/UGC_SportsCar_Npc/UGC_SportsCar_Npc_02.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000695()


class DetectItem_30000695(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000695):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000695):
            return WrongItem()


#  	30000696 
class PickItem_30000696(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000696)
        add_effect_nif(spawnId=2002, nifPath='Npc/Etc/UGC_F1RacingCar/UGC_F1RacingCar_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000696()


class DetectItem_30000696(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000696):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000696):
            return WrongItem()


#  	30000697 
class PickItem_30000697(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000697)
        add_effect_nif(spawnId=2002, nifPath='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000697()


class DetectItem_30000697(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000697):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000697):
            return WrongItem()


#  	30000698 
class PickItem_30000698(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000698)
        add_effect_nif(spawnId=2002, nifPath='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000698()


class DetectItem_30000698(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000698):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000698):
            return WrongItem()


#  	30000699 
class PickItem_30000699(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000699)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Field/co_fi_prop_tent_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000699()


class DetectItem_30000699(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000699):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000699):
            return WrongItem()


#  	30000700 
class PickItem_30000700(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000700)
        add_effect_nif(spawnId=2002, nifPath='Map/Royalcity/Indoor/ry_in_prop_djtable_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000700()


class DetectItem_30000700(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000700):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000700):
            return WrongItem()


#  	30000701 
class PickItem_30000701(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000701)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Indoor/co_in_prop_security_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000701()


class DetectItem_30000701(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000701):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000701):
            return WrongItem()


#  	30000702 
class PickItem_30000702(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000702)
        add_effect_nif(spawnId=2002, nifPath='Map/Tria/Indoor/tr_in_prop_workit_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000702()


class DetectItem_30000702(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000702):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000702):
            return WrongItem()


#  	30000703 
class PickItem_30000703(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000703)
        add_effect_nif(spawnId=2002, nifPath='Map/Steampunk/Field/sp_fi_prop_anvil_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Steampunk/Field/sp_fi_prop_bellows_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

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
        add_effect_nif(spawnId=2002, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_C01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000705()


class DetectItem_30000705(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000705):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000705):
            return WrongItem()


#  	30000706 
class PickItem_30000706(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000706)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Indoor/co_in_prop_icebox_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000706()


class DetectItem_30000706(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000706):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000706):
            return WrongItem()


#  	30000707 
class PickItem_30000707(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000707)
        add_effect_nif(spawnId=2002, nifPath='Map/Henesys/Indoor/he_in_prop_cushiona_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000707()


class DetectItem_30000707(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000707):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000707):
            return WrongItem()


#  	30000708 
class PickItem_30000708(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000708)
        add_effect_nif(spawnId=2002, nifPath='Effect/BG/Liftup/co_liftup_piano_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000708()


class DetectItem_30000708(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000708):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000708):
            return WrongItem()


#  	30000709 
class PickItem_30000709(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000709)
        add_effect_nif(spawnId=2002, nifPath='Effect/BG/Liftup/co_liftup_vibraphone_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000709()


class DetectItem_30000709(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000709):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000709):
            return WrongItem()


#  	30000710 
class PickItem_30000710(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000710)
        add_effect_nif(spawnId=2002, nifPath='Map/Common/Indoor/co_in_prop_camera_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000710()


class DetectItem_30000710(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000710):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000710):
            return WrongItem()


#  	30000711 
class PickItem_30000711(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000711)
        add_effect_nif(spawnId=2002, nifPath='Map/UGC/Indoor/ugc_in_funct_workstone_G01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000711()


class DetectItem_30000711(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000711):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000711):
            return WrongItem()


#  	30000712 
class PickItem_30000712(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000712)
        add_effect_nif(spawnId=2002, nifPath='Map/Orient/Indoor/or_in_prop_incense_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000712()


class DetectItem_30000712(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000712):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000712):
            return WrongItem()


#  	30000713 
class PickItem_30000713(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000713)
        add_effect_nif(spawnId=2002, nifPath='Map/Steampunk/Indoor/sp_in_prop_desk_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000713()


class DetectItem_30000713(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000713):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000713):
            return WrongItem()


#  	30000714 
class PickItem_30000714(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000714)
        add_effect_nif(spawnId=2002, nifPath='Map/SF/Field/sf_fi_prop_incubator_D01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000714()


class DetectItem_30000714(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000714):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000714):
            return WrongItem()


#  	30000715 
class PickItem_30000715(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000715)
        add_effect_nif(spawnId=2002, nifPath='Map/Steampunk/Field/sp_fi_prop_brazier_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000715()


class DetectItem_30000715(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000715):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000715):
            return WrongItem()


#  	30000716 
class PickItem_30000716(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=True) # DownArrow
        set_user_value(key='ItemNumber', value=30000716)
        add_effect_nif(spawnId=2002, nifPath='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000716()


class DetectItem_30000716(state.State):
    def on_tick(self) -> state.State:
        if detect_liftable_object(boxIds=[9202], itemId=30000716):
            return RightItem()
        if not detect_liftable_object(boxIds=[9202], itemId=30000716):
            return WrongItem()


#  미션 성공 
class RightItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        remove_effect_nif(spawnId=2002)
        set_conversation(type=1, spawnId=2002, script='$02000387_BF__2002_CUSTOMER__0$', arg4=3, arg5=0)
        add_buff(boxIds=[9900], skillId=70000112, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CustomerLeave()


class CustomerLeave(state.State):
    def on_enter(self):
        move_npc(spawnId=2002, patrolName='MS2PatrolData_222')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9302, spawnIds=[2002]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Wait()


#  잘못된 아이템을 내려놓으면 
class WrongItem(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        remove_effect_nif(spawnId=2002)
        set_conversation(type=1, spawnId=2002, script='$02000387_BF__2002_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return WrongItemReturn()


class WrongItemReturn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='ItemNumber', value=30000617):
            return PickItem_30000617()
        if user_value(key='ItemNumber', value=30000618):
            return PickItem_30000618()
        if user_value(key='ItemNumber', value=30000619):
            return PickItem_30000619()
        if user_value(key='ItemNumber', value=30000620):
            return PickItem_30000620()
        if user_value(key='ItemNumber', value=30000621):
            return PickItem_30000621()
        if user_value(key='ItemNumber', value=30000622):
            return PickItem_30000622()
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
        if user_value(key='ItemNumber', value=30000628):
            return PickItem_30000628()
        if user_value(key='ItemNumber', value=30000629):
            return PickItem_30000629()
        if user_value(key='ItemNumber', value=30000630):
            return PickItem_30000630()
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
        if user_value(key='ItemNumber', value=30000639):
            return PickItem_30000639()
        if user_value(key='ItemNumber', value=30000640):
            return PickItem_30000640()
        if user_value(key='ItemNumber', value=30000641):
            return PickItem_30000641()
        if user_value(key='ItemNumber', value=30000642):
            return PickItem_30000642()
        if user_value(key='ItemNumber', value=30000643):
            return PickItem_30000643()
        if user_value(key='ItemNumber', value=30000644):
            return PickItem_30000644()
        if user_value(key='ItemNumber', value=30000645):
            return PickItem_30000645()
        if user_value(key='ItemNumber', value=30000646):
            return PickItem_30000646()
        if user_value(key='ItemNumber', value=30000647):
            return PickItem_30000647()
        if user_value(key='ItemNumber', value=30000648):
            return PickItem_30000648()
        if user_value(key='ItemNumber', value=30000649):
            return PickItem_30000649()
        if user_value(key='ItemNumber', value=30000650):
            return PickItem_30000650()
        if user_value(key='ItemNumber', value=30000651):
            return PickItem_30000651()
        if user_value(key='ItemNumber', value=30000652):
            return PickItem_30000652()
        if user_value(key='ItemNumber', value=30000653):
            return PickItem_30000653()
        if user_value(key='ItemNumber', value=30000654):
            return PickItem_30000654()
        if user_value(key='ItemNumber', value=30000655):
            return PickItem_30000655()
        if user_value(key='ItemNumber', value=30000656):
            return PickItem_30000656()
        if user_value(key='ItemNumber', value=30000657):
            return PickItem_30000657()
        if user_value(key='ItemNumber', value=30000658):
            return PickItem_30000658()
        if user_value(key='ItemNumber', value=30000659):
            return PickItem_30000659()
        if user_value(key='ItemNumber', value=30000660):
            return PickItem_30000660()
        if user_value(key='ItemNumber', value=30000661):
            return PickItem_30000661()
        if user_value(key='ItemNumber', value=30000662):
            return PickItem_30000662()
        if user_value(key='ItemNumber', value=30000663):
            return PickItem_30000663()
        if user_value(key='ItemNumber', value=30000664):
            return PickItem_30000664()
        if user_value(key='ItemNumber', value=30000665):
            return PickItem_30000665()
        if user_value(key='ItemNumber', value=30000666):
            return PickItem_30000666()
        if user_value(key='ItemNumber', value=30000667):
            return PickItem_30000667()
        if user_value(key='ItemNumber', value=30000668):
            return PickItem_30000668()
        if user_value(key='ItemNumber', value=30000669):
            return PickItem_30000669()
        if user_value(key='ItemNumber', value=30000670):
            return PickItem_30000670()
        if user_value(key='ItemNumber', value=30000671):
            return PickItem_30000671()
        if user_value(key='ItemNumber', value=30000672):
            return PickItem_30000672()
        if user_value(key='ItemNumber', value=30000673):
            return PickItem_30000673()
        if user_value(key='ItemNumber', value=30000674):
            return PickItem_30000674()
        if user_value(key='ItemNumber', value=30000675):
            return PickItem_30000675()
        if user_value(key='ItemNumber', value=30000676):
            return PickItem_30000676()
        if user_value(key='ItemNumber', value=30000677):
            return PickItem_30000677()
        if user_value(key='ItemNumber', value=30000678):
            return PickItem_30000678()
        if user_value(key='ItemNumber', value=30000679):
            return PickItem_30000679()
        if user_value(key='ItemNumber', value=30000680):
            return PickItem_30000680()
        if user_value(key='ItemNumber', value=30000681):
            return PickItem_30000681()
        if user_value(key='ItemNumber', value=30000682):
            return PickItem_30000682()
        if user_value(key='ItemNumber', value=30000683):
            return PickItem_30000683()
        if user_value(key='ItemNumber', value=30000684):
            return PickItem_30000684()
        if user_value(key='ItemNumber', value=30000685):
            return PickItem_30000685()
        if user_value(key='ItemNumber', value=30000686):
            return PickItem_30000686()
        if user_value(key='ItemNumber', value=30000687):
            return PickItem_30000687()
        if user_value(key='ItemNumber', value=30000688):
            return PickItem_30000688()
        if user_value(key='ItemNumber', value=30000689):
            return PickItem_30000689()
        if user_value(key='ItemNumber', value=30000690):
            return PickItem_30000690()
        if user_value(key='ItemNumber', value=30000691):
            return PickItem_30000691()
        if user_value(key='ItemNumber', value=30000692):
            return PickItem_30000692()
        if user_value(key='ItemNumber', value=30000693):
            return PickItem_30000693()
        if user_value(key='ItemNumber', value=30000694):
            return PickItem_30000694()
        if user_value(key='ItemNumber', value=30000695):
            return PickItem_30000695()
        if user_value(key='ItemNumber', value=30000696):
            return PickItem_30000696()
        if user_value(key='ItemNumber', value=30000697):
            return PickItem_30000697()
        if user_value(key='ItemNumber', value=30000698):
            return PickItem_30000698()
        if user_value(key='ItemNumber', value=30000699):
            return PickItem_30000699()
        if user_value(key='ItemNumber', value=30000700):
            return PickItem_30000700()
        if user_value(key='ItemNumber', value=30000701):
            return PickItem_30000701()
        if user_value(key='ItemNumber', value=30000702):
            return PickItem_30000702()
        if user_value(key='ItemNumber', value=30000703):
            return PickItem_30000703()
        if user_value(key='ItemNumber', value=30000704):
            return PickItem_30000704()
        if user_value(key='ItemNumber', value=30000705):
            return PickItem_30000705()
        if user_value(key='ItemNumber', value=30000706):
            return PickItem_30000706()
        if user_value(key='ItemNumber', value=30000707):
            return PickItem_30000707()
        if user_value(key='ItemNumber', value=30000708):
            return PickItem_30000708()
        if user_value(key='ItemNumber', value=30000709):
            return PickItem_30000709()
        if user_value(key='ItemNumber', value=30000710):
            return PickItem_30000710()
        if user_value(key='ItemNumber', value=30000711):
            return PickItem_30000711()
        if user_value(key='ItemNumber', value=30000712):
            return PickItem_30000712()
        if user_value(key='ItemNumber', value=30000713):
            return PickItem_30000713()
        if user_value(key='ItemNumber', value=30000714):
            return PickItem_30000714()
        if user_value(key='ItemNumber', value=30000715):
            return PickItem_30000715()
        if user_value(key='ItemNumber', value=30000716):
            return PickItem_30000716()


