""" trigger/99999912/01_movetest.xml """
import common


class Init(common.Trigger):
    def on_enter(self):
        self.create_field_game(type='GuildVsGame')
        self.user_tag_symbol(symbol1='guild_game_red', symbol2='guild_game_blue')

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=9000, boxId=1, operator='>=', userTagId=1):
            return Wait(self.ctx)


class Wait(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10001129], state=1)
        self.set_interact_object(triggerIds=[10001130], state=1)
        self.set_interact_object(triggerIds=[10001131], state=1)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return Move01(self.ctx)


class Move01(common.Trigger):
    def on_enter(self):
        self.debug_string(string='강제이동 트리거가 발동됩니다.')
        # <action name="MoveToPortal" boxId="9000" userTagId="1" portalId="1"  />
        # <action name="MoveToPortal" boxId="9000" userTagId="2" portalId="2"  />
        # desc 속성은 설명을 위해서 적어둔 것이니 사용할때는 지우고 사용해주시면 됩니다.
        self.move_to_portal(userTagId=1, portalId=1)
        self.move_to_portal(userTagId=2, portalId=2)
        self.show_event_result(type='notice', text='1팀 안녕?\n줄바꿈확인', duration=3000, userTagId=1)
        self.show_event_result(type='notice', text='2팀 안녕?\n줄바꿈확인', duration=3000, userTagId=2)
        self.play_system_sound_by_user_tag(userTagId=1, soundKey='System_ShowGuideSummary_01')
        self.play_system_sound_by_user_tag(userTagId=2, soundKey='System_PartTimeJob_Right_01')
        self.guild_vs_game_score_by_user(boxId=9000, score=1, desc='9000 트리거 박스 안의 유저수가 많은 팀에 1점을 추가한다.')
        self.guild_vs_game_give_reward(type='exp', teamId=1, isWin=True, desc='길드 경험치를 지급한다.')
        self.guild_vs_game_give_reward(type='fund', teamId=1, isWin=True, desc='길드 기금을 지급한다.')
        self.guild_vs_game_give_contribution(teamId=1, isWin=True, desc='길드 기여도를 지급한다.')
        self.guild_vs_game_give_reward(type='exp', teamId=2, isWin=False, desc='길드 경험치를 지급한다.')
        self.guild_vs_game_give_reward(type='fund', teamId=2, isWin=False, desc='길드 기금을 지급한다.')
        self.guild_vs_game_give_contribution(teamId=2, isWin=False, desc='길드 기여도를 지급한다.')
        self.guild_vs_game_result(desc='결과창을 출력')
        self.guild_vs_game_log_result(desc='로그를 남긴다')
        self.guild_vs_game_log_won_by_default(teamId=1, desc='1팀의 부전승 보상 로그를 남긴다.')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return PrintWinnerTeam(self.ctx)


class PrintWinnerTeam(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.guild_vs_game_scored_team(teamId=1):
            self.debug_string(string='1팀이 득점 했습니다')
            return Reset(self.ctx)
        if self.guild_vs_game_scored_team(teamId=2):
            self.debug_string(string='2팀이 득점 했습니다')
            return Reset(self.ctx)
        if self.guild_vs_game_scored_team(teamId=0):
            self.debug_string(string='아직 득점한 팀이 없습니다.')
            return Reset(self.ctx)


class Reset(common.Trigger):
    def on_enter(self):
        self.debug_string(string='트리거 초기화')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Wait(self.ctx)


initial_state = Init
