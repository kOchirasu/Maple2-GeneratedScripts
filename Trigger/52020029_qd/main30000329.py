""" trigger/52020029_qd/main30000329.xml """
from common import *
import state


#  진리의 문 입장 
class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000329], questStates=[2]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_02()


class 연출시작_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020029, portalId=6001)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 진리의문입장()


class 진리의문입장(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        move_npc(spawnId=101, patrolName='MS2PatrolData_3002')
        move_npc(spawnId=102, patrolName='MS2PatrolData_3003')
        add_cinematic_talk(npcId=11003755, msg='후. 이제서야 이곳에 들어오게 되는 군요.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진리의문입장_02()


class 진리의문입장_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003755, msg='덕분에 정말 큰 도움 받았습니다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진리의문입장_03()


class 진리의문입장_03(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='defaultBattle')
        add_cinematic_talk(npcId=0, msg='저건...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진리의문유례()


class 진리의문유례(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11003755, msg='아아. 저 두개의 큰 화면. 저것이 바로 진리의 문입니다.', duration=3000)
        add_cinematic_talk(npcId=11003755, msg='듣기론 세상의 모든 정보를 찾을 수 있는 기계라더군요.', duration=3000)
        set_scene_skip(state=마무리, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 감탄()


class 감탄(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_B')
        add_cinematic_talk(npcId=11003717, msg='아아... 저것을 직접 만져볼 수 있다니 황홀하군!', duration=3000)
        add_cinematic_talk(npcId=11003755, msg='자, 시간이 없으니 빨리 원하는 정보를 검색해 보죠.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 마무리()


class 마무리(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마무리2()


class 마무리2(state.State):
    def on_enter(self):
        move_user(mapId=52020029, portalId=6002)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 마무리3()


class 마무리3(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


