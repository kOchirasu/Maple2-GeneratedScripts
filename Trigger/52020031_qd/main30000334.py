""" trigger/52020031_qd/main30000334.xml """
from common import *
import state


#  제단 입장 
# 
# 예상치 못한 인물 하렌(11003747) - spawnpoint : 1 
# 한순간의 방심 하렌(11003749) - spawnpoint : 2
# 연출용 하렌(11003756) - spawnpoint : 101 
# 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000334], questStates=[1]):
            return 세번째전투끝나고()


class 세번째전투끝나고(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세번째전투끝나고1()


class 세번째전투끝나고1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5001], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 세번째전투끝나고2()


class 세번째전투끝나고2(state.State):
    def on_enter(self):
        move_user(mapId=52020031, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 세번째전투끝나고2_2()


class 세번째전투끝나고2_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5001], visible=True)
        face_emotion(spawnId=0, emotionName='defaultBattle')
        set_pc_emotion_loop(sequenceName='Idle_A', duration=5000)
        add_cinematic_talk(npcId=0, msg='역시 너희 흑성회는 믿을 만한 사람들이 아니었군.\n천공의 심장은 내가 가져가겠어.', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 세번째전투끝나고3()


class 세번째전투끝나고3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        set_effect(triggerIds=[5001], visible=False)
        add_cinematic_talk(npcId=11003756, msg='크윽...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째전투끝나고3_01()


class 세번째전투끝나고3_01(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 세번째전투끝나고4()


class 세번째전투끝나고4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=0, msg='오늘 있었던 일은, 라딘에게도 전하겠어.', duration=3000)
        add_cinematic_talk(npcId=0, msg='흑성회와의 동맹은 여기까지야.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 천공의탑으로이동()


class 천공의탑으로이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52020030, portalId=6001)


