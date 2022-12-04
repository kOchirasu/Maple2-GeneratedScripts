""" trigger/51000004_dg/51000004_main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000004, portalId=10)
        self.create_monster(spawnIds=[101], animationEffect=False) # 101: 게임상대 - 11004557 핑크핑크 핑크빈

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=셋둘하나_스킵완료, action='nextState') # setsceneskip 1 set
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Walk_A', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 인트로00(self.ctx)


class 인트로00(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000004_DG__51000004_MAIN__0$') # 안녕? 난 게임을 좋아하는 핑크빈!\n지금부터 나랑 재밌게 놀자!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인트로01(self.ctx)


class 인트로01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000004_DG__51000004_MAIN__1$') # 나와 다른 방향을 선택하면 네가 이기고, \n같은 방향을 선택하면 지는 거야~!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인트로02(self.ctx)


class 인트로02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000004_DG__51000004_MAIN__2$') # 네가 다섯 번 지면 게임은 끝!\n지지 않고 오래 버티면 높은 점수를 받지!
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_01_I_Bore', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 인트로03(self.ctx)


class 인트로03(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip() # setsceneskip 1 close
        self.select_camera_path(pathIds=[8003,8004], returnView=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000004_DG__51000004_MAIN__3$') # 높은 순위를 기록하면 선물도 있으니까,\n자~ 지금 바로 도전하라고!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 게임시작_대기(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 셋둘하나_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=1.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 게임시작_대기(self.ctx)
        if not self.user_detected(boxIds=[9000]):
            return 연출종료(self.ctx)


class 게임시작_대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_achievement(triggerId=9000, type='trigger', achieve='PinkBeanThreeTwoOne_start')
        self.write_log(logName='PinkBeanThreeTwoOne_log', triggerId=9000, event='char_event', subEvent='gamestart') # lifeCount : 최대 사망 횟수
        self.arcade_three_two_one(type='StartGame', lifeCount=5, initScore=10000)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="1,1" arg4="120"/>
        self.set_user_value(triggerId=4001, key='Fail', value=1) # Fail Event on
        self.add_balloon_talk(spawnId=0, msg='$51000004_DG__51000004_MAIN__4$', duration=3000) # 좋아, 붙어 보자!
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_GetReadyGo_01') # 시작 효과음 / 레디-고! 음성 포함 02100323

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드준비(self.ctx)


class 라운드준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(waitTick=500):
            return 라운드시작(self.ctx)


class 라운드시작(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=1, textId=26300736, duration=3000) # 26300736 가이드 텍스트 ON : [[icon:click]] 방향을 선택하세요.
        self.arcade_three_two_one(type='StartRound', uiDuration=4, round=1) # uiDuration : 게임 UI (화살표) 노출 시간
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_ArrowPopup_01') # 화살표 Ui 팝업 효과음 02100325

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9000]):
            return 완전끝(self.ctx)
        if self.wait_tick(waitTick=4000):
            return 라운드진행(self.ctx)


class 라운드진행(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$51000004_DG__51000004_MAIN__5$', duration=1800) # 핑크빈 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=1):
            return 좌로돌아01(self.ctx)
        if self.random_condition(rate=1):
            return 뒤로돌아02(self.ctx)
        if self.random_condition(rate=1):
            return 우로돌아03(self.ctx)


class 좌로돌아01(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='ResultRound', resultDirection=1)
        self.set_npc_rotation(spawnId=101, rotation=270) # 핑크빈 왼쪽으로 돔 : 270도 = resultDirection 1
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 핑크빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 뒤로돌아02(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='ResultRound', resultDirection=2)
        self.set_npc_rotation(spawnId=101, rotation=180) # 핑크빈 뒤쪽으로 돔 : 180도 = resultDirection 2
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 핑크빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 우로돌아03(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='ResultRound', resultDirection=3)
        self.set_npc_rotation(spawnId=101, rotation=90) # 핑크빈 오른쪽으로 돔 : 90도 = resultDirection 3
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Turning_01') # 핑크빈 도는 효과음 2500밀리초 02100326

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 결과연출(self.ctx)


class 결과연출(trigger_api.Trigger):
    def on_enter(self):
        self.init_npc_rotation(spawnIds=[101])
        self.set_pc_rotation(rotation=[0,0,0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ThreeTwoOneResult', value=1):
            self.set_npc_emotion_loop(spawnId=101, sequenceName='Failure_A', duration=2700)
            self.set_pc_emotion_loop(sequenceName='Emotion_Dance_V', duration=2450)
            self.add_balloon_talk(spawnId=101, msg='$51000004_DG__51000004_MAIN__6$', duration=3000)
            self.add_balloon_talk(msg='$51000004_DG__51000004_MAIN__7$', duration=3000)
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Correct_01')
            return 결과정산(self.ctx)
        if self.user_value(key='ThreeTwoOneResult', value=0):
            self.set_npc_emotion_loop(spawnId=101, sequenceName='Dance_A', duration=2700)
            self.set_pc_emotion_sequence(sequenceNames=['Emotion_Fuss_A'])
            self.add_balloon_talk(spawnId=101, msg='$51000004_DG__51000004_MAIN__8$', duration=3000)
            self.add_balloon_talk(msg='$51000004_DG__51000004_MAIN__9$', duration=2700)
            self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Wrong_01')
            return 결과정산(self.ctx)


class 결과정산(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='ResultRound2', round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2300):
            return 라운드결과(self.ctx)


class 라운드결과(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='ClearRound', round=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 라운드준비(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.arcade_three_two_one(type='EndGame')
        self.move_user(mapId=51000004, portalId=44)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 진짜끝(self.ctx)


class 진짜끝(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=8010, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.play_system_sound_in_box(sound='System_PinkBeans_Arcade_Result_01') # 끝나는 효과음 02100329 핑크빈 셋둘하나 전용

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 완전끝(self.ctx)


class 완전끝(trigger_api.Trigger):
    pass


initial_state = 입장
