""" trigger/52020028_qd/main30000328.xml """
from common import *
import state


#  아크로폴리스 수호자 처치 퀘스트를 받고 입장 
class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[30000328], questStates=[1]):
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        move_user(mapId=52020028, portalId=6002)
        set_onetime_effect(id=1000, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 아크로폴리스내부확인()


class 아크로폴리스내부확인(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='아크로폴리스', desc='고대 크리티아스 지식의 안식처', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        select_camera_path(pathIds=[4002,4003,4004], returnView=False)
        add_cinematic_talk(npcId=0, msg='여기가 아크로폴리스...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 유저이동()


class 유저이동(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012,4001], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=0, msg='생각보다 조용하군.', duration=3000)
        add_cinematic_talk(npcId=0, msg='수호자 때문에 안에 들어갈 수가 없다니, 얼마나 대단한 녀석인거지.', duration=3000)
        add_cinematic_talk(npcId=0, msg='싸우지 않을 수 있었으면 좋겠는데.', duration=3000)
        add_cinematic_talk(npcId=0, msg='그나저나, 정말 아무도 없는 것 같은데...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 유저자격확인하기전()


class 유저자격확인하기전(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_effect(triggerIds=[5003], visible=True)
        face_emotion(spawnId=0, emotionName='Trigger_panic')
        set_pc_emotion_loop(sequenceName='Idle_A', duration=6000)
        add_balloon_talk(spawnId=0, msg='?!', duration=3000)
        add_balloon_talk(spawnId=0, msg='이... 이건?', duration=3000, delayTick=3000)
        set_scene_skip(state=경고, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 유저자격확인()


class 유저자격확인(state.State):
    def on_enter(self):
        set_cinematic_ui(type=9, script='침입자 발견. 자격을 확인한다.', arg3=False)
        set_scene_skip(state=아르케온등장4, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저자격확인2()


class 유저자격확인2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        face_emotion(spawnId=0, emotionName='Trigger_panic')
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=18000)
        set_effect(triggerIds=[5003], visible=True)
        add_balloon_talk(spawnId=0, msg='자격을 확인한다고? 잠깐!!!', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저자격확인2_1()


class 유저자격확인2_1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=22000117, msg='문답무용.\n순수한 크리티아스의 피가 흐르지 않는 자는 이곳에 발을 디딜 수 없다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저자격확인3()


class 유저자격확인3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4010], returnView=False)
        add_balloon_talk(spawnId=0, msg='잠시 이야기를 들어줘!', duration=3000, delayTick=4000)
        add_cinematic_talk(npcId=22000117, msg='결과를 확인한다.', duration=3000)
        add_cinematic_talk(npcId=22000117, msg='결과, 부적합.\n전투 시스템 가동.', duration=3000)
        set_effect(triggerIds=[5003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 아르케온등장()


class 아르케온등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=False)
        set_onetime_effect(id=1000, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=22000117, msg='자격이 없는 자, 즉시 처단한다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 아르케온등장2()


class 아르케온등장2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4007], returnView=False)
        add_balloon_talk(spawnId=0, msg='아니 대화가 전혀 안 통하잖아!', duration=2000, delayTick=0)
        set_onetime_effect(id=1000, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 경고()


class 경고(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 등장연출()


class 등장연출(state.State):
    def on_enter(self):
        set_onetime_effect(id=1000, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        select_camera_path(pathIds=[4005], returnView=False)
        set_effect(triggerIds=[5001], visible=True)
        create_monster(spawnIds=[101], arg2=False)
        show_caption(type='VerticalCaption', title='아르케온', desc='아크로폴리스의 수호자', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        set_onetime_effect(id=1001, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 아르케온등장3()


class 아르케온등장3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=0, msg='역시 이렇게 되는군.', duration=3000)
        add_cinematic_talk(npcId=0, msg='말이 통하지 않으니, 어쩔 수 없지.\n여기서 시간을 낭비할 수 없어.\n어서 처치하자.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 아르케온등장4()


class 아르케온등장4(state.State):
    def on_enter(self):
        set_onetime_effect(id=1001, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='수호자 아르케온을 처치하세요.', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 다음연출시작()


class 다음연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다음연출시작_02()


class 다음연출시작_02(state.State):
    def on_enter(self):
        move_user(mapId=52020028, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 위치이동()


class 위치이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=0, msg='휴... 힘든 싸움이었어.', duration=3000)
        add_cinematic_talk(npcId=0, msg='중요한 시설인가보군, 이런 괴물같은 녀석이 지키고 있는 것을 보니...', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 진리의문확인()


class 진리의문확인(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004,4003], returnView=False)
        set_effect(triggerIds=[5002], visible=False)
        add_cinematic_talk(npcId=0, msg='아무래도 저기가 진리의 문인가 보군.', duration=3000)
        add_cinematic_talk(npcId=0, msg='아르망에게 전달해야겠어. 알케이나 고원으로 돌아가자.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 이오네독백준비()


class 이오네독백준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이오네독백준비_02()


class 이오네독백준비_02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        select_camera(triggerId=4011, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이오네독백()


class 이오네독백(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011,4008], returnView=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        show_caption(type='VerticalCaption', title='이오네', desc='크리티아스의 왕녀', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)
        add_cinematic_talk(npcId=11003760, msg='그 동안 수고 했어요. 아르케온.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 이오네독백_02()


class 이오네독백_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003760, msg='이 뒤는 저에게 맡기고 편히 쉬세요.', duration=3000)
        add_cinematic_talk(npcId=11003760, msg='이제 이 곳의 모든 정보는 그 누구도 열어보지 못하도록...\n이 이오네가 책임지고 막겠습니다.', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Warp준비()


class Warp준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Warp()


class Warp(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2020016, portalId=3)


