""" trigger/61000029_me/61000029_main.xml """
from common import *
import state


#  None 
class StateNone(state.State):
    def on_enter(self):
        create_field_game(type='HideAndSeek', reset=True) # TriggerID 시작
        field_game_constant(key='BeginTriggerID', value='1') # TriggerID 끝
        field_game_constant(key='EndTriggerID', value='36') # 숨바꼭질 플레이를 위한 최소 유저수
        field_game_constant(key='RequireUserCount', value='2') # 숨바꼭질 플레이어 입장 대기 시간
        field_game_constant(key='EnterableSeconds', value='60') # 숨바꼭질 게임룰 설명 시간
        field_game_constant(key='GameRuleNoticeTick', value='10000') # 방폭 진행 소요 시간
        field_game_constant(key='ShortOfUserTick', value='10000') # 편 나누기 소요 시간
        field_game_constant(key='DivideTeamsSeconds', value='5') # 유저가 게임포탈로 이동할 동안 카메라 무빙 소요 시간
        field_game_constant(key='MoveGameAreaTick', value='2000') # 사물팀 숨는 소요 시간
        field_game_constant(key='BeInHidingTeamsSeconds', value='30') # 술래팀 사물찾는데 소요 시간
        field_game_constant(key='LookingForATeamsSeconds', value='150') # 승패 알림 소요 시간
        field_game_constant(key='TeamMatchResultTick', value='15000') # 숨바꼭질 게임종료 설명 시간
        field_game_constant(key='GameExitNoticeTick', value='10000') # 사물팀 경험치 할당 주기
        field_game_constant(key='HideTeamExpDurationTick', value='30000') # 술래팀 무적 시간 (전체 시간에서 아래 시간 만큼 남았을때 발동.)
        field_game_constant(key='SeekTeamInvincibleTick', value='20000') # 술래팀 무적 안내 시간
        field_game_constant(key='InvincibleNoticeTick', value='7000') # 술래팀 무적 안내 메세지
        field_game_constant(key='InvincibleMessage', value='$61000023_ME__61000023_MAIN__6$') # 대기지역 포탈 아이디
        field_game_constant(key='PortalWaitAreaID', value='1') # 게임지역 포탈 아이디
        field_game_constant(key='PortalGameAreaID', value='10') # 탈락지역 포탈 아이디
        field_game_constant(key='PortalFailAreaID', value='20') # 술래팀이 사용하는 SkillSet
        field_game_constant(key='SeekTeamSkillSetID', value='99930041') # 사물팀 경험치
        field_game_constant(key='HideTeamExp', value='0') # 술래팀 경험치
        field_game_constant(key='SeekTeamExp', value='0') # KR 승리팀 보상 id, rank, count
        field_game_constant(key='WinnerRewardItemID', value='30001442', feature='MassiveHideAndSeek', locale='KR')
        field_game_constant(key='WinnerRewardItemRank', value='1', feature='MassiveHideAndSeek', locale='KR')
        field_game_constant(key='WinnerRewardItemCount', value='3', feature='MassiveHideAndSeek', locale='KR') # KR 패배팀 보상 id, rank, count
        field_game_constant(key='LoserRewardItemID', value='30001442', feature='MassiveHideAndSeek', locale='KR')
        field_game_constant(key='LoserRewardItemRank', value='1', feature='MassiveHideAndSeek', locale='KR')
        field_game_constant(key='LoserRewardItemCount', value='1', feature='MassiveHideAndSeek', locale='KR') # CN 승리팀 보상 id, rank, count
        field_game_constant(key='WinnerRewardItemID', value='30001446', feature='MassiveHideAndSeek', locale='CN')
        field_game_constant(key='WinnerRewardItemRank', value='1', feature='MassiveHideAndSeek', locale='CN')
        field_game_constant(key='WinnerRewardItemCount', value='3', feature='MassiveHideAndSeek', locale='CN') # CN 패배팀 보상 id, rank, count
        field_game_constant(key='LoserRewardItemID', value='30001446', feature='MassiveHideAndSeek', locale='CN')
        field_game_constant(key='LoserRewardItemRank', value='1', feature='MassiveHideAndSeek', locale='CN')
        field_game_constant(key='LoserRewardItemCount', value='1', feature='MassiveHideAndSeek', locale='CN') # 관전 CameraID
        field_game_constant(key='WatchCameraID', value='101') # 데일리 이벤트
        field_game_constant(key='EventDailyQuestStart', value='dailyquest_start') # 숨바꼭질 참여 이벤트
        field_game_constant(key='EventHideAndSeekStart', value='hideandseek_start') # 숨바꼭질 승리 이벤트
        field_game_constant(key='EventHideAndSeekWin', value='hideandseek_win')

    def on_tick(self) -> state.State:
        if user_value(key='WaitForEnterUser', value=1):
            return WaitForEnterUser()


#  유저를 대기 한다. 
class WaitForEnterUser(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if user_value(key='GameRuleNotice', value=1):
            return GameRuleNotice()
        if user_value(key='ShortOfUser', value=1):
            return ShortOfUser()
        if wait_and_reset_tick(waitTick=5000):
            show_guide_summary(entityId=26500301, textId=26500301, duration=4500)
            return None

    def on_exit(self):
        reset_timer(timerId='1')
        hide_guide_summary(entityId=26500301)


#  게임룰을 설명한다. 
class GameRuleNotice(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000023_ME__61000023_MAIN__1$', arg3='10000')

    def on_tick(self) -> state.State:
        if user_value(key='DivideIntoTeams', value=1):
            return DivideIntoTeams()


#  팀 나누기 
class DivideIntoTeams(state.State):
    def on_enter(self):
        show_count_ui(text='$61000023_ME__61000023_MAIN__0$', stage=0, count=5)

    def on_tick(self) -> state.State:
        if user_value(key='MoveGameArea', value=1):
            return MoveGameArea()
        if user_value(key='ShortOfUser', value=1):
            return ShortOfUser()


#  유저가 게임포탈로 이동할 동안 카메라 무빙 
class MoveGameArea(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BeInHidingTeams', value=1):
            return BeInHidingTeams()
        if user_value(key='ShortOfUser', value=1):
            return ShortOfUser()


#  사물로 숨기 
class BeInHidingTeams(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=True, display=True)
        field_game_message(custom=1, type='SetEventUI', arg1=1, script='$61000023_ME__61000023_MAIN__2$', duration=30000)
        field_game_message(custom=2, type='SetEventUI', arg1=1, script='$61000023_ME__61000023_MAIN__3$', duration=30000)

    def on_tick(self) -> state.State:
        if user_value(key='LookingForATeams', value=1):
            return LookingForATeams()
        if user_value(key='TeamMatchResult', value=1):
            return TeamMatchResult()

    def on_exit(self):
        reset_timer(timerId='1')


#  술래잡기 시작 
class LookingForATeams(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=150, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if user_value(key='TeamMatchResult', value=1):
            return TeamMatchResult()

    def on_exit(self):
        reset_timer(timerId='1')


#  숨바꼭질 승패 결정 
class TeamMatchResult(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GameExitNotice', value=1):
            return GameExitNotice()


#  게임종료를 설명한다. 
class GameExitNotice(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000023_ME__61000023_MAIN__4$', arg3='10000')

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return End()


#  플레이어 부족으로 방폭 메세지 
class ShortOfUser(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$61000023_ME__61000023_MAIN__5$', arg3='10000')

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return End()


#  게임종료 
class End(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


