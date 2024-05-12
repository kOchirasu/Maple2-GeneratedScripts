""" trigger/81000003_item/trigger_03.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='59', seconds=180, startDelay=1, interval=1, vOffset=-90, desc='wait.xml 시작 타이머 설정 UI') # 3분 후 시작

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[402]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=999, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        """
        if self.count_users(boxId=402, minUsers='20'):
            return 어나운스0(self.ctx)
        """
        if self.wait_tick(waitTick=180000):
            # 3분 후 시작
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='ME_Trigger_03_00')
        self.set_event_ui(type=1, arg2='$61000006_ME__TRIGGER_03__0$', arg3='4000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_count_ui(text='$61000006_ME__TRIGGER_03__1$', stage=0, count=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=999111, key='gameStart', value=1)
        self.set_timer(timerId='160', seconds=160, startDelay=0, interval=1, desc='trigger_03.xml 시작 타이머 설정')
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=False)
        self.set_interact_object(triggerIds=[10000224], state=1)
        self.set_interact_object(triggerIds=[10000214], state=1)
        # self.set_achievement(triggerId=402, type='trigger', achieve='dailyquest_start')
        # 길드 경험치 지급 / boxID="타겟박스id", 0이면 맵전체, type="GuildGainExp의 id" 2가 매시브이벤트
        # self.give_guild_exp(boxId=0, type=2)
        self.start_mini_game(isShowResultUI=False, boxId=499, round=1, gameName='UserMassive_Crazyrunner')
        self.start_mini_game_round(boxId=499, round=1)
        self.move_user_to_box(boxId=400, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='160'):
            return 경기종료(self.ctx)


class 경기종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_achievement(triggerId=401, type='trigger', achieve='crazyrunner_win')
        # self.mini_game_camera_direction(boxId=401, cameraId=301)
        self.set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        self.set_event_ui(type=4, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        self.add_buff(boxIds=[401], skillId=70000132, level=1)
        # self.set_event_ui(type=5, arg2='$61000004_ME__TRIGGER_01__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            self.end_mini_game_round(winnerBoxId=401, expRate=0.13333334, isGainLoserBonus=True, gameName='UserMassive_Crazyrunner') # 승리자 및 실패자도 경험치 지급함
            self.end_mini_game(winnerBoxId=401, gameName='UserMassive_Crazyrunner')
            # self.set_local_camera(cameraId=301, enable=False)
            return 강제이동(self.ctx)


class 강제이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 입장
