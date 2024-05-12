""" trigger/52000044_qd/10003040.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000390], state=0)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.create_monster(spawnIds=[1001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[1]):
            self.destroy_monster(spawnIds=[1001])
            self.create_monster(spawnIds=[1003], animationEffect=False)
            return 오브젝트반응대기(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[3]):
            self.destroy_monster(spawnIds=[1001])
            self.create_monster(spawnIds=[1003], animationEffect=False)
            return 오브젝트반응조건(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[2]):
            self.destroy_monster(spawnIds=[1001])
            self.create_monster(spawnIds=[1003], animationEffect=False)
            return 오브젝트반응조건(self.ctx)
        if self.quest_user_detected(boxIds=[103], questIds=[10003041], questStates=[1]):
            return 연출시작02(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[1]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=301, enable=True)
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.set_effect(triggerIds=[602], visible=True)
        self.create_monster(spawnIds=[2001,2002,2003,2004,2005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 말풍선대사01(self.ctx)


class 연출시작02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[1001])
        self.create_monster(spawnIds=[1002], animationEffect=False)
        self.set_effect(triggerIds=[602], visible=True)
        self.create_monster(spawnIds=[2001,2002,2003,2004,2005], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 차전투시작1(self.ctx)


class 말풍선대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=2001, script='$52000044_QD__10003040__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 말풍선대사02(self.ctx)


class 말풍선대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2001, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')
        self.move_npc(spawnId=2003, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData_2005')
        self.set_conversation(type=1, spawnId=2003, script='$52000044_QD__10003040__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 제이시대사01(self.ctx)


class 제이시대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000515, script='$52000044_QD__10003040__2$', arg4=2)
        self.set_skip(state=제이시대사01스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 제이시대사02(self.ctx)


class 제이시대사01스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 제이시대사02(self.ctx)


class 제이시대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_conversation(type=2, spawnId=11000515, script='$52000044_QD__10003040__3$', arg4=4)
        self.set_skip(state=제이시대사02스킵)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 제이시대사02스킵(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=302, enable=False)
        self.set_effect(triggerIds=[601], visible=False)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 차전투시작1(self.ctx)


class 차전투시작1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=25200441, textId=25200441, duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001,2002,2003,2004,2005]):
            self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')
            return 차전투시작2(self.ctx)


class 차전투시작2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2006], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2006]):
            self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')
            return NPC감지대기(self.ctx)


class NPC감지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=102, spawnIds=[1002]):
            self.set_achievement(triggerId=199, type='trigger', achieve='EscapewithJacy')
            self.destroy_monster(spawnIds=[1002])
            self.create_monster(spawnIds=[1003], animationEffect=False)
            return 오브젝트반응조건(self.ctx)


class 오브젝트반응조건(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[1]):
            return 오브젝트반응대기(self.ctx)


class 오브젝트반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10000390], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000390], stateValue=0):
            self.move_user(mapId=52000045, portalId=1)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
