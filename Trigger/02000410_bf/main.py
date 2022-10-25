""" trigger/02000410_bf/main.xml """
import common


class Ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6010,6011], visible=True, arg3=1, delay=1) # 맨 오른쪽 지점에서 대포 배치하기 위한 오프젝트 생성하기 , TriggerObjectID: 6010, 6011
        self.set_mesh(triggerIds=[6000,6001,6002,6003], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_mesh(triggerIds=[6004,6005], visible=False) # 몬스터는 밟을 수 있고 플레이어는 밟을 수 없는 투명벽 설정하기
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 던전 나가기 위한 포탈 초기화 설정,   arg1="1" 은 포탈ID, 전투판에 있는 포탈
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 던전 나가기 위한 포탈 초기화 설정,   arg1="2" 은 포탈ID, 안전 부활 지점에 있는 포탈

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=750, boxId=1):
            return 전투시작_인페르녹전함(self.ctx)


class 전투시작_인페르녹전함(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 인페르녹 전함 스폰하기, 스폰ID : 101
        self.dungeon_set_lap_time(id=1, lapTime=420000) # 월드인베이젼 던전 Type에서 사용하는 보스 HP바 위에 있는 타임 게이지UI 위에 보스 등장을 알리는 첫번째 아이콘을 띄우며 어느 위치에 띄울지를 정의하는 부분, 15분 즉 900000을 풀 게이지 기준으로 어느 위치에 띄울지를 정의함
        self.dungeon_set_lap_time(id=2, lapTime=720000) # 월드인베이젼 던전 Type에서 사용하는 보스 HP바 위에 있는 타임 게이지UI 위에 보스 폭주를 알리는 두번째 아이콘을 띄우며 어느 위치에 띄울지를 정의하는 부분, 15분 즉 900000을 풀 게이지 기준으로 어느 위치에 띄울지를 정의함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째페이즈_인페르녹전함(self.ctx)


class 첫번째페이즈_인페르녹전함(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SecondPhase', value=1):
            return 두번째페이즈_인페르녹전함(self.ctx)


class 두번째페이즈_인페르녹전함(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6010,6011,6012,6013,6014,6015,6016], visible=False, arg3=0, delay=0, scale=0.5) # 맨 오른쪽 건너편 막힌 벽 제거하기 ,    오른쪽 지점 대포 배치하기 위한 오프젝트는 TriggerObjectID: 6010, 6011  이거 제거해야 전투가 쾌적함
        self.dungeon_mission_complete(feature='DungeonRankBalance_01', missionId=24090007) # ## 한국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호
        self.dungeon_mission_complete(feature='DungeonRankBalance_02', missionId=24090017) # ## 중국용 던전랭크 코드: 인페르녹의 전함 측면파괴 던전랭크 달성을 위한 신호

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ThirdPhase', value=1):
            return 세번째페이즈_인페르녹등장(self.ctx)


class 세번째페이즈_인페르녹등장(common.Trigger):
    def on_enter(self):
        self.dungeon_move_lap_time_to_now(id=1)
        # 위에서 선언한   <action name="DungeonSetLapTime" id="1" lapTime="420000" /> 의 첫번째 아이콘을(id="1") 현재 시간 기준 게이지 위치로 옮기고자 할때 이렇게 설정
        self.create_monster(spawnIds=[102], animationEffect=True) # 인페르녹 보스 스폰하기, 스폰ID : 102
        self.set_sound(triggerId=8410, enable=True) # 보스 등장하면 보스용 BGM으로 교체하기

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='BalrogMagicBursterBattlePhase', value=1):
            return 인페르녹전투시작(self.ctx)


class 인페르녹전투시작(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='Phase', value=1) # 트리거에서 인페르녹 보스 AI에게  Phase = 1 신호를 보내서, 행동에 영향 받도록 함

    def on_tick(self) -> common.Trigger:
        if self.dungeon_check_play_time(playSeconds=720):
            return 네번째페이즈_인페르녹광폭화(self.ctx)


class 네번째페이즈_인페르녹광폭화(common.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='Phase', value=2) # 트리거에서 인페르녹 보스 AI에게  Phase = 2 신호를 보내서, 광폭화 공격 스킬 사용하도록 함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Ready
