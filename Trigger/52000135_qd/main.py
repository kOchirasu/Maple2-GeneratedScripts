""" trigger/52000135_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102])
        self.set_mesh(triggerIds=[3000,3001], visible=False) # 아이노 크리스탈 on/off 컨트롤
        self.set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on/off 컨트롤
        self.set_interact_object(triggerIds=[10001175], state=1) # 아이노 크리스탈
        self.set_effect(triggerIds=[3010,3011,3012], visible=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[2]):
            return 연출이후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[1]):
            return 연출대기(self.ctx)


class 연출이후(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 연출대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000135, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스대사01(self.ctx)


class 아노스대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_01')
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__0$', duration=4000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8500)
        self.set_scene_skip(state=오브젝트조사전_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스대사02(self.ctx)


class 아노스대사02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__1$', duration=4000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6800)
        self.set_skip(state=아노스대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스대사03(self.ctx)


class 아노스대사02_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사03(self.ctx)


class 아노스대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=True)
        self.add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__2$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='ChatUp_A', duration=5400)
        self.move_user_path(patrolName='MS2PatrolData_PC_03')
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오브젝트조사(self.ctx)


class 오브젝트조사전_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000135, portalId=10) # 퀘스트 시작 위치로 pc 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 오브젝트조사(self.ctx)


class 오브젝트조사(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10001175], stateValue=0):
            return 오브젝트반응이후(self.ctx)


class 오브젝트반응이후(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_mesh(triggerIds=[3000], visible=True) # 아이노 크리스탈 on
        self.set_mesh_animation(triggerIds=[3000], visible=True) # 아이노 크리스탈 on
        self.set_effect(triggerIds=[3011], visible=True)
        self.set_interact_object(triggerIds=[10001175], state=2)
        self.move_user_path(patrolName='MS2PatrolData_PC_0301')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스대사04(self.ctx)


class 아노스대사04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__3$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=7000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0201')
        self.set_scene_skip(state=오브젝트조사후_스킵완료, action='nextState') # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사05(self.ctx)


class 아노스대사05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__4$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8300)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0202')
        self.set_skip(state=아노스대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사06(self.ctx)


class 아노스대사05_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사06(self.ctx)


class 아노스대사06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__5$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6500)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0203')
        self.set_skip(state=아노스대사06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사07(self.ctx)


class 아노스대사06_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사07(self.ctx)


class 아노스대사07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='Anos_normal', msg='$52000135_QD__MAIN__6$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Chatup_A', duration=7900)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0204')
        self.set_skip(state=아노스대사07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크리스탈끄기(self.ctx)


class 아노스대사07_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 크리스탈끄기(self.ctx)


class 크리스탈끄기(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_0205')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 크리스탈꺼짐(self.ctx)


class 크리스탈꺼짐(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        self.set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(triggerIds=[3011], visible=False)
        self.set_effect(triggerIds=[3012], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아노스대사08(self.ctx)


class 아노스대사08(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__7$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=11000)
        self.set_effect(triggerIds=[3012], visible=False)
        self.set_skip(state=아노스대사08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아시모프대사01(self.ctx)


class 아노스대사08_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아시모프대사01(self.ctx)


class 아시모프대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.add_cinematic_talk(npcId=11003250, illustId='0', msg='$52000135_QD__MAIN__8$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=5100)
        self.set_skip(state=아시모프대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아노스대사09(self.ctx)


class 아시모프대사01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아노스대사09(self.ctx)


class 아노스대사09(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__9$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3800)
        self.move_user_path(patrolName='MS2PatrolData_PC_0302')
        self.set_skip(state=아노스대사09_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC크리스탈접근(self.ctx)


class 아노스대사09_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC크리스탈접근(self.ctx)


class PC크리스탈접근(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000135_QD__MAIN__10$', duration=2000, align='right')
        self.set_pc_emotion_loop(sequenceName='Object_React_H', duration=1500)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크리스탈켜짐(self.ctx)


class 크리스탈켜짐(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.set_mesh(triggerIds=[3001], visible=False) # 아이노 크리스탈 off-on
        self.set_mesh_animation(triggerIds=[3001], visible=False) # 아이노 크리스탈 off-on
        self.set_mesh(triggerIds=[3000], visible=True) # 아이노 크리스탈 off-on
        self.set_mesh_animation(triggerIds=[3000], visible=True) # 아이노 크리스탈 off-on
        self.set_effect(triggerIds=[3010], visible=True)
        self.add_balloon_talk(spawnId=0, msg='$52000135_QD__MAIN__11$', duration=3000, delayTick=1000)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Surprise_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마법사들접근(self.ctx)


class 마법사들접근(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8012], returnView=False)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Asimov_05')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_04')
        self.set_effect(triggerIds=[3011], visible=True)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Think_A'])
        self.add_balloon_talk(spawnId=101, msg='$52000135_QD__MAIN__12$', duration=2000, delayTick=100)
        self.add_balloon_talk(spawnId=102, msg='$52000135_QD__MAIN__13$', duration=2000, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스대사10(self.ctx)


class 아노스대사10(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__14$', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3400)
        self.set_skip(state=아노스대사10_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사(self.ctx)


class 아노스대사10_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사(self.ctx)


class PC대사(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000135_QD__MAIN__15$', duration=3000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_06')
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A'])
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 크리스탈다시꺼짐(self.ctx)


class 크리스탈다시꺼짐(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        self.set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        self.set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(triggerIds=[3010,3011], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아노스대사11(self.ctx)


class 아노스대사11(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003251, illustId='0', msg='$52000135_QD__MAIN__16$', duration=5000, align='right')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_07')
        self.set_skip(state=아노스대사11_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아시모프대사02(self.ctx)


class 아노스대사11_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아시모프대사02(self.ctx)


class 아시모프대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.add_cinematic_talk(npcId=11003250, illustId='Asimov_normal', msg='$52000135_QD__MAIN__17$', duration=3000, align='left')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=8600)
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class 오브젝트조사후_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Asimov_05') # 아시모프 이동. 굳이 안 해도 될 것 같음
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Anos_07') # 아노스 이동. 굳이 안 해도 될 것 같음
        self.set_mesh(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        self.set_mesh_animation(triggerIds=[3000], visible=False) # 아이노 크리스탈 on-off
        self.set_mesh(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_mesh_animation(triggerIds=[3001], visible=True) # 아이노 크리스탈 on-off
        self.set_effect(triggerIds=[3010,3011], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='Studyindarkness')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
