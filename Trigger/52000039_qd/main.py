""" trigger/52000039_qd/main.xml """
from common import *
import state


class ready(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        hide_guide_summary(entityId=20020030)
        hide_guide_summary(entityId=20020031)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[3]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[2]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[1]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[3]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[3]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[2]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[1]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[3]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[2]):
            return NextMapPortalOpen()
        if quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[1]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return PCPatrol01()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[3]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[3]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_b_07()
        if quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[2]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_b_07()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()
        if quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[1]):
            return ready_02()
        if quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[2]):
            create_monster(spawnIds=[101], arg2=True)
            return scene_b_01()
        if quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[3]):
            create_monster(spawnIds=[101], arg2=True)
            return scene_b_01()
        if quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[1]):
            create_monster(spawnIds=[101], arg2=True)
            move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
            create_monster(spawnIds=[122], arg2=True)
            return scene_b_02()
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()
        if user_detected(boxIds=[701], jobCode=110):
            set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            set_mesh(triggerIds=[6001], visible=False)
            set_mesh(triggerIds=[6010], visible=False)
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01()


class ready_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203], arg2=False)
        create_monster(spawnIds=[101,102], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[40002633], questStates=[1]):
            return start()


class start(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=7001, enable=True)
        move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return start_02()


class start_02(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_conversation(type=2, spawnId=11001546, script='$52000039_QD__MAIN__0$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            select_camera(triggerId=7001, enable=False)
            return start_03()


class start_03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20020030, textId=20020030)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203]):
            destroy_monster(spawnIds=[102])
            hide_guide_summary(entityId=20020030)
            return scene_b_01()


class scene_b_01(state.State):
    def on_enter(self):
        set_achievement(triggerId=701, type='trigger', achieve='beyondroid2')
        create_monster(spawnIds=[112], arg2=True)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[1]):
            destroy_monster(spawnIds=[112])
            create_monster(spawnIds=[122], arg2=True)
            return scene_b_02()


class scene_b_02(state.State):
    def on_enter(self):
        move_npc(spawnId=122, patrolName='MS2PatrolData_2004')
        set_conversation(type=1, spawnId=122, script='$52000039_QD__MAIN__1$', arg4=3, arg5=0)
        set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
        set_mesh(triggerIds=[6001], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=703, spawnIds=[122]):
            set_cinematic_ui(type=1)
            set_cinematic_ui(type=3)
            select_camera(triggerId=7002, enable=True)
            move_user(mapId=52000039, portalId=3)
            set_mesh(triggerIds=[6010], visible=False)
            return scene_b_03()


class scene_b_03(state.State):
    def on_enter(self):
        move_npc(spawnId=122, patrolName='MS2PatrolData_2006')
        set_conversation(type=2, spawnId=11001546, script='$52000039_QD__MAIN__2$', arg4=3)
        set_actor(triggerId=3010, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_b_04()


class scene_b_04(state.State):
    def on_enter(self):
        select_camera(triggerId=7003, enable=True)
        move_npc(spawnId=122, patrolName='MS2PatrolData_2008')
        set_conversation(type=1, spawnId=122, script='$52000039_QD__MAIN__3$', arg4=3)
        set_actor(triggerId=3010, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_b_05()


class scene_b_05(state.State):
    def on_enter(self):
        set_actor(triggerId=3010, visible=True, initialSequence='Attack_01_D')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=650):
            return scene_b_06()


class scene_b_06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=4)
        move_npc(spawnId=122, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            create_monster(spawnIds=[210], arg2=True)
            return scene_b_07()


class scene_b_07(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20020031, textId=20020031)
        select_camera(triggerId=7003, enable=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[210]):
            hide_guide_summary(entityId=20020031)
            set_achievement(triggerId=701, type='trigger', achieve='beyondguard')
            destroy_monster(spawnIds=[101,122])
            return scene_b_08()


class scene_b_08(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,132], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return scene_b_09()


class scene_b_09(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__4$', arg4=3)
        set_npc_emotion_loop(spawnId=132, sequenceName='Sit_Down_A', duration=3000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Sit_Down_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return scene_b_10()


class scene_b_10(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__5$', arg4=3)
        set_npc_emotion_loop(spawnId=132, sequenceName='Stun_A', duration=3000)
        set_npc_emotion_loop(spawnId=111, sequenceName='Stun_A', duration=3000)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            return scene_c_01()


class scene_c_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__6$', arg4=3)
        move_npc(spawnId=132, patrolName='MS2PatrolData_2012')
        move_npc(spawnId=111, patrolName='MS2PatrolData_2011')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_c_02()


class scene_c_02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[132,111])


#  비욘드 링크 중앙 컴퓨터실 포탈 열림 
class NextMapPortalOpen(state.State):
    def on_enter(self):
        set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
        set_mesh(triggerIds=[6001], visible=False)
        set_mesh(triggerIds=[6010], visible=False)
        set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


#  흑성회 본부 지하 밀실 이동 
class PCPatrol01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCPatrol02()


class PCPatrol02(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCPatrol03()


class PCPatrol03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Bore_C'])
        set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__8$', arg4=2, arg5=0)
        move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LookAround03()


class LookAround03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1002')
        set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__9$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1600):
            return PCFainted01()


class PCFainted01(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2667):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTeleport02()


class PCTeleport02(state.State):
    def on_enter(self):
        move_user(mapId=52000045, portalId=2, boxId=701)
        select_camera(triggerId=502, enable=False)

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


