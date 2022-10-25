""" trigger/02000387_bf/1109_customer.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001099], state=0) # Greeting
        self.set_user_value(key='CustomerEnter', value=0)
        self.set_user_value(key='ItemNumber', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CustomerEnter', value=1):
            return CustomerEnterDelay(self.ctx)


class CustomerEnterDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return CustomerEnter(self.ctx)


class CustomerEnter(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1109], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9110, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9111, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1109, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9112, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1109, patrolName='MS2PatrolData_102')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9113, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1109, patrolName='MS2PatrolData_103')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9113, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9113, spawnIds=[1109]):
            return WaitGreeting(self.ctx)


class WaitGreeting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001099], state=1) # Greeting

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001099], stateValue=0):
            return OrderRandomPick(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001099], state=2) # Greeting


# 고객 주문 랜덤
class OrderRandomPick(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return PickItem_30000641(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000647(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000648(self.ctx)
        if self.random_condition(rate=1):
            return PickItem_30000711(self.ctx)


# 30000641
class PickItem_30000641(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000641)
        self.add_effect_nif(spawnId=1109, nifPath='Map/Henesys/Indoor/he_in_prop_kettle_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000641(self.ctx)


class DetectItem_30000641(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000641):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000641):
            return WrongItem(self.ctx)


# 30000647
class PickItem_30000647(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000647)
        self.add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_B01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000647(self.ctx)


class DetectItem_30000647(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000647):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000647):
            return WrongItem(self.ctx)


# 30000648
class PickItem_30000648(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000648)
        self.add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_alchemy_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000648(self.ctx)


class DetectItem_30000648(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000648):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000648):
            return WrongItem(self.ctx)


# 30000711
class PickItem_30000711(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000711)
        self.add_effect_nif(spawnId=1109, nifPath='Map/UGC/Indoor/ugc_in_funct_workstone_G01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=0):
            return DetectItem_30000711(self.ctx)


class DetectItem_30000711(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9201], itemId=30000711):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9201], itemId=30000711):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=1109)
        self.set_conversation(type=1, spawnId=1109, script='$02000387_BF__1109_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1109, patrolName='MS2PatrolData_111')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9301, spawnIds=[1109]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1109])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5101], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=1109)
        self.set_conversation(type=1, spawnId=1109, script='$02000387_BF__1109_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ItemNumber', value=30000641):
            return PickItem_30000641(self.ctx)
        if self.user_value(key='ItemNumber', value=30000647):
            return PickItem_30000647(self.ctx)
        if self.user_value(key='ItemNumber', value=30000648):
            return PickItem_30000648(self.ctx)
        if self.user_value(key='ItemNumber', value=30000711):
            return PickItem_30000711(self.ctx)


initial_state = Wait
