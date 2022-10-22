""" trigger/51000005_dg/51000005_main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        move_user(mapId=51000005, portalId=10)
        create_monster(spawnIds=[101], arg2=False) # 101: 게임상대 - 11004718 아이돌 혁이
        set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트
        set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트
        set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 인트로()


class 인트로(state.State):
    def on_enter(self):
        set_scene_skip(state=셋둘하나_스킵완료, arg2='nextState') # setsceneskip 1 set
        select_camera_path(pathIds=[8000], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 인트로00()


class 인트로00(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003,8004], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__0$') # 안녕? 난 무대에서 가장 빛나는 아이돌 혁이!\n지금부터 나와 대결을 해보자!
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_B', durationTick=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2600):
            return 인트로01()


class 인트로01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8005,8006], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__1$') # 나와 다른 방향을 선택하면 네가 이기고, \n같은 방향을 선택하면 지는 거야~!
        set_npc_emotion_sequence(spawnId=101, sequenceName='Emotion_A', durationTick=2400)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2700):
            return 인트로02()


class 인트로02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8001], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__2$') # 네가 다섯 번 지면 게임은 끝!\n오래 버틸수록 높은 점수를 받지!
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 인트로03()


class 인트로03(state.State):
    def on_enter(self):
        set_scene_skip() # setsceneskip 1 close
        select_camera_path(pathIds=[8003,8006], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__3$') # 높은 순위를 기록하면 선물도 있어. 완전 럭키~!\n자, 그럼 바로 시작해 볼까?
        set_npc_emotion_sequence(spawnId=101, sequenceName='Emotion_D', durationTick=2400)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 게임시작_대기()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 셋둘하나_스킵완료(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 게임시작_대기()
        if not user_detected(boxIds=[9000]):
            return 연출종료()


class 게임시작_대기(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8000], returnView=False)
        set_achievement(triggerId=9000, type='trigger', achieve='HyukiThreeTwoOne_start')
        write_log(logName='ThreeTwoOne_log', event='9000', arg3='char_event', arg5='HyukiThreeTwoOnegamestart') # 로그를 남기기 위한 행 : arg5가 트리거 전체에서 유니크한 값이 들어가야 하며, arg1은 코드에 남고 있지 않음(서바이벌일 때만 서바이벌 로그 불러옴)
        arcade_three_two_one2(type='StartGame', lifeCount=5, initScore=10000)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="1,1" arg4="120"/>
        set_user_value(triggerId=4001, key='Fail', value=1) # Fail Event on
        add_balloon_talk(spawnId=0, msg='$51000005_DG__51000005_MAIN__4$', duration=3000) # PC : 내가 이길 거야!
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Start_01') # 시작 효과음 / 레디-고! 안 들어간 무음성 02100322

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라운드준비()


class 라운드준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트 끄기
        set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return 완전끝()
        if wait_tick(waitTick=500):
            return 라운드시작()


class 라운드시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=1, textId=26300736, duration=3000) # 26300736 가이드 텍스트 ON : [[icon:click]] 방향을 선택하세요.
        arcade_three_two_one2(type='StartRound', uiDuration=4, round=1) # uiDuration : 게임 UI (화살표) 노출 시간
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_ArrowPopup_01') # 화살표 Ui 팝업 효과음 02100325

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9000]):
            return 완전끝()
        if wait_tick(waitTick=4000):
            return 라운드진행()


class 라운드진행(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$51000005_DG__51000005_MAIN__5$', duration=1800) # 혁이 대사 : 날 따라해!

    def on_tick(self) -> state.State:
        if random_condition(rate=1):
            return 좌로돌아01()
        if random_condition(rate=1):
            return 뒤로돌아02()
        if random_condition(rate=1):
            return 우로돌아03()


class 좌로돌아01(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='ResultRound', resultDirection=1)
        set_npc_rotation(spawnId=101, rotation=270) # 혁이 왼쪽으로 돔 : 270도 = resultDirection 1
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 혁이 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 결과연출()


class 뒤로돌아02(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='ResultRound', resultDirection=2)
        set_npc_rotation(spawnId=101, rotation=180) # 혁이 뒤쪽으로 돔 : 180도 = resultDirection 2
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 혁이 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 결과연출()


class 우로돌아03(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='ResultRound', resultDirection=3)
        set_npc_rotation(spawnId=101, rotation=90) # 혁이 오른쪽으로 돔 : 90도 = resultDirection 3
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 혁이 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 결과연출()


class 결과연출(state.State):
    def on_enter(self):
        init_npc_rotation(spawnIds=[101])
        set_pc_rotation(rotation=[0,0,0])
        set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트 끄기
        set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트

    def on_tick(self) -> state.State:
        if user_value(key='ThreeTwoOneResult', value=1):
            set_npc_emotion_sequence(spawnId=101, sequenceName='Emotion_B', durationTick=4000)
            set_pc_emotion_loop(sequenceName='Emotion_Dance_X', duration=2450)
            set_effect(triggerIds=[602], visible=True)
            set_effect(triggerIds=[604], visible=True)
            add_balloon_talk(spawnId=101, msg='$51000005_DG__51000005_MAIN__6$', duration=3000)
            add_balloon_talk(msg='$51000005_DG__51000005_MAIN__7$', duration=3000)
            play_system_sound_in_box(sound='System_PinkBeans_Arcade_Correct_01')
            return 결과정산()
        if user_value(key='ThreeTwoOneResult', value=0):
            set_npc_emotion_sequence(spawnId=101, sequenceName='Emotion_A', durationTick=2167)
            set_effect(triggerIds=[601], visible=True)
            set_effect(triggerIds=[603], visible=True)
            set_pc_emotion_sequence(sequenceNames=['Emotion_Fuss_A'])
            add_balloon_talk(spawnId=101, msg='$51000005_DG__51000005_MAIN__8$', duration=3000)
            add_balloon_talk(msg='$51000005_DG__51000005_MAIN__9$', duration=2700)
            play_system_sound_in_box(sound='System_PinkBeans_Arcade_Wrong_01')
            return 결과정산()


class 결과정산(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='ResultRound2', round=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2300):
            return 라운드결과()


class 라운드결과(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='ClearRound', round=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 라운드준비()


class 연출종료(state.State):
    def on_enter(self):
        arcade_three_two_one2(type='EndGame')
        move_user(mapId=51000005, portalId=44)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 진짜끝()


class 진짜끝(state.State):
    def on_enter(self):
        select_camera(triggerId=8010, enable=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01') # 끝나는 효과음 02100329 혁이 셋둘하나 전용

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 완전끝()


class 완전끝(state.State):
    pass


