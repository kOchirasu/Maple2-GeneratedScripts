""" trigger/52000073_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[60100115], questStates=[1]):
            return 레논등장(self.ctx)


class 레논등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        """
        연출 3 : 레터박스
        연출 1 : 플레이어 조작 뺏기
        """
        self.set_onetime_effect(id=1, enable=True, path='BG\\weather\\Eff_monochrome_03.xml')
        self.set_sound(triggerId=7001, enable=True)
        self.destroy_monster(spawnIds=[101])
        self.visible_my_pc(isVisible=False)
        self.set_ambient_light(primary=[0,0,0])
        self.set_ambient_light(primary=[1,1,1])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[302]) # 윈 스틸던의 시체
        self.create_monster(spawnIds=[301]) # 레논
        self.select_camera_path(pathIds=[8001,8002], returnView=False)
        self.set_scene_skip(state=다크윈드통로, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 계단이동(self.ctx)


class 계단이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2001')
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__0$', arg4=3, arg5=0) # 레논 계단 올라가며 하는 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 시체발견(self.ctx)


class 시체발견(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__1$', arg4=2, arg5=0)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2002')
        self.select_camera_path(pathIds=[8005], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 의문(self.ctx)


class 의문(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__2$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 상황파악(self.ctx)


class 상황파악(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=7002, enable=True)
        self.select_camera_path(pathIds=[8006], returnView=False) # 카메라 레논 얼굴로
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__3$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Sit_down_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 현장목격(self.ctx)


class 현장목격(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8007], returnView=False) # 레논 뒤편으로
        self.create_monster(spawnIds=[303]) # 다크윈드 대원 좌
        self.create_monster(spawnIds=[304]) # 다크윈드 대원 우
        self.set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__4$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=1500) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=1500) # 다크윈드 대원 우 모션
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오해1(self.ctx)


class 오해1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__5$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=304, script='$52000073_QD__MAIN__6$', arg4=3, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오해2(self.ctx)


class 오해2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__7$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__8$', arg4=3, arg5=1)
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Attack_01_A', duration=2000) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawnId=301, sequenceName='Talk_A', duration=3000) # 레논 대화 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오해3(self.ctx)


class 오해3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__9$', arg4=3, arg5=0)
        self.set_conversation(type=1, spawnId=304, script='$52000073_QD__MAIN__10$', arg4=3, arg5=2)
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_2003')
        self.move_npc(spawnId=304, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오해4(self.ctx)


class 오해4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=5000) # 다크윈드 대원 좌 모션
        self.set_conversation(type=1, spawnId=303, script='$52000073_QD__MAIN__11$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=5000) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오해5(self.ctx)


class 오해5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=301, script='$52000073_QD__MAIN__12$', arg4=5, arg5=0)
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2006')
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=6000) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawnId=304, sequenceName='Attack_Idle_A', duration=6000) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 쓰러짐(self.ctx)


class 쓰러짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Down_Idle_A', duration=500000) # 다크윈드 대원 좌 모션
        self.set_npc_emotion_loop(spawnId=304, sequenceName='Down_Idle_A', duration=500000) # 다크윈드 대원 우 모션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 탈출(self.ctx)


class 탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_2007')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 레논탈출(self.ctx)


class 레논탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[301])
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라시점변경_ready(self.ctx)


class 카메라시점변경_ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라시점변경(self.ctx)


class 카메라시점변경(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8008], returnView=False) # 공중뷰

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카트반등장(self.ctx)


class 카트반등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[305]) # 카트반

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카트반이동(self.ctx)


class 카트반이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_2008')
        self.set_conversation(type=1, spawnId=305, script='$52000073_QD__MAIN__13$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 의미심장(self.ctx)


class 의미심장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11001024, msg='$52000073_QD__MAIN__14$', duration=3000, align='center')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 다크윈드통로(self.ctx)


class 다크윈드통로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.create_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[301,302,303,304,305])
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=52000138, portalId=0)


initial_state = idle
