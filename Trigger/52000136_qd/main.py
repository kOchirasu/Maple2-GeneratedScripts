""" trigger/52000136_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601,602], visible=False)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001604], questStates=[1]):
            return 기본(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001603], questStates=[3]):
            return 기본(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001603], questStates=[2]):
            return 연출시작(self.ctx)


class 기본(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 첫진입(self.ctx)


class 첫진입(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__0$', duration=3000, align='left')
        self.set_scene_skip(state=불안한케이틀린_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전경스케치01(self.ctx)


class 전경스케치01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전경스케치02(self.ctx)


class 전경스케치02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_user(mapId=52000136, portalId=10)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 케이틀린발견01(self.ctx)


class 케이틀린발견01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.move_npc(spawnId=101, patrolName='Patrol_101_katelyn_wander')
        self.add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__1$', duration=1000, delayTick=0)
        self.add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__2$', duration=1000, delayTick=500)
        self.add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__3$', duration=1000, delayTick=500)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 케이틀린발견02(self.ctx)


class 케이틀린발견02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__4$', duration=3000, align='left')
        self.move_user_path(patrolName='MS2PatrolData_PC')
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린발견03(self.ctx)


class 케이틀린발견03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.add_balloon_talk(spawnId=101, msg='$52000136_QD__MAIN__5$', duration=3000, delayTick=500)
        self.move_npc(spawnId=101, patrolName='Patrol_101_katelyn_run')
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사01(self.ctx)


class 케이틀린대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.set_conversation(type=2, spawnId=11003261, script='$52000136_QD__MAIN__6$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4300)
        self.set_skip(state=불안한케이틀린_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사01(self.ctx)


class PC대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000136_QD__MAIN__7$', duration=3000, align='left')
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 케이틀린대사02(self.ctx)


class 케이틀린대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.set_conversation(type=2, spawnId=11003261, script='$52000136_QD__MAIN__8$', arg4=3, arg5=0)
        self.set_skip(state=불안한케이틀린_스킵완료) # 통스킵 위한 추가한 액션

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 문줌인(self.ctx)


class 문줌인(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8011], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출종료(self.ctx)


class 불안한케이틀린_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010,8011], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000136, portalId=11)
        self.move_npc(spawnId=101, patrolName='Patrol_101_katelyn_run') # 케이틀린 위치로

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
