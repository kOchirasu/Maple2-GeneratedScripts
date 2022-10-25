""" trigger/81000003_item/trigger_03.xml """
import common


class 입장(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='59', seconds=180, startDelay=1, interval=1, vOffset=-90, desc='wait.xml 시작 타이머 설정 UI') # 3분 후 시작

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[402]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=999, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=180000):
            return 어나운스0(self.ctx)
        """
        <condition name="여러명의유저를감지했으면" arg1="402" arg2="20">
                    <transition state="어나운스0" />
                </condition>
        """


class 어나운스0(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='ME_Trigger_03_00')
        self.set_event_ui(type=1, arg2='$61000006_ME__TRIGGER_03__0$', arg3='4000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 어나운스1(self.ctx)


class 어나운스1(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$61000006_ME__TRIGGER_03__1$', stage=0, count=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999111, key='gameStart', value=1)
        self.set_timer(timerId='160', seconds=160, startDelay=0, interval=1, desc='trigger_03.xml 시작 타이머 설정')
        self.set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509], visible=False)
        self.set_interact_object(triggerIds=[10000224], state=1)
        self.set_interact_object(triggerIds=[10000214], state=1)
        # <action name="업적이벤트를발생시킨다" arg1="402" arg2="trigger" arg3="dailyquest_start"/>
        self.start_mini_game(isShowResultUI=False, boxId=499, round=1, gameName='UserMassive_Crazyrunner')
        self.start_mini_game_round(boxId=499, round=1)
        self.move_user_to_box(boxId=400, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='160'):
            return 경기종료(self.ctx)


class 경기종료(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        self.set_event_ui(type=4, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        self.add_buff(boxIds=[401], skillId=70000132, level=1)
        # action name="이벤트UI를설정한다" arg1="5" arg2="$61000004_ME__TRIGGER_01__2$" arg3="3000" arg4="0" /

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.end_mini_game_round(winnerBoxId=401, expRate=0.13333334, isGainLoserBonus=True, gameName='UserMassive_Crazyrunner')
            self.end_mini_game(winnerBoxId=401, gameName='UserMassive_Crazyrunner')
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 입장
