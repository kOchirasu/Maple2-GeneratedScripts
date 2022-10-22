""" trigger/52000038_qd/main.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20020010)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002632], questStates=[3]):
            set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002632], questStates=[2]):
            set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            create_monster(spawnIds=[131,132], arg2=True)
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[3]):
            set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            create_monster(spawnIds=[131,132], arg2=True)
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[2]):
            set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
            set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
            create_monster(spawnIds=[131,132], arg2=True)
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[1]):
            create_monster(spawnIds=[121,122], arg2=True)
            return scene_b_02()
        if quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[3]):
            return scene_b_01()
        if quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[2]):
            return scene_b_01()
        if quest_user_detected(boxIds=[701], questIds=[40002630], questStates=[1]):
            return ready_02()


class ready_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002630], questStates=[1]):
            return start()


class start(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__0$', arg4=2, arg5=0)
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')
        set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__1$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return start_03()


class start_03(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_2003')
        set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_04()


class start_04(state.State):
    def on_enter(self):
        move_npc(spawnId=102, patrolName='MS2PatrolData_2004')
        set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return start_05()


class start_05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start_05_b()


class start_05_b(state.State):
    def on_enter(self):
        set_actor(triggerId=3001, visible=False, initialSequence='Dead_A')
        move_npc(spawnId=101, patrolName='MS2PatrolData_2005')
        set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__4$', arg4=2, arg5=0)
        move_npc(spawnId=102, patrolName='MS2PatrolData_2006')
        set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__5$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return start_06()


class start_06(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)
        create_monster(spawnIds=[203], arg2=True)
        create_monster(spawnIds=[204], arg2=True)
        create_monster(spawnIds=[205], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return start_07()


class start_07(state.State):
    def on_enter(self):
        set_actor(triggerId=3002, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=3003, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=3004, visible=False, initialSequence='Dead_A')
        set_actor(triggerId=3005, visible=False, initialSequence='Dead_A')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2007')
        set_conversation(type=1, spawnId=101, script='$52000038_QD__MAIN__6$', arg4=2, arg5=2)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2008')
        set_conversation(type=1, spawnId=102, script='$52000038_QD__MAIN__7$', arg4=2, arg5=4)
        show_guide_summary(entityId=40010, textId=40010)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205]):
            destroy_monster(spawnIds=[101,102])
            hide_guide_summary(entityId=40010)
            return scene_b_01()


class scene_b_01(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='beyondroid1')
        create_monster(spawnIds=[111,112], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[1]):
            destroy_monster(spawnIds=[111,112])
            create_monster(spawnIds=[121,122], arg2=True)
            return scene_b_02()


class scene_b_02(state.State):
    def on_enter(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2009')
        set_conversation(type=1, spawnId=121, script='$52000038_QD__MAIN__8$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return scene_b_03()


class scene_b_03(state.State):
    def on_enter(self):
        move_npc(spawnId=122, patrolName='MS2PatrolData_2010')
        set_conversation(type=1, spawnId=122, script='$52000038_QD__MAIN__9$', arg4=2, arg5=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return scene_b_04()


class scene_b_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True)
        show_guide_summary(entityId=20020010, textId=20020010)
        set_conversation(type=1, spawnId=121, script='$52000038_QD__MAIN__10$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002631], questStates=[2]):
            destroy_monster(spawnIds=[121,122])
            create_monster(spawnIds=[131,132], arg2=True)
            hide_guide_summary(entityId=20020010)
            return scene_c_01()


class scene_c_01(state.State):
    pass


