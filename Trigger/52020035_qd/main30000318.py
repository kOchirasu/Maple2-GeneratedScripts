""" trigger/52020035_qd/main30000318.xml """
from common import *
import state


#  퀘스트 수락 후 연출 시작 
class idle3(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[703], questIds=[30000318], questStates=[2]):
            return 연출시작3()


#  라딘과 대화 시작 
class 연출시작3(state.State):
    def on_enter(self):
        set_onetime_effect(id=8, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출시작3_1()


class 연출시작3_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)
        destroy_monster(spawnIds=[117])
        destroy_monster(spawnIds=[118])
        destroy_monster(spawnIds=[119])
        destroy_monster(spawnIds=[120])
        destroy_monster(spawnIds=[121])
        create_monster(spawnIds=[110], arg2=False, arg3=0) # 연출라딘
        create_monster(spawnIds=[117], arg2=False, arg3=0) # 연출웨이홍
        create_monster(spawnIds=[118], arg2=False, arg3=0) # 연출브리드민
        create_monster(spawnIds=[119], arg2=False, arg3=0) # 연출바사라첸
        create_monster(spawnIds=[120], arg2=False, arg3=0) # 연출하렌
        create_monster(spawnIds=[121], arg2=False, arg3=0) # 연출카일
        select_camera_path(pathIds=[4026], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 뒷이야기()


class 뒷이야기(state.State):
    def on_enter(self):
        set_onetime_effect(id=8, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003754, msg='크크큭... 착한 연기 잘 하는군. 라딘.', duration=3000)
        set_scene_skip(state=끝, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 뒷이야기01()


class 뒷이야기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003753, msg='...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 뒷이야기01()


class 뒷이야기01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4030], returnView=False)
        set_npc_emotion_sequence(spawnId=119, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003756, msg='훗. 생각보다 잘 넘어간 것 같군요.', duration=3000)
        add_cinematic_talk(npcId=11003759, msg='쳇, 복잡하게 만들지 말고 그냥 죽어버리면 되잖아?', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 뒷이야기02()


class 뒷이야기02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003754, msg='하렌. 그럼 우리도 다음 작전을 이야기 해 볼까.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 뒷이야기02_1()


class 뒷이야기02_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4031], returnView=False)
        move_npc(spawnId=119, patrolName='MS2PatrolData_3008')
        add_cinematic_talk(npcId=11003756, msg='...후훗.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 끝()


class 끝(state.State):
    def on_enter(self):
        set_onetime_effect(id=9, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        set_onetime_effect(id=9, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True)
        move_user(mapId=2020012, portalId=1)
        destroy_monster(spawnIds=[111])
        destroy_monster(spawnIds=[112])
        destroy_monster(spawnIds=[113])
        destroy_monster(spawnIds=[114])
        destroy_monster(spawnIds=[115])


