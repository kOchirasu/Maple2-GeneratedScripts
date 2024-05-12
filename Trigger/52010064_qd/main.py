""" trigger/52010064_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.create_monster(spawnIds=[101], animationEffect=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[3]):
            return 돌아가(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[2]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[1]):
            return CameraEffect01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[91000072], questStates=[3]):
            return 돌아가(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[91000073], questStates=[1]):
            return 돌아가(self.ctx)


class CameraEffect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_scene_skip(state=quit01, action='nextState') # setsceneskip 1 set
        # setsceneskip set
        # setsceneskip set
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='flyingtristan') # 퀘스트 완료 업적

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return CameraEffect02(self.ctx)


class CameraEffect02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.select_camera_path(pathIds=[8000], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리스탄대사01(self.ctx)


class 트리스탄대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__0$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사02(self.ctx)


class 트리스탄대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__1$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사03(self.ctx)


class 트리스탄대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__2$', duration=3000, align='right')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Tristan_walking')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사04(self.ctx)


class 트리스탄대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__3$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사05(self.ctx)


class 트리스탄대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__4$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트리스탄대사06(self.ctx)


class 트리스탄대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003842, illustId='Tristan_normal', msg='$52010064_QD__main__5$', duration=3000, align='right')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마무리줌아웃(self.ctx)


class 마무리줌아웃(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_cinematic_ui(type=0)
        # Missing State: State
        self.set_scene_skip() # setsceneskip 1 close
        # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return quit01(self.ctx)


class quit01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return quit03(self.ctx)


class quit03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=2)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')
        self.move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return quit03(self.ctx)


class 돌아가(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52010052, portalId=1) # 작전실로 자동 이동
        self.visible_my_pc(isVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            # 맵 튕기고 이동 명령 못 받을 상태를 대비한 안전장치
            return 돌아가(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
