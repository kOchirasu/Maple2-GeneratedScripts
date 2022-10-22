""" trigger/52020030_qd/main30000334.xml """
from common import *
import state


#  탑 입장 
# 
# 크란츠 - 101
# 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000334], questStates=[1]):
            return 연출시작()
        if quest_user_detected(boxIds=[2001], questIds=[30000334], questStates=[2]):
            return 크란츠습격04_01()


class 연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4023,4020], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52020030, portalId=6001) # 천공의탑 문앞

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저걸어감()


class 유저걸어감(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user_path(patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=0, msg='천공의 심장을 손에 넣었으니 티어스 코어를 완벽히 다시 만들 순 없을거야.', duration=3000)
        add_cinematic_talk(npcId=0, msg='지금쯤 수호군은 도착했을까...', duration=3000)
        add_cinematic_talk(npcId=0, msg='빨리 라딘에게 돌아가야겠어.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 바라보는크란츠()


class 바라보는크란츠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 바라보는크란츠_01()


class 바라보는크란츠_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4027,4014], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 바라보는크란츠_02()


class 바라보는크란츠_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4014], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_C')
        add_cinematic_talk(npcId=11003761, msg='후우... 말을 안 듣는군.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 바라보는크란츠_03()


class 바라보는크란츠_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4024], returnView=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 잠시암전()


class 잠시암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4016,4015], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 크란츠습격전()


class 크란츠습격전(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크란츠습격()


class 크란츠습격(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[106], arg2=False)
        add_cinematic_talk(npcId=11003761, msg='... 봐 주는건, 여기까지야.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠습격01()


class 크란츠습격01(state.State):
    def on_enter(self):
        set_onetime_effect(id=300, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=0, msg='커헉!', duration=1500)
        move_user(mapId=52020030, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 크란츠습격02()


class 크란츠습격02(state.State):
    def on_enter(self):
        set_onetime_effect(id=300, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5006], visible=True)
        select_camera_path(pathIds=[4005], returnView=False)
        set_pc_emotion_loop(sequenceName='Stun_A', duration=20000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠습격03()


class 크란츠습격03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4025], returnView=False)
        add_cinematic_talk(npcId=0, msg='으으... 넌...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 크란츠습격03_01()


class 크란츠습격03_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4026], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='빨리 이곳에서 나가라니깐, 정~말 말을 안 듣는 인간이군.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠습격03_01_01()


class 크란츠습격03_01_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4028], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='이런 귀중한 크리티아스의 보물을 당신과 같은 외지인에게 넘길 순 없어.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠습격03_02()


class 크란츠습격03_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4025], returnView=False)
        add_cinematic_talk(npcId=0, msg='잠깐... 이건 오해야. 난 이오네 왕녀를 위해서...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 크란츠습격03_03()


class 크란츠습격03_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4029], returnView=False)
        add_cinematic_talk(npcId=11003761, msg='... 천공의 심장은 내가 가져가겠다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 크란츠습격04()


class 크란츠습격04(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5006], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크란츠습격04_01()


class 크란츠습격04_01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111], arg2=False) # 퀘스트용 크란츠

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 크란츠습격05()


class 크란츠습격05(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0.5)
        destroy_monster(spawnIds=[106])
        set_achievement(triggerId=2001, type='trigger', achieve='AttackSomeone')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


