""" trigger/02020120_bf/bgmchangeskillbreakreset.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_portal(portalId=1220, visible=False, enabled=False, minimapVisible=False) # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 초기화 시키기
        set_user_value(key='SkillBreakStart', value=0) # SkillBreakStart 변수 0으로 초기화
        set_user_value(key='DungeonReset', value=0) # DungeonReset 변수 0으로 초기화

    def on_tick(self) -> state.State:
        if count_users(boxId=299, boxId=1):
            return 던전시간작동대기()


class 던전시간작동대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=399, boxId=1):
            return 스킬브레이크신호대기_BGM교체()
        if user_value(key='BgmChangeTriggerCancel', value=1):
            return 종료()


class 스킬브레이크신호대기_BGM교체(state.State):
    def on_enter(self):
        set_sound(triggerId=19600, arg2=True) # 보스 메인 전투판으로 들어서면 보스용 BGM으로 교체하기, 스킬브레이크 막기 실패해서 원래 BGM으로 되돌리는 초기화 설정은 bossSpawn.xml 에 있음

    def on_tick(self) -> state.State:
        if user_value(key='SkillBreakStart', value=1, operator='GreaterEqual'):
            return 스킬브레이크로직작동()


class 스킬브레이크로직작동(state.State):
    def on_enter(self):
        set_portal(portalId=6201, visible=False, enabled=False, minimapVisible=False) # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 이때 감추기, 이 포탈 PortalStage06Boss.xml 에서도 사용함

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 스킬브레이크실패초기화처리()


class 스킬브레이크실패초기화처리(state.State):
    def on_enter(self):
        set_portal(portalId=1220, visible=True, enabled=True, minimapVisible=True) # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 활성화 시키기

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 스킬브레이크실패연출출력()


class 스킬브레이크실패연출출력(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonReset', value=1):
            return Ready()


class 종료(state.State):
    pass


#  여기 아래는 사용 안함
class 보스한테보내는포탈생성(state.State):
    def on_enter(self):
        set_portal(portalId=6201, visible=True, enabled=True, minimapVisible=True) # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 생성시키기, 이 포탈 PortalStage06Boss.xml 에서도 사용함
        set_portal(portalId=1220, visible=False, enabled=False, minimapVisible=False) # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 다시 감추기
        set_user_value(key='SkillBreakStart', value=0) # SkillBreakStart 변수 0으로 초기화

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: 스킬브레이크신호대기_시간다시셋팅


class 보스한테보내는포탈생성_시간초기화안함01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 보스한테보내는포탈생성_시간초기화안함02()


class 보스한테보내는포탈생성_시간초기화안함02(state.State):
    def on_enter(self):
        set_portal(portalId=6201, visible=True, enabled=True, minimapVisible=True) # 5스테이지 가운데 전투판에 보스 메인 전투판으로 보내는 순간이동 포탈 생성시키기, 이 포탈 PortalStage06Boss.xml 에서도 사용함
        set_portal(portalId=1220, visible=False, enabled=False, minimapVisible=False) # 포탈ID 1220 , 큐브 파괴되어 추락된 플레이어 이전 전투판으로 보내는 순간이동 포탈 다시 감추기
        set_user_value(key='SkillBreakStart', value=0) # SkillBreakStart 변수 0으로 초기화

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return None # Missing State: 스킬브레이크신호대기_시간셋팅안함


