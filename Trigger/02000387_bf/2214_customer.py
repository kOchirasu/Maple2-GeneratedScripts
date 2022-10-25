""" trigger/02000387_bf/2214_customer.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001089], state=0) # Greeting
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
        self.create_monster(spawnIds=[2214], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9120, spawnIds=[0]):
            return Patrol03(self.ctx)
        if not self.npc_detected(boxId=9121, spawnIds=[0]):
            return Patrol01(self.ctx)


class Patrol01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2214, patrolName='MS2PatrolData_201')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9122, spawnIds=[0]):
            return Patrol02Delay(self.ctx)


class Patrol02Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol02(self.ctx)


class Patrol02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2214, patrolName='MS2PatrolData_202')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return Patrol03Delay(self.ctx)


class Patrol03Delay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Patrol03(self.ctx)


class Patrol03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2214, patrolName='MS2PatrolData_203')

    def on_tick(self) -> common.Trigger:
        if not self.npc_detected(boxId=9123, spawnIds=[0]):
            return PatrolEndDelay(self.ctx)


class PatrolEndDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return PatrolEnd(self.ctx)


class PatrolEnd(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9123, spawnIds=[2214]):
            return WaitGreeting(self.ctx)


class WaitGreeting(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001089], state=1) # Greeting

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10001089], stateValue=0):
            return PickItem_30000701(self.ctx)

    def on_exit(self):
        self.set_interact_object(triggerIds=[10001089], state=2) # Greeting


# 30000701
class PickItem_30000701(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=True) # DownArrow
        self.set_user_value(key='ItemNumber', value=30000701)
        self.add_effect_nif(spawnId=2214, nifPath='Map/Common/Indoor/co_in_prop_security_A01.nif', isOutline=True, scale=1.2, rotateZ=225)

    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=0):
            return DetectItem_30000701(self.ctx)


class DetectItem_30000701(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.detect_liftable_object(boxIds=[9202], itemId=30000701):
            return RightItem(self.ctx)
        if not self.detect_liftable_object(boxIds=[9202], itemId=30000701):
            return WrongItem(self.ctx)


# 미션 성공
class RightItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Right_01')
        self.remove_effect_nif(spawnId=2214)
        self.set_conversation(type=1, spawnId=2214, script='$02000387_BF__2214_CUSTOMER__0$', arg4=3, arg5=0)
        self.add_buff(boxIds=[9900], skillId=70000112, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return CustomerLeave(self.ctx)


class CustomerLeave(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2214, patrolName='MS2PatrolData_222')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=9302, spawnIds=[2214]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2214])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Wait(self.ctx)


# 잘못된 아이템을 내려놓으면
class WrongItem(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5102], visible=False) # DownArrow
        self.play_system_sound_in_box(boxIds=[9900], sound='System_PartTimeJob_Wrong_01')
        self.remove_effect_nif(spawnId=2214)
        self.set_conversation(type=1, spawnId=2214, script='$02000387_BF__2214_CUSTOMER__1$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return WrongItemReturn(self.ctx)


class WrongItemReturn(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ItemNumber', value=30000701):
            return PickItem_30000701(self.ctx)


initial_state = Wait
