""" trigger/52100103_qd/main.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[700], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작체크(self.ctx)


class 연출시작체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[10000], questIds=[50100960], questStates=[2]):
            return 연출시작준비(self.ctx)


class 연출시작준비(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1], arg2=False)
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[700], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출NPC소환(self.ctx)


class 연출NPC소환(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52100103, portalId=3)
        self.create_monster(spawnIds=[1000], animationEffect=False)
        self.create_monster(spawnIds=[2000], animationEffect=False)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작암전1(self.ctx)


class 시작암전1(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100103, portalId=3)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=엔딩암전, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 클라디아대사1(self.ctx)


class 클라디아대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.select_camera_path(pathIds=[1000,1001], returnView=False)
        self.set_npc_emotion_loop(spawnId=2000, sequenceName='Bore_A', duration=1333)
        self.add_cinematic_talk(npcId=11004419, msg='$52100103_QD__MAIN__0$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네대사1(self.ctx)


class 마를레네대사1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')
        self.set_npc_emotion_loop(spawnId=1000, sequenceName='Talk_A', duration=1333)
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__1$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라흔들기(self.ctx)


class 카메라흔들기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[700], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네대사2(self.ctx)


class 마를레네대사2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[3], animationEffect=False)
        self.create_monster(spawnIds=[200], animationEffect=False)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.set_npc_rotation(spawnId=1000, rotation=-45)
        self.set_npc_rotation(spawnId=2000, rotation=45)
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__2$', duration=2000, align='left')
        self.add_cinematic_talk(npcId=11004419, msg='$52100103_QD__MAIN__3$', duration=2000, align='left')
        self.set_npc_emotion_loop(spawnId=3, sequenceName='Bore_A', duration=1333)
        self.select_camera(triggerId=100, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사1(self.ctx)


class 투르카대사1(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='PatrolData_PC_01')
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__4$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC돌아보기(self.ctx)


class PC돌아보기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=200, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 포탈오픈(self.ctx)


class 포탈오픈(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.select_camera(triggerId=1002, enable=True)
        self.create_monster(spawnIds=[300], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__5$', duration=3000, align='left')
        self.move_user(mapId=52100103, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카이동1(self.ctx)


class 투르카이동1(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=300, patrolName='PatrolData_Turka_1')
        self.move_npc(spawnId=200, patrolName='PatrolData_200_1')
        self.move_npc(spawnId=201, patrolName='PatrolData_201_1')
        self.move_npc(spawnId=202, patrolName='PatrolData_202_1')
        self.move_npc(spawnId=203, patrolName='PatrolData_203_1')
        self.select_camera(triggerId=1003, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC이동(self.ctx)


class PC이동(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1000], arg2=False)
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__6$', duration=3000, align='left')
        self.move_npc(spawnId=1001, patrolName='PatrolData_1001_1')
        self.move_npc(spawnId=300, patrolName='PatrolData_Turka_2')
        self.move_npc(spawnId=200, patrolName='PatrolData_200_2')
        self.move_npc(spawnId=201, patrolName='PatrolData_201_2')
        self.move_npc(spawnId=202, patrolName='PatrolData_202_2')
        self.move_npc(spawnId=203, patrolName='PatrolData_203_2')
        self.move_user_path(patrolName='PatrolData_PC_02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC말풍선대사(self.ctx)


class PC말풍선대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52100103_QD__MAIN__7$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC공격자세(self.ctx)


class PC공격자세(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=30000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사협박1(self.ctx)


class 투르카대사협박1(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_rotation(spawnId=202, rotation=45)
        self.set_npc_rotation(spawnId=201, rotation=-45)
        self.set_npc_rotation(spawnId=200, rotation=15)
        self.set_npc_rotation(spawnId=203, rotation=-15)
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__8$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네협박(self.ctx)


class 마를레네협박(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__9$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Talk_A', duration=1333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사협박2(self.ctx)


class 투르카대사협박2(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__10$', duration=6000, align='left')
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__11$', duration=2000, align='left')
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__12$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)
        self.destroy_monster(spawnIds=[2000], arg2=False)
        self.create_monster(spawnIds=[2001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아대사(self.ctx)


class 클라디아대사(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=2001, patrolName='PatrolData_2001_1')
        self.add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__13$', duration=2000, align='left')
        self.add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__14$', duration=3500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 마를레네대사(self.ctx)


class 마를레네대사(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__15$', duration=2000, align='left')
        self.set_npc_rotation(spawnId=1001, rotation=45)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아마를레네바라보기(self.ctx)


class 클라디아마를레네바라보기(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_rotation(spawnId=2001, rotation=-90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아대사2(self.ctx)


class 클라디아대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=2001, sequenceName='Talk_A', duration=1333)
        self.add_cinematic_talk(npcId=11004385, msg='$52100103_QD__MAIN__16$', duration=4000, align='left')
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__17$', duration=3000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사3(self.ctx)


class 투르카대사3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11004430, msg='$52100103_QD__MAIN__18$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=300, sequenceName='Bore_A', duration=1333)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클라디아퇴장(self.ctx)


class 클라디아퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=True)
        self.select_camera(triggerId=1004, enable=True)
        self.move_npc(spawnId=2001, patrolName='PatrolData_2001_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부하퇴장(self.ctx)


class 부하퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=200, patrolName='PatrolData_200_3')
        self.move_npc(spawnId=201, patrolName='PatrolData_201_3')
        self.move_npc(spawnId=202, patrolName='PatrolData_202_3')
        self.move_npc(spawnId=203, patrolName='PatrolData_203_3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카퇴장(self.ctx)


class 투르카퇴장(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=300, patrolName='PatrolData_Turka_3')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네엔딩대사(self.ctx)


class 마를레네엔딩대사(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[1005,1006], returnView=False)
        self.add_cinematic_talk(npcId=11004395, msg='$52100103_QD__MAIN__19$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 엔딩암전(self.ctx)


class 엔딩암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_3sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터정리(self.ctx)


class 몬스터정리(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 상황정리(self.ctx)


class 상황정리(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100109, portalId=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네생성준비(self.ctx)


class 마를레네생성준비(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마를레네생성(self.ctx)


class 마를레네생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[600], visible=False)
        self.set_effect(triggerIds=[700], visible=False)
        self.create_monster(spawnIds=[1], animationEffect=False)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 


initial_state = Ready
