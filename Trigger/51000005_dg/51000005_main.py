""" trigger/51000005_dg/51000005_main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=51000005, portal_id=10)
        # 101: 게임상대 - 11004718 아이돌 혁이
        self.spawn_monster(spawn_ids=[101], auto_target=False)
        # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트
        self.set_effect(trigger_ids=[601], visible=False)
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트
        self.set_effect(trigger_ids=[602], visible=False)
        # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603], visible=False)
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=셋둘하나_스킵완료, action='nextState') # setsceneskip 1 set
        # setsceneskip 1 set
        # setsceneskip 1 set
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=500):
            return 인트로00(self.ctx)


class 인트로00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8003,8004], return_view=False)
        self.set_cinematic_ui(type=1)
        # 안녕? 난 무대에서 가장 빛나는 아이돌 혁이!\n지금부터 나와 대결을 해보자!
        self.set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__0$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Bore_B', duration_tick=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2600):
            return 인트로01(self.ctx)


class 인트로01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8005,8006], return_view=False)
        self.set_cinematic_ui(type=1)
        # 나와 다른 방향을 선택하면 네가 이기고, \n같은 방향을 선택하면 지는 거야~!
        self.set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__1$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Emotion_A', duration_tick=2400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2700):
            return 인트로02(self.ctx)


class 인트로02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8002,8001], return_view=False)
        self.set_cinematic_ui(type=1)
        # 네가 다섯 번 지면 게임은 끝!\n오래 버틸수록 높은 점수를 받지!
        self.set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__2$')
        self.set_npc_emotion_loop(spawn_id=101, sequence_name='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 인트로03(self.ctx)


class 인트로03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip() # setsceneskip 1 close
        # setsceneskip 1 close
        # setsceneskip 1 close
        self.select_camera_path(path_ids=[8003,8006], return_view=False)
        self.set_cinematic_ui(type=1)
        # 높은 순위를 기록하면 선물도 있어. 완전 럭키~!\n자, 그럼 바로 시작해 볼까?
        self.set_cinematic_ui(type=3, script='$51000005_DG__51000005_MAIN__3$')
        self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Emotion_D', duration_tick=2400)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 게임시작_대기(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 셋둘하나_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolation_time=1.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 게임시작_대기(self.ctx)
        if not self.user_detected(box_ids=[9000]):
            return 연출종료(self.ctx)


class 게임시작_대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8000], return_view=False)
        self.set_achievement(trigger_id=9000, type='trigger', achieve='HyukiThreeTwoOne_start')
        # 로그를 남기기 위한 행 : arg5가 트리거 전체에서 유니크한 값이 들어가야 하며, arg1은 코드에 남고 있지 않음(서바이벌일 때만 서바이벌 로그 불러옴)
        self.write_log(log_name='ThreeTwoOne_log', trigger_id=9000, event='char_event', sub_event='HyukiThreeTwoOnegamestart')
        # lifeCount : 최대 사망 횟수
        self.arcade_three_two_one2(type='StartGame', life_count=5, init_score=10000)
        # self.set_event_ui(type=0, arg2='1,1', arg4='120')
        # 셋둘하나는 1라운드 내에서 무한루핑이므로 라운드 ui를 표시하지 않아 이 행을 넣지 않음
        self.set_user_value(trigger_id=4001, key='Fail', value=1) # Fail Event on
        self.add_balloon_talk(spawn_id=0, msg='$51000005_DG__51000005_MAIN__4$', duration=3000) # PC : 내가 이길 거야!
        # 시작 효과음 / 레디-고! 안 들어간 무음성 02100322
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Start_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드준비(self.ctx)


class 라운드준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[601], visible=False)
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[602], visible=False)
        # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603], visible=False)
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(wait_tick=500):
            return 라운드시작(self.ctx)


class 라운드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 26300736 가이드 텍스트 ON : [[icon:click]] 방향을 선택하세요.
        self.show_guide_summary(entity_id=1, text_id=26300736, duration=3000)
        # uiDuration : 게임 UI (화살표) 노출 시간
        self.arcade_three_two_one2(type='StartRound', ui_duration=4, round=1)
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_ArrowPopup_01') # 화살표 Ui 팝업 효과음 02100325

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(wait_tick=4000):
            return 라운드진행(self.ctx)


class 라운드진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=101, msg='$51000005_DG__51000005_MAIN__5$', duration=1800) # 혁이 대사 : 날 따라해!

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(weight=1):
            return 좌로돌아01(self.ctx)
        if self.random_condition(weight=1):
            return 뒤로돌아02(self.ctx)
        if self.random_condition(weight=1):
            return 우로돌아03(self.ctx)


class 좌로돌아01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='ResultRound', result_direction=1)
        # 혁이 왼쪽으로 돔 : 270도 = resultDirection 1
        self.set_npc_rotation(spawn_id=101, rotation=270)
        # 혁이 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 뒤로돌아02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='ResultRound', result_direction=2)
        # 혁이 뒤쪽으로 돔 : 180도 = resultDirection 2
        self.set_npc_rotation(spawn_id=101, rotation=180)
        # 혁이 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 우로돌아03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='ResultRound', result_direction=3)
        # 혁이 오른쪽으로 돔 : 90도 = resultDirection 3
        self.set_npc_rotation(spawn_id=101, rotation=90)
        # 혁이 도는 효과음 2500밀리초 02100326
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 결과연출(self.ctx)


class 결과연출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.init_npc_rotation(spawn_ids=[101])
        self.set_pc_rotation(rotation=[0,0,0])
        # 이펙트 601: 게임상대 - 11004718 아이돌 혁이 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[601], visible=False)
        # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(trigger_ids=[602], visible=False)
        # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[603], visible=False)
        # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(trigger_ids=[604], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThreeTwoOneResult') >= 1:
            # ThreeTwoOneResult 1 = 유저승리 = 다른방향
            # self.show_guide_summary(entity_id=2, text_id=26300737, duration=3000)
            # 26300737 가이드 텍스트 ON : 승리
            self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Emotion_B', duration_tick=4000) # 혁이 돌아서서 고개숙이고 씩씩 4000
            self.set_pc_emotion_loop(sequence_name='Emotion_Dance_X', duration=2450) # PC 신나서 인싸댄스
            self.set_effect(trigger_ids=[602], visible=True) # PC 머리 위 스포트라이트 이펙트
            # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
            self.set_effect(trigger_ids=[604], visible=True)
            self.add_balloon_talk(spawn_id=101, msg='$51000005_DG__51000005_MAIN__6$', duration=3000) # 혁이 : 말도 안 돼…!
            self.add_balloon_talk(msg='$51000005_DG__51000005_MAIN__7$', duration=3000) # …PC : 이겼다!
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Correct_01') # 성공 효과음 02100327
            return 결과정산(self.ctx)
        if self.user_value(key='ThreeTwoOneResult') >= 0:
            # ThreeTwoOneResult 0 = 유저패배 = 같은방향
            # self.show_guide_summary(entity_id=3, text_id=26300738, duration=3000)
            # 26300738 가이드 텍스트 ON : 패배
            self.set_npc_emotion_sequence(spawn_id=101, sequence_name='Emotion_A', duration_tick=2167)
            self.set_effect(trigger_ids=[601], visible=True) # 혁이 머리 위 스포트라이트 이펙트
            # 이펙트 603: 게임상대 - 11004718 아이돌 혁이 머리 위 불꽃놀이 이펙트
            self.set_effect(trigger_ids=[603], visible=True)
            self.set_pc_emotion_sequence(sequence_names=['Emotion_Fuss_A']) # PC 패배
            self.add_balloon_talk(spawn_id=101, msg='$51000005_DG__51000005_MAIN__8$', duration=3000) # …혁이 : 훗, 내가 좀 하지~
            self.add_balloon_talk(msg='$51000005_DG__51000005_MAIN__9$', duration=2700) # …PC : 내가 졌어!
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Wrong_01') # 패배 효과음 02100328
            return 결과정산(self.ctx)


class 결과정산(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='ResultRound2', round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2300):
            return 라운드결과(self.ctx)


class 라운드결과(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='ClearRound', round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 라운드준비(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.arcade_three_two_one2(type='EndGame')
        self.move_user(map_id=51000005, portal_id=44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 진짜끝(self.ctx)


class 진짜끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=8010, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        # 끝나는 효과음 02100329 혁이 셋둘하나 전용
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 완전끝(self.ctx)


class 완전끝(trigger_api.Trigger):
    pass


initial_state = 입장
