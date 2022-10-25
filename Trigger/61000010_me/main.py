""" trigger/61000010_me/main.xml """
import common


class 입장(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return 어나운스0(self.ctx)
        if self.user_value(key='GameStart', value=1):
            return 어나운스0(self.ctx)


class 어나운스0(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$61000010_ME__main__0$', arg3='3000', arg4='0')
        self.set_achievement(triggerId=101, type='trigger', achieve='ShanghaiRunnersStart')
        # <action name="SetLocalCamera" cameraId="302" enable="0"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 어나운스1(self.ctx)


class 어나운스1(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$61000006_ME__TRIGGER_03__1$', stage=0, count=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='99', seconds=190, startDelay=0, interval=1)
        self.set_mesh(triggerIds=[3000,3001,3002,3003], visible=False)
        self.set_user_value(triggerId=999111, key='gameStart', value=1)
        self.start_mini_game(boxId=199, round=1, gameName='shanghairunner')
        self.start_mini_game_round(boxId=199, round=1)
        self.move_user_to_box(boxId=101, portalId=1)
        self.set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start')
        self.give_guild_exp(boxId=0, type=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='99'):
            return 경기종료(self.ctx)


class 경기종료(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=3, arg2='$61000006_ME__TRIGGER_03__2$', arg3='5000', arg4='401')
        self.set_event_ui(type=6, arg2='$61000006_ME__TRIGGER_03__3$', arg3='5000', arg4='!401')
        # <action name="버프를걸어준다" arg1="199" arg2="70000019" arg3="1"/>

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.end_mini_game_round(winnerBoxId=102, expRate=0.25, isGainLoserBonus=True)
            self.mini_game_give_reward(winnerBoxId=102, contentType='MiniGameType2')
            self.end_mini_game(winnerBoxId=102, gameName='shanghairunner')
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 입장
