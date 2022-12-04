""" trigger/52000037_qd/lookinto_soulbinder_12.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=False, initialSequence='Dead_A') # NelfActor
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000175], state=0) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출01조건(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[60100065], questStates=[3], jobCode=110):
            return NPC만배치(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class NPC만배치(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC
        self.set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 연출01조건(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=4000, visible=True, initialSequence='Dead_A') # NelfActor
        self.create_monster(spawnIds=[101], animationEffect=False) # NelfDummyNPC
        self.set_interact_object(triggerIds=[10000175], state=1) # Bag

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9300], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출01시작(self.ctx)


class 연출01시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000037, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            self.move_user_path(patrolName='MS2PatrolData_PC1101A')
            return PC말풍선01(self.ctx)


class PC말풍선01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC말풍선02(self.ctx)


class PC말풍선02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선04(self.ctx)


class PC말풍선04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선05(self.ctx)


class PC말풍선05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__4$', arg4=5, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 강제이동02조건(self.ctx)


class 강제이동02조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9301], questIds=[60100065], questStates=[2], jobCode=110):
            return PC말풍선07(self.ctx)


class PC말풍선07(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__LOOKINTO_SOULBINDER_12__5$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 강제이동02(self.ctx)


class 강제이동02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_PC1101B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9302], questIds=[60100065], questStates=[2], jobCode=110):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
