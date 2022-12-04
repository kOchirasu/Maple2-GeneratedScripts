""" trigger/02020098_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=10, visible=False, enable=False, minimapVisible=False) # 스타팅 부활 지점에서 바로 보스  전투판 근처로 가는 순간이동 포탈 최초에는 감추기, 10: 스타팅 지점에서 1페이지 전투판 근처로 도착
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # 전투판 근처로 가는 순간이동 포탈 최초에는 감추기, 20: 2페이지 전투판으로 도착하기, 30: 3페이지 도착하기
        self.set_portal(portalId=30, visible=False, enable=False, minimapVisible=False) # 전투판 근처로 가는 순간이동 포탈 최초에는 감추기, 30: 3페이지 도착하기
        self.set_mesh(triggerIds=[201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223], visible=False, arg3=0, delay=0, scale=0) # 몬스터는 밟고 플레이어는 밟지 못하는 트리거메쉬 설정하기
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178], visible=False, arg3=0, delay=0, scale=0) # 보스 전투판으로 진입하는 계단 트리거메쉬 처음에는 감추기
        self.set_mesh(triggerIds=[6501,6502,6503,6504,6505,6506,6507,6508,6509,6510,6511,6512,6513,6514,6515,6516,6517,6518,6519,6520,6521,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6536,6537,6538,6539,6540,6541,6542,6543,6544,6545,6546,6547,6548,6549,6550,6551,6552,6553,6554,6555,6556,6557,6558,6559,6560,6561,6562,6563,6564,6565,6566,6567,6568,6569,6570,6571,6572,6573,6574,6575,6576,6577,6578,6579,6580], visible=False, arg3=0, delay=0, scale=0) # 2페이즈 보스 전투판의 플레이어만 막는 투명벽 최초에는 Off 상태로 하기, 보스가 2페이지 전투 시작할 때 이 투명벽을 On 해야 함
        self.set_mesh(triggerIds=[6701,6702,6703,6704,6705,6706,6707,6708,6709,6710,6711,6712,6713,6714,6715,6716,6717,6718,6719,6720,6721,6722,6723,6724,6725,6726,6727,6728,6729], visible=False, arg3=0, delay=0, scale=0) # 3페이즈 보스 전투판의 플레이어만 막는 투명벽 최초에는 Off 상태로 하기, 보스가 3페이지 전투 시작할 때 이 투명벽을 On 해야 함
        self.set_user_value(key='StairsOkPass', value=0) # @중요!:  트리거가 순서대로 실행되면 좋은데 보스 HP가 급감되어 건너띄기 되어 순서대로 실행이 안될 경우 로직이 꼬일 수 있는데 그것을 방지하기 위한 변수임

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[10]):
            return 던전코드별보스등장(self.ctx)


class 던전코드별보스등장(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_id(dungeonId=23042003):
            return 어려움난이도보스등장(self.ctx)
        if self.dungeon_id(dungeonId=23043003):
            return 쉬움난이도보스등장(self.ctx)
        if self.wait_tick(waitTick=2000):
            return 어려움난이도보스등장(self.ctx)


class 어려움난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # 어려운 난이도의 인페르녹 등장
        self.create_monster(spawnIds=[97], animationEffect=False) # 어려운 난이도의 우호적 NPC 트리스탄 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹최초이미지대사연출(self.ctx)


class 쉬움난이도보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[98], animationEffect=False) # 쉬운 난이도의 인페르녹 등장
        self.create_monster(spawnIds=[96], animationEffect=False) # 쉬운 난이도의 우호적 NPC 트리스탄 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 인페르녹최초이미지대사연출(self.ctx)


class 인페르녹최초이미지대사연출(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23000150, illust='infernog_nomal', duration=9000, script='$02020098_BF__PopUpCinema__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


class 대기상태(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StairsOk', value=1): # 1페이즈 끝나서 보스가 바닥 큐브 파괴하면서 2페이즈로 넘어갈 때, AI_BalrogMagicBurster_Kritias.xml 인페르녹에게   2PhaseStart = 1 신호를 받으면 이 부분 실행
            return 계단생성시작중(self.ctx)
        if self.user_value(key='2PhaseStart', value=1): # 2페이즈 끝나서 보스가 바닥 큐브 파괴하면서  3페이즈로 넘어갈 때, AI_BalrogMagicBurster_Kritias.xml 인페르녹에게   3PhaseStart = 1 신호를 받으면 이 부분 실행
            return 페이지_바로가기포탈생성2(self.ctx)
        if self.user_value(key='3PhaseStart', value=1):
            return 페이지_바로가기포탈생성3(self.ctx)


class 계단생성시작중(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='StairsOk', value=0) # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StairsOkPass', value=0):
            return 계단생성(self.ctx)
        if self.user_value(key='StairsOkPass', value=1):
            return 대기상태(self.ctx)


class 계단생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[198,199], visible=False, arg3=0, delay=0, scale=0) # 최초에 설치된 계단 진입로 투명벽, 계단이 생성되면서 제거하기
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178], visible=True, arg3=1, delay=50, scale=0.5) # 계단 트리거메쉬 생성
        self.set_portal(portalId=10, visible=True, enable=True, minimapVisible=True) # 스타트 지점에서  1페이지 전투판 바로 가는 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 대기상태(self.ctx)


class 페이지_바로가기포탈생성2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[125,116,168,126], visible=False, arg3=0, delay=50, scale=0.5) # 비주얼적인 이슈로 이 4개 트리거메쉬 제일 먼저 제거함
        self.set_user_value(key='2PhaseStart', value=0) # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=True) # 2페이지 전투판 바로 가는 포탈 생성
        self.set_mesh(triggerIds=[198,199], visible=True, arg3=1, delay=1, scale=1) # 1페이지 진입 계단 사라졌으니, 계단 진입로의 투명벽으로 다시 막기
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178], visible=False, arg3=0, delay=50, scale=0.5) # 2페이지 시작할 때 1페이지 전투판 파괴하기 때문에 1페이지 진입하는 계단 제거하기
        self.set_user_value(key='StairsOkPass', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6300):
            return 페이지_2PhaseWall_생성2(self.ctx)


class 페이지_2PhaseWall_생성2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6501,6502,6503,6504,6505,6506,6507,6508,6509,6510,6511,6512,6513,6514,6515,6516,6517,6518,6519,6520,6521,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6536,6537,6538,6539,6540,6541,6542,6543,6544,6545,6546,6547,6548,6549,6550,6551,6552,6553,6554,6555,6556,6557,6558,6559,6560,6561,6562,6563,6564,6565,6566,6567,6568,6569,6570,6571,6572,6573,6574,6575,6576,6577,6578,6579,6580], visible=True, arg3=1, delay=1, scale=1) # 플레이어 추락 하여 2페이지 전투판 도착할 때 쯤 2PhaseWall  투명벽 생성함
        self.set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016,6017,6018,6019,6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033,6034,6035,6036,6037,6038,6039,6040,6041,6042,6043,6044,6045,6046,6047,6048,6049,6050,6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066,6067,6068,6069,6070,6071,6072], visible=False, arg3=0, delay=0, scale=0) # 1페이지 전투판이 전부 파괴되니 1페이지용 1PhaseWall 투명벽은 제거함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


class 페이지_바로가기포탈생성3(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=60, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=61, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=62, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=63, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=64, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=65, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_portal(portalId=66, visible=False, enable=False, minimapVisible=False) # 2페이지 드랍때 전투판 밖으로 떨어지는 플레이어 체크하는 포탈 3페이지 시작할때 꼭 제거하기
        self.set_user_value(key='3PhaseStart', value=0) # 무한 루프 빠지는 것을 막기 위해 이 변수 0 초기화 하기, 이후 이 변수 다시 사용할 일 없음
        self.set_portal(portalId=30, visible=True, enable=True, minimapVisible=True) # 3페이지 전투판 바로 가는 포탈 생성
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False) # 3페이지 시작할 때 2페이지 전투판 파괴하기 때문에 2페이지 가는 포탈 제거함, 이거 안하면 버그 생김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6300):
            return 페이지_3PhaseWall_생성3(self.ctx)


class 페이지_3PhaseWall_생성3(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[6701,6702,6703,6704,6705,6706,6707,6708,6709,6710,6711,6712,6713,6714,6715,6716,6717,6718,6719,6720,6721,6722,6723,6724,6725,6726,6727,6728,6729], visible=True, arg3=1, delay=1, scale=1) # 플레이어 추락 하여 3페이지 전투판 도착할 때 쯤 3PhaseWall  투명벽 생성함
        self.set_mesh(triggerIds=[6501,6502,6503,6504,6505,6506,6507,6508,6509,6510,6511,6512,6513,6514,6515,6516,6517,6518,6519,6520,6521,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6536,6537,6538,6539,6540,6541,6542,6543,6544,6545,6546,6547,6548,6549,6550,6551,6552,6553,6554,6555,6556,6557,6558,6559,6560,6561,6562,6563,6564,6565,6566,6567,6568,6569,6570,6571,6572,6573,6574,6575,6576,6577,6578,6579,6580], visible=False, arg3=0, delay=0, scale=0) # 2페이지 전투판이 전부 파괴되니 2페이지용 2PhaseWall 투명벽은 제거함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기상태(self.ctx)


initial_state = 시작대기중
