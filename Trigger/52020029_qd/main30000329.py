""" trigger/52020029_qd/main30000329.xml """
import common


# 진리의 문 입장
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[30000329], questStates=[2]):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_02(self.ctx)


class 연출시작_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52020029, portalId=6001)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 진리의문입장(self.ctx)


class 진리의문입장(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3001')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3003')
        self.add_cinematic_talk(npcId=11003755, msg='후. 이제서야 이곳에 들어오게 되는 군요.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진리의문입장_02(self.ctx)


class 진리의문입장_02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003755, msg='덕분에 정말 큰 도움 받았습니다.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진리의문입장_03(self.ctx)


class 진리의문입장_03(common.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=0, emotionName='defaultBattle')
        self.add_cinematic_talk(npcId=0, msg='저건...', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 진리의문유례(self.ctx)


class 진리의문유례(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.add_cinematic_talk(npcId=11003755, msg='아아. 저 두개의 큰 화면. 저것이 바로 진리의 문입니다.', duration=3000)
        self.add_cinematic_talk(npcId=11003755, msg='듣기론 세상의 모든 정보를 찾을 수 있는 기계라더군요.', duration=3000)
        self.set_scene_skip(state=마무리, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 감탄(self.ctx)


class 감탄(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=11003717, msg='아아... 저것을 직접 만져볼 수 있다니 황홀하군!', duration=3000)
        self.add_cinematic_talk(npcId=11003755, msg='자, 시간이 없으니 빨리 원하는 정보를 검색해 보죠.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 마무리(self.ctx)


class 마무리(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마무리2(self.ctx)


class 마무리2(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020029, portalId=6002)
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.create_monster(spawnIds=[105], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마무리3(self.ctx)


class 마무리3(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
