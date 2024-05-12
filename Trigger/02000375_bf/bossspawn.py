""" trigger/02000375_bf/bossspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 1페이지 졸구간에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False)
        # 2페이지에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portalId=7, visible=False, enable=False, minimapVisible=False)
        # 3페이지에 있는 나가기 포탈, 최초에는 감추기
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 난이도체크(self.ctx)


class 난이도체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_level(level=2):
            # 일반레이드 난이도로 던전입장을 했을 경우
            return 레이드(self.ctx)
        if self.dungeon_level(level=3):
            # 카오스 난이도로 던전입장을 했을 경우
            return 카오스레이드(self.ctx)
        if self.wait_tick(waitTick=2000):
            # 그냥 테스트용으로 맵코드로 바로 들어왔으면 카오스용 보스 등장
            return 카오스레이드(self.ctx)


class 레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2001], animationEffect=False) # 일반레이드 난이도용 칸두라 보스 호출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클리어_체크대기(self.ctx)


class 카오스레이드(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2101], animationEffect=False) # 카오스 난이도용 칸두라 보스 호출

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 클리어_체크대기(self.ctx)


class 클리어_체크대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='KanduraNormalDead', value=1):
            # 1페이지 변신전 칸두라가 스펙높은 유저에게 극딜 당해서 죽은 경우  AI_KanduraNormal.xml, AI_KanduraNormal_Chaos.xml 로 부터 KanduraNormalDead = 1신호를 받음
            return 클리어처리01(self.ctx)
        if self.user_value(key='ThirdPhaseEnd', value=1):
            # 칸두라가 변신 한 이후 죽은 경우  AI_KanduraBigBurster.xml, AI_KanduraBigBurster_Chaos.xml 로 부터 ThirdPhaseEnd = 1신호를 받음
            return 클리어처리01(self.ctx)


class 클리어처리01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            # 칸두라 죽은 애니가 나오는 시간 6초 정도 되니, 이 연출 다 나오고 클리어 처리함
            return 클리어처리02(self.ctx)


class 클리어처리02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[-1])
        # DungeonRoom.xlsx  의  clearType  trigger 로 설정한 경우 맵 트리거를 통해서 클리어 UI 띄우는 처리함
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 나가기포털생성(self.ctx)


class 나가기포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # move.xml  트리거에 BattleEnd = 1 신호 보내기
        self.set_user_value(triggerId=99999002, key='BattleEnd', value=1)
        self.set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249,3250,3251,3252,3253,3254,3255,3256,3257,3258,3259,3260,3261,3262,3263,3264,3265,3266,3267,3268,3269,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3280,3281,3282,3283,3284,3285,3286,3287,3288,3289,3290,3291,3292,3293,3294,3295,3296,3297,3298,3299,3300], visible=True, arg3=0, delay=0, scale=0)
        # 1페이지 왼쪽 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portalId=6, visible=True, enable=True, minimapVisible=True)
        # 1페이지 오른쪽 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        # 2페이지 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        # 3페이지 전투판에 등장하는 나가기 포탈 생성
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
