""" trigger/52000187_qd/tutorial.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2000], visible=True, arg3=0, arg4=0, arg5=0) # Invisible
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        create_widget(type='Guide')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90001]):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90002]):
            return 환영()


class 환영(state.State):
    def on_enter(self):
        set_quest_accept(questId=90000008)
        side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__0$')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[11000071], arg2=0):
            side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__1$')
            set_quest_complete(questId=90000008)
            return 머쉬킹대화1()


class 머쉬킹대화1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2000], visible=False, arg3=0, arg4=0, arg5=0) # Invisible
        create_monster(spawnIds=[103], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[1]):
            return 머쉬킹대화2()
        if quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[2]):
            return 머쉬킹대화2()
        if quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[3]):
            return 머쉬킹대화2()


class 머쉬킹대화2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001], visible=False, arg3=0, arg4=0, arg5=0) # Invisible

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90003]):
            side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__2$')
            move_npc(spawnId=103, patrolName='MS2PatrolData_lazy_1')
            return 머쉬킹대화3()


class 머쉬킹대화3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90004]):
            side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__3$')
            return 머쉬킹대화4()


class 머쉬킹대화4(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[90005]):
            return 모쿰소환()


class 모쿰소환(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__4$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 모쿰이동()


class 모쿰이동(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_0')
        add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__5$')
        side_npc_talk(npcId=29000403, illust='Mushking_normal', duration=4000, script='$52000187_QD__TUTORIAL__6$')
        add_buff(boxIds=[99999], skillId=71000077, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if widget_condition(type='Guide', name='IsTriggerEvent', condition='551'):
            create_monster(spawnIds=[101], arg2=False)
            return 모쿰대사1()


class 모쿰대사1(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_1')
        add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__7$')
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 해제()
        if wait_tick(waitTick=3000):
            return 모쿰대사2()


class 모쿰대사2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=102, msg='$52000187_QD__TUTORIAL__8$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 해제()
        if wait_tick(waitTick=3000):
            return 모쿰대사2()


class 해제(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_mokum_2')
        guide_event(eventId=560)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[99999], questIds=[90000007], questStates=[3]):
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            return None


class 종료(state.State):
    pass


