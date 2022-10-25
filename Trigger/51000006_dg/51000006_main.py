""" trigger/51000006_dg/51000006_main.xml """
import common


class 입장(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000006, portalId=10)
        self.create_monster(spawnIds=[101], animationEffect=False) # 101: 게임상대 - 11004827 NPC 시간여행자 블랙빈
        self.set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트
        self.set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트
        self.set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(triggerIds=[610], visible=False) # 이펙트 610: PC 머리 위 내리는 비 이펙트
        self.set_actor(triggerId=611, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈01끄기
        self.set_actor(triggerId=612, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈02끄기
        self.set_actor(triggerId=613, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈03끄기
        self.set_actor(triggerId=614, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈04끄기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 인트로(self.ctx)


class 인트로(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=셋둘하나_스킵완료, action='nextState') # setsceneskip 1 set
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 인트로00(self.ctx)


class 인트로00(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__0$') # 대사내용01 : 안녕! 난 자유로운 블랙빈! 노는 게 제일 좋아~\n지금부터 나랑 놀자!"
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Walk_A', durationTick=2500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2600):
            return 인트로01(self.ctx)


class 인트로01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005,8006], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__1$') # 대사내용02 : 나와 다른 방향을 선택하면 네가 이기고, \n같은 방향을 선택하면 지는 거야~!
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Event_Bore_A', durationTick=2900)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인트로02(self.ctx)


class 인트로02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__2$') # 대사내용03 : 네가 다섯 번 지면 놀이는 끝!\n오래 버틸수록 높은 점수를 받지!
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Event_Eat_A', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3100):
            return 인트로03(self.ctx)


class 인트로03(common.Trigger):
    def on_enter(self):
        self.set_scene_skip() # setsceneskip 1 close
        self.select_camera_path(pathIds=[8003,8006], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000006_DG__51000006_MAIN__3$') # 대사내용04 : 순위가 높으면 선물도 주지! 어때, 끌리지?\n그럼 바로 시작해 보자~ 뿡뿡!
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_G', durationTick=3200)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3300):
            return 게임시작_대기(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 셋둘하나_스킵완료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 게임시작_대기(self.ctx)
        if not self.user_detected(boxIds=[9000]):
            return 연출종료(self.ctx)


class 게임시작_대기(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_achievement(triggerId=9000, type='trigger', achieve='BlackbeanThreeTwoOne_start')
        self.write_log(logName='ThreeTwoOne_log', triggerId=9000, event='char_event', subEvent='BlackbeanThreeTwoOnegamestart') # 로그를 남기기 위한 행 : arg5가 트리거 전체에서 유니크한 값이 들어가야 하며, arg1은 코드에 남고 있지 않음(서바이벌일 때만 서바이벌 로그 불러옴)
        self.arcade_three_two_one3(type='StartGame', lifeCount=5, initScore=10000)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="1,1" arg4="120"/>
        self.set_user_value(triggerId=4001, key='Fail', value=1) # Fail Event on
        self.add_balloon_talk(spawnId=0, msg='$51000006_DG__51000006_MAIN__4$', duration=3000) # PC : 너한텐 안 져!
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_GetReadyGo_01') # 시작 효과음 / 레디-고! 들어간 버전 02100323

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드준비(self.ctx)


class 라운드준비(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트
        self.set_effect(triggerIds=[610], visible=False) # 이펙트 610: PC 머리 위 내리는 비 이펙트
        self.set_actor(triggerId=611, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈01끄기
        self.set_actor(triggerId=612, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈02끄기
        self.set_actor(triggerId=613, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈03끄기
        self.set_actor(triggerId=614, visible=False, initialSequence='0', arg4=False, arg5=False) # 미니빈04끄기
        self.set_pc_rotation(rotation=[0,0,0])

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(waitTick=500):
            return 라운드시작(self.ctx)


class 라운드시작(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=1, textId=26300736, duration=3000) # 26300736 가이드 텍스트 ON : [[icon:click]] 방향을 선택하세요.
        self.arcade_three_two_one3(type='StartRound', uiDuration=4, round=1) # uiDuration : 게임 UI (화살표) 노출 시간
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_ArrowPopup_01') # 화살표 Ui 팝업 효과음 02100325

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(waitTick=4000):
            return 라운드진행(self.ctx)


class 라운드진행(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$51000006_DG__51000006_MAIN__5$', duration=1800) # 블랙빈 대사 : 빙글빙글~!

    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=1):
            return 좌로돌아01(self.ctx)
        if self.random_condition(rate=1):
            return 뒤로돌아02(self.ctx)
        if self.random_condition(rate=1):
            return 우로돌아03(self.ctx)


class 좌로돌아01(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='ResultRound', resultDirection=1)
        self.set_npc_rotation(spawnId=101, rotation=270) # 블랙빈 왼쪽으로 돔 : 270도 = resultDirection 1
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 블랙빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 뒤로돌아02(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='ResultRound', resultDirection=2)
        self.set_npc_rotation(spawnId=101, rotation=180) # 블랙빈 뒤쪽으로 돔 : 180도 = resultDirection 2
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 블랙빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 우로돌아03(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='ResultRound', resultDirection=3)
        self.set_npc_rotation(spawnId=101, rotation=90) # 블랙빈 오른쪽으로 돔 : 90도 = resultDirection 3
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 블랙빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 결과연출(common.Trigger):
    def on_enter(self):
        self.init_npc_rotation(spawnIds=[101])
        self.set_pc_rotation(rotation=[0,0,0])
        self.set_effect(triggerIds=[601], visible=False) # 이펙트 601: 게임상대 - 11004718 블랙빈 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(triggerIds=[602], visible=False) # 이펙트 602: PC 머리 위 스포트라이트 이펙트 끄기
        self.set_effect(triggerIds=[603], visible=False) # 이펙트 603: 게임상대 - 11004718 블랙빈 머리 위 불꽃놀이 이펙트
        self.set_effect(triggerIds=[604], visible=False) # 이펙트 604: PC 머리 위 불꽃놀이 이펙트

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ThreeTwoOneResult', value=1):
            self.set_npc_emotion_sequence(spawnId=101, sequenceName='Dance_C_Ride', durationTick=3300)
            self.set_pc_emotion_loop(sequenceName='Emotion_Dance_E', duration=3300)
            self.set_effect(triggerIds=[602], visible=True)
            self.set_effect(triggerIds=[604], visible=True)
            self.add_balloon_talk(spawnId=101, msg='$51000006_DG__51000006_MAIN__6$', duration=3300)
            self.add_balloon_talk(msg='$51000006_DG__51000006_MAIN__7$', duration=3300)
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Correct_01')
            return 결과정산(self.ctx)
        if self.user_value(key='ThreeTwoOneResult', value=0):
            self.set_npc_emotion_sequence(spawnId=101, sequenceName='Event_Happy_A', durationTick=3300)
            self.set_effect(triggerIds=[601], visible=True)
            self.set_effect(triggerIds=[603], visible=True)
            self.set_effect(triggerIds=[610], visible=True)
            self.set_actor(triggerId=611, visible=True, initialSequence='Run_A')
            self.set_actor(triggerId=612, visible=True, initialSequence='Run_A')
            self.set_actor(triggerId=613, visible=True, initialSequence='Run_A')
            self.set_actor(triggerId=614, visible=True, initialSequence='Run_A')
            self.set_pc_emotion_sequence(sequenceNames=['Emotion_Fuss_A'])
            self.add_balloon_talk(spawnId=101, msg='$51000006_DG__51000006_MAIN__8$', duration=3300)
            self.add_balloon_talk(msg='$51000006_DG__51000006_MAIN__9$', duration=3300)
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Wrong_01')
            return 결과정산(self.ctx)


class 결과정산(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='ResultRound2', round=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return 라운드결과(self.ctx)


class 라운드결과(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='ClearRound', round=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드준비(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.arcade_three_two_one3(type='EndGame')
        self.move_user(mapId=51000006, portalId=44)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 진짜끝(self.ctx)


class 진짜끝(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8010, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01') # 끝나는 효과음 02100329 셋둘하나 전용

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완전끝(self.ctx)


class 완전끝(common.Trigger):
    pass


initial_state = 입장
