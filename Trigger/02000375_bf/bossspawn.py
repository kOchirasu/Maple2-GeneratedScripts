""" trigger/02000375_bf/bossspawn.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False) # 2페이지에 있는 나가기 포탈, 최초에는 감추기
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False) # 3페이지에 있는 나가기 포탈, 최초에는 감추기
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 난이도체크()


class 난이도체크(state.State):
    def on_tick(self) -> state.State:
        if dungeon_level(level=2):
            return 레이드()
        if dungeon_level(level=3):
            return 카오스레이드()
        if wait_tick(waitTick=2000):
            return 카오스레이드()


class 레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False) # 일반레이드 난이도용 칸두라 보스 호출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클리어_체크대기()


class 카오스레이드(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2101], arg2=False) # 카오스 난이도용 칸두라 보스 호출

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클리어_체크대기()


class 클리어_체크대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='KanduraNormalDead', value=1):
            return 클리어처리01()
        if user_value(key='ThirdPhaseEnd', value=1):
            return 클리어처리01()


class 클리어처리01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 클리어처리02()


class 클리어처리02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        dungeon_clear() # DungeonRoom.xlsx  의  clearType  trigger 로 설정한 경우 맵 트리거를 통해서 클리어 UI 띄우는 처리함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 나가기포털생성()


class 나가기포털생성(state.State):
    def on_enter(self):
        set_user_value(triggerId=99999002, key='BattleEnd', value=1) # move.xml  트리거에 BattleEnd = 1 신호 보내기
        set_mesh(triggerIds=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212,3213,3214,3215,3216,3217,3218,3219,3220,3221,3222,3223,3224,3225,3226,3227,3228,3229,3230,3231,3232,3233,3234,3235,3236,3237,3238,3239,3240,3241,3242,3243,3244,3245,3246,3247,3248,3249,3250,3251,3252,3253,3254,3255,3256,3257,3258,3259,3260,3261,3262,3263,3264,3265,3266,3267,3268,3269,3270,3271,3272,3273,3274,3275,3276,3277,3278,3279,3280,3281,3282,3283,3284,3285,3286,3287,3288,3289,3290,3291,3292,3293,3294,3295,3296,3297,3298,3299,3300], visible=True, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True) # 1페이지 왼쪽 전투판에 등장하는 나가기 포탈 생성
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True) # 1페이지 오른쪽 전투판에 등장하는 나가기 포탈 생성
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True) # 2페이지 전투판에 등장하는 나가기 포탈 생성
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True) # 3페이지 전투판에 등장하는 나가기 포탈 생성
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


