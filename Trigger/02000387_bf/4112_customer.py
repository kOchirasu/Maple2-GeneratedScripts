""" trigger/02000387_bf/4112_customer.xml """
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
        self.create_monster(spawnIds=[4112], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9140, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9141, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4112, patrolName='MS2PatrolData_401')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9142, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4112, patrolName='MS2PatrolData_402')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9143, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4112, patrolName='MS2PatrolData_403')

    def on_tick(self) -> trigger_api.Trigger:
        if not self.npc_detected(boxId=9143, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9143, spawnIds=[4112]):
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
            return PickItem_30000649(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000657(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000697(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000698(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000701(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000716(self.ctx)


# 30000649
class PickItem_30000649(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000649)
        self.add_effect_nif(spawnId=4112, nifPath='Map/Tria/Indoor/tr_in_prop_mirror_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000649(self.ctx)


class DetectItem_30000649(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000649):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000649):
            return WrongItem(self.ctx)


# 30000657
class PickItem_30000657(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000657)
        self.add_effect_nif(spawnId=4112, nifPath='Map/Iceland/Indoor/ic_in_prop_bed_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000657(self.ctx)


class DetectItem_30000657(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000657):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000657):
            return WrongItem(self.ctx)


# 30000697
class PickItem_30000697(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000697)
        self.add_effect_nif(spawnId=4112, nifPath='Npc/Etc/UGC_Poclain/UGC_Poclain_01.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000697(self.ctx)


class DetectItem_30000697(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000697):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000697):
            return WrongItem(self.ctx)


# 30000698
class PickItem_30000698(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000698)
        self.add_effect_nif(spawnId=4112, nifPath='Npc/Etc/UGC_FlameBike_Npc/UGC_FlameBike_03.nif', isOutline=True, scale=1.2, rotateZ=315)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000698(self.ctx)


class DetectItem_30000698(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000698):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000698):
            return WrongItem(self.ctx)


# 30000701
class PickItem_30000701(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000701)
        self.add_effect_nif(spawnId=4112, nifPath='Map/Common/Indoor/co_in_prop_security_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000701(self.ctx)


class DetectItem_30000701(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000701):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000701):
            return WrongItem(self.ctx)


# 30000716
class PickItem_30000716(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000716)
        self.add_effect_nif(spawnId=4112, nifPath='Map/Kerningcity/Field/ke_fi_prop_tire_A02.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=0):
            return DetectItem_30000716(self.ctx)


class DetectItem_30000716(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.detect_liftable_object(boxIds=[9204], itemId=30000716):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9204], itemId=30000716):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=4112)
        self.set_conversation(type=1, spawnId=4112, script='$02000387_BF__4112_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=4112, patrolName='MS2PatrolData_444')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9304, spawnIds=[4112]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[4112])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5104], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=4112)
        self.set_conversation(type=1, spawnId=4112, script='$02000387_BF__4112_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ItemNumber', value=30000649):
            return PickItem_30000649(self.ctx)
        if self.user_value(key='ItemNumber', value=30000657):
            return PickItem_30000657(self.ctx)
        if self.user_value(key='ItemNumber', value=30000697):
            return PickItem_30000697(self.ctx)
        if self.user_value(key='ItemNumber', value=30000698):
            return PickItem_30000698(self.ctx)
        if self.user_value(key='ItemNumber', value=30000701):
            return PickItem_30000701(self.ctx)
        if self.user_value(key='ItemNumber', value=30000716):
            return PickItem_30000716(self.ctx)


initial_state = Wait
