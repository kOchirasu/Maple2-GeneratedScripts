""" trigger/52000039_qd/main.xml """
import trigger_api


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.hide_guide_summary(entityId=20020030)
        self.hide_guide_summary(entityId=20020031)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[3]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[2]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003054], questStates=[1]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[3]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[2]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003053], questStates=[1]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[3]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[2]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003052], questStates=[1]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[3]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[2]):
            return NextMapPortalOpen(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003051], questStates=[1]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return PCPatrol01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[3]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[3]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_b_07(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[2]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_b_07(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[1]):
            return ready_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[2]):
            self.create_monster(spawnIds=[101], animationEffect=True)
            return scene_b_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002633], questStates=[3]):
            self.create_monster(spawnIds=[101], animationEffect=True)
            return scene_b_01(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[1]):
            self.create_monster(spawnIds=[101], animationEffect=True)
            self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
            self.create_monster(spawnIds=[122], animationEffect=True)
            return scene_b_02(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[2]):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)
        if self.user_detected(boxIds=[701], jobCode=110):
            self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
            self.set_mesh(triggerIds=[6001], visible=False)
            self.set_mesh(triggerIds=[6010], visible=False)
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            return scene_c_01(self.ctx)


class ready_02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203], animationEffect=False)
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[702], questIds=[40002633], questStates=[1]):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=7001, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_2001')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_2002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return start_02(self.ctx)


class start_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_conversation(type=2, spawnId=11001546, script='$52000039_QD__MAIN__0$', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_cinematic_ui(type=0)
            self.set_cinematic_ui(type=2)
            self.select_camera(triggerId=7001, enable=False)
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20020030, textId=20020030)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201,202,203]):
            self.destroy_monster(spawnIds=[102])
            self.hide_guide_summary(entityId=20020030)
            return scene_b_01(self.ctx)


class scene_b_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=701, type='trigger', achieve='beyondroid2')
        self.create_monster(spawnIds=[112], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002634], questStates=[1]):
            self.destroy_monster(spawnIds=[112])
            self.create_monster(spawnIds=[122], animationEffect=True)
            return scene_b_02(self.ctx)


class scene_b_02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2004')
        self.set_conversation(type=1, spawnId=122, script='$52000039_QD__MAIN__1$', arg4=3, arg5=0)
        self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
        self.set_mesh(triggerIds=[6001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=703, spawnIds=[122]):
            self.set_cinematic_ui(type=1)
            self.set_cinematic_ui(type=3)
            self.select_camera(triggerId=7002, enable=True)
            self.move_user(mapId=52000039, portalId=3)
            self.set_mesh(triggerIds=[6010], visible=False)
            return scene_b_03(self.ctx)


class scene_b_03(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2006')
        self.set_conversation(type=2, spawnId=11001546, script='$52000039_QD__MAIN__2$', arg4=3)
        self.set_actor(triggerId=3010, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_b_04(self.ctx)


class scene_b_04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=7003, enable=True)
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2008')
        self.set_conversation(type=1, spawnId=122, script='$52000039_QD__MAIN__3$', arg4=3)
        self.set_actor(triggerId=3010, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_b_05(self.ctx)


class scene_b_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3010, visible=True, initialSequence='Attack_01_D')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=650):
            return scene_b_06(self.ctx)


class scene_b_06(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=4)
        self.move_npc(spawnId=122, patrolName='MS2PatrolData_2010')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
            self.create_monster(spawnIds=[210], animationEffect=True)
            return scene_b_07(self.ctx)


class scene_b_07(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20020031, textId=20020031)
        self.select_camera(triggerId=7003, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[210]):
            self.hide_guide_summary(entityId=20020031)
            self.set_achievement(triggerId=701, type='trigger', achieve='beyondguard')
            self.destroy_monster(spawnIds=[101,122])
            return scene_b_08(self.ctx)


class scene_b_08(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111,132], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return scene_b_09(self.ctx)


class scene_b_09(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__4$', arg4=3)
        self.set_npc_emotion_loop(spawnId=132, sequenceName='Sit_Down_A', duration=3000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Sit_Down_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_b_10(self.ctx)


class scene_b_10(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__5$', arg4=3)
        self.set_npc_emotion_loop(spawnId=132, sequenceName='Stun_A', duration=3000)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Stun_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[40002635], questStates=[1]):
            return scene_c_01(self.ctx)


class scene_c_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=132, script='$52000039_QD__MAIN__6$', arg4=3)
        self.move_npc(spawnId=132, patrolName='MS2PatrolData_2012')
        self.move_npc(spawnId=111, patrolName='MS2PatrolData_2011')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_c_02(self.ctx)


class scene_c_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.destroy_monster(spawnIds=[132,111])


# 비욘드 링크 중앙 컴퓨터실 포탈 열림
class NextMapPortalOpen(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=3001, visible=True, initialSequence='sf_fi_funct_door_A01_Opened')
        self.set_mesh(triggerIds=[6001], visible=False)
        self.set_mesh(triggerIds=[6010], visible=False)
        self.set_actor(triggerId=3010, visible=False, initialSequence='Idle_A')
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


# 흑성회 본부 지하 밀실 이동
class PCPatrol01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCPatrol02(self.ctx)


class PCPatrol02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCPatrol03(self.ctx)


class PCPatrol03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Bore_C'])
        self.set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__7$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)
        self.set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__8$', arg4=2, arg5=0)
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1002')
        self.set_conversation(type=1, spawnId=0, script='$52000039_QD__MAIN__9$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1600):
            return PCFainted01(self.ctx)


class PCFainted01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2667):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000045, portalId=2, boxId=701)
        self.select_camera(triggerId=502, enable=False)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
