""" trigger/52000044_qd/10003040.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000390], state=0)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        create_monster(spawnIds=[1001], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[1]):
            destroy_monster(spawnIds=[1001])
            create_monster(spawnIds=[1003], arg2=False)
            return 오브젝트반응대기()
        if quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[3]):
            destroy_monster(spawnIds=[1001])
            create_monster(spawnIds=[1003], arg2=False)
            return 오브젝트반응조건()
        if quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[2]):
            destroy_monster(spawnIds=[1001])
            create_monster(spawnIds=[1003], arg2=False)
            return 오브젝트반응조건()
        if quest_user_detected(boxIds=[103], questIds=[10003041], questStates=[1]):
            return 연출시작02()
        if quest_user_detected(boxIds=[199], questIds=[10003041], questStates=[1]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=301, enable=True)
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1002], arg2=False)
        set_effect(triggerIds=[602], visible=True)
        create_monster(spawnIds=[2001,2002,2003,2004,2005], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 말풍선대사01()


class 연출시작02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001])
        create_monster(spawnIds=[1002], arg2=False)
        set_effect(triggerIds=[602], visible=True)
        create_monster(spawnIds=[2001,2002,2003,2004,2005], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 차전투시작1()


class 말풍선대사01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2001, script='$52000044_QD__10003040__0$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 말풍선대사02()


class 말풍선대사02(state.State):
    def on_enter(self):
        move_npc(spawnId=2001, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=2002, patrolName='MS2PatrolData_2002')
        move_npc(spawnId=2003, patrolName='MS2PatrolData_2003')
        move_npc(spawnId=2004, patrolName='MS2PatrolData_2004')
        move_npc(spawnId=2005, patrolName='MS2PatrolData_2005')
        set_conversation(type=1, spawnId=2003, script='$52000044_QD__10003040__1$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 제이시대사01()


class 제이시대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000515, script='$52000044_QD__10003040__2$', arg4=2)
        set_skip(state=제이시대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 제이시대사02()


class 제이시대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 제이시대사02()


class 제이시대사02(state.State):
    def on_enter(self):
        select_camera(triggerId=302, enable=True)
        set_effect(triggerIds=[601], visible=True)
        set_conversation(type=2, spawnId=11000515, script='$52000044_QD__10003040__3$', arg4=4)
        set_skip(state=제이시대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 제이시대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=302, enable=False)
        set_effect(triggerIds=[601], visible=False)
        move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 차전투시작1()


class 차전투시작1(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200441, textId=25200441, duration=4000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001,2002,2003,2004,2005]):
            move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')
            return 차전투시작2()


class 차전투시작2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2006]):
            move_npc(spawnId=1002, patrolName='MS2PatrolData_1002C')
            return NPC감지대기()


class NPC감지대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1002]):
            set_achievement(triggerId=199, type='trigger', achieve='EscapewithJacy')
            destroy_monster(spawnIds=[1002])
            create_monster(spawnIds=[1003], arg2=False)
            return 오브젝트반응조건()


class 오브젝트반응조건(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[199], questIds=[10003042], questStates=[1]):
            return 오브젝트반응대기()


class 오브젝트반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000390], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000390], arg2=0):
            move_user(mapId=52000045, portalId=1)
            return 종료()


class 종료(state.State):
    pass


