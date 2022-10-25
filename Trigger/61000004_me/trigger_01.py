""" trigger/61000004_me/trigger_01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_mesh(triggerIds=[301,302,303], visible=True, arg3=0, delay=0)
        self.set_mesh(triggerIds=[3101,3102,3201,3202,3301,3302,3401,3402,3403,3404], visible=False, arg3=0, delay=0)
        self.set_effect(triggerIds=[71011], visible=False)
        self.set_effect(triggerIds=[71012], visible=False)
        self.set_effect(triggerIds=[71021], visible=False)
        self.set_effect(triggerIds=[71022], visible=False)
        self.set_effect(triggerIds=[72011], visible=False)
        self.set_effect(triggerIds=[72021], visible=False)
        self.set_effect(triggerIds=[73011], visible=False)
        self.set_effect(triggerIds=[73021], visible=False)
        self.set_effect(triggerIds=[73022], visible=False)
        self.set_effect(triggerIds=[73023], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 랜덤블록01(self.ctx)


class 랜덤블록01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[71011], visible=True)
            self.set_effect(triggerIds=[71012], visible=True)
            return 랜덤블록02(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[71021], visible=True)
            self.set_effect(triggerIds=[71022], visible=True)
            return 랜덤블록02(self.ctx)


class 랜덤블록02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3201], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[72011], visible=True)
            return 랜덤블록03(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3202], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[72021], visible=True)
            return 랜덤블록03(self.ctx)


class 랜덤블록03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3301], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[73011], visible=True)
            return 랜덤블록04(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3302], visible=True, arg3=0, delay=0)
            self.set_effect(triggerIds=[73021], visible=True)
            self.set_effect(triggerIds=[73022], visible=True)
            self.set_effect(triggerIds=[73023], visible=True)
            return 랜덤블록04(self.ctx)


class 랜덤블록04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3401,3402], visible=True, arg3=0, delay=0)
            return 시작조건체크(self.ctx)
        if self.random_condition(rate=50):
            self.set_mesh(triggerIds=[3403,3404], visible=True, arg3=0, delay=0)
            return 시작조건체크(self.ctx)


class 시작조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=60000):
            return 어나운스0(self.ctx)
        if self.count_users(boxId=101, boxId=20):
            return 어나운스0(self.ctx)


class 어나운스0(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='ME_Trigger_01_00')
        self.set_event_ui(type=1, arg2='$61000004_ME__TRIGGER_01__0$', arg3='7000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 어나운스1(self.ctx)


# 전체 box : 105
# 대기 box : 101
# 승자 box : 102
class 어나운스1(common.Trigger):
    def on_enter(self):
        self.show_count_ui(text='$61000004_ME__TRIGGER_01__1$', stage=0, count=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5500):
            self.set_mesh(triggerIds=[301,302,303], visible=False, arg3=12, delay=0)
            self.set_achievement(triggerId=101, type='trigger', achieve='dailyquest_start')
            self.give_guild_exp(boxId=0, type=2)
            self.start_mini_game(boxId=105, round=1, gameName='escape')
            self.start_mini_game_round(boxId=105, round=1)
            self.move_user_to_box(boxId=101, portalId=1)
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999111, key='gameStart', value=1)
        self.set_timer(timerId='180', seconds=180, startDelay=0, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='180'):
            return 경기종료(self.ctx)


class 경기종료(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=102, type='trigger', achieve='escape_win')
        # action name="MiniGameCameraDirection" boxId="102" cameraId="901" /
        self.set_event_ui(type=3, arg2='$61000004_ME__TRIGGER_01__2$', arg3='5000', arg4='102')
        self.set_event_ui(type=6, arg2='$61000004_ME__TRIGGER_01__3$', arg3='5000', arg4='!102')
        self.add_buff(boxIds=[102], skillId=70000019, level=1)
        # action name="이벤트UI를설정한다" arg1="5" arg2="$61000004_ME__TRIGGER_01__2$" arg3="3000" arg4="0" /

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            self.end_mini_game_round(winnerBoxId=102, expRate=0.25, isGainLoserBonus=True)
            self.mini_game_give_reward(winnerBoxId=102, contentType='miniGame')
            self.end_mini_game(winnerBoxId=102, gameName='escape')
            return 강제이동(self.ctx)


class 강제이동(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=15000):
            self.move_user(mapId=0, portalId=0)
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
