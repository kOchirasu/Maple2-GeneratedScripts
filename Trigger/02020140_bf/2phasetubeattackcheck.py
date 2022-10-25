""" trigger/02020140_bf/2phasetubeattackcheck.xml """
import common


class 시작대기중(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='2PhaseTubeStep', value=0) # 변수 최초 초기화: 이 변수가 1이 되면 튜브 대미지 필드 1단계 진행,  이 변수가 2이 되면 튜브 대미지 필드 2단계 진행
        self.set_user_value(key='MarbleTurkaSupportMany', value=0) # 변수 최초 초기화: 마법 구슬 오브젝트가 등장하면, 이 오브젝트  AI_MarbleTurkaSupport.xml  AI로 부터 이 변수 +1 신호를 받고, 파괴되어 죽으면  AI_MarbleTurkaSupport.xml AI로 부터 이 변수 -1 신호를 받게 됨

    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 트리거작동신호받기대기중(self.ctx)


class 트리거작동신호받기대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2PhaseTubeStep', value=1, operator='GreaterEqual'):
            return 트리거작동대기중(self.ctx)


class 트리거작동대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 트리거작동시작(self.ctx)


class 트리거작동시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2PhaseTubeStep', value=1):
            return 튜브대미지필드_1단계진행(self.ctx)
        if self.user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)


class 튜브대미지필드_1단계진행(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_생성1(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거1(self.ctx)


class 단계_튜브대미지필드_생성1(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[102], skillId=50004566, level=1, isPlayer=True, isSkillSet=True) # 1단계 튜브대미지필드 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)
        if self.user_value(key='MarbleTurkaSupportMany', value=0):
            return 단계_튜브대미지필드_제거1(self.ctx)


class 단계_튜브대미지필드_제거1(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004566) # 1단계 튜브대미지필드 제거

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='2PhaseTubeStep', value=2):
            return 튜브대미지필드_2단계전환_우선1단계제거(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 튜브대미지필드_1단계진행(self.ctx)


class 튜브대미지필드_2단계전환_우선1단계제거(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004566) # 우선 1단계 튜브대미지필드  제거
        self.set_user_value(key='TubeLeveStep', value=0) # 이 변수 최초 초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 단계_튜브대미지필드_처음단계2(self.ctx)


class 단계_튜브대미지필드_처음단계2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_1Lv생성2(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거2(self.ctx)


class 단계_튜브대미지필드_1Lv생성2(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[102], skillId=50004563, level=1, isPlayer=True, isSkillSet=True) # 튜브대미지필드 1Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_2Lv생성2(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004563) # 2단계 튜브대미지필드 1Lv  제거
        self.add_buff(boxIds=[102], skillId=50004564, level=1, isPlayer=True, isSkillSet=True) # 튜브대미지필드 2Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_3Lv생성2(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004564) # 2단계 튜브대미지필드 2Lv 제거
        self.add_buff(boxIds=[102], skillId=50004565, level=1, isPlayer=True, isSkillSet=True) # 튜브대미지필드 3Lv 발동 , arg1 은 등장 몬스터의 스폰ID, arg2은 애디셔널 코드,  arg3은 애디셔널 레벨,   arg4 = 1 이면 플레이어가 아닌 NPC에게 적용,    arg5 = 1 하면 트리거 박스 영역 외의 모든 지점 체크

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)


class 단계_튜브대미지필드_TubeLeveStep_더하기2(common.Trigger):
    def on_enter(self):
        self.add_user_value(key='TubeLeveStep', value=1) # 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_체크2(self.ctx)
        if self.user_value(key='TubeLeveStep', value=30):
            return 버프부여구슬제거경고메시지(self.ctx)


class 단계_튜브대미지필드_TubeLeveStep_체크2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='TubeLeveStep', value=10):
            return 단계_튜브대미지필드_2Lv생성2(self.ctx)
        if self.user_value(key='TubeLeveStep', value=20):
            return 단계_튜브대미지필드_3Lv생성2(self.ctx)
        if self.user_value(key='MarbleTurkaSupportMany', value=1, operator='GreaterEqual'):
            return 단계_튜브대미지필드_TubeLeveStep_더하기2(self.ctx)
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_제거2(self.ctx)


class 버프부여구슬제거경고메시지(common.Trigger):
    def on_enter(self):
        self.add_user_value(key='TubeLeveStep', value=-9) # 이 변수 -9를 빼서 21로 만들기, 절대 20 이하로 만들면 안됨!! 대박 버그임
        self.add_buff(boxIds=[102], skillId=50000348, level=2, isPlayer=True, isSkillSet=True) # 벙업 버프 (5중첩) 걸기(50000348 2Lv), 홀로그램 소녀 소환몹 몬스터가 보스한테 부여하는 버프랑 동일한 것임
        self.show_guide_summary(entityId=29200005, textId=29200005, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_TubeLeveStep_체크2(self.ctx)


class 단계_튜브대미지필드_제거2(common.Trigger):
    def on_enter(self):
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004563) # 2단계 튜브대미지필드 1Lv  제거
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004564) # 2단계 튜브대미지필드 2Lv 제거
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50004565) # 2단계 튜브대미지필드 3Lv 제거
        self.npc_remove_additional_effect(spawnId=102, additionalEffectId=50000348)
        self.set_user_value(key='TubeLeveStep', value=0) # 다시 처음부터 시작하니 이 변수  초기화: 보스가 마법 구슬 오브제트로 인한 애디셔널에 계속 걸려 있으면, 이 변수 1씩 더하는데, 이 변수가 10씩 쌓일 수록 튜브대미지필드 1단계씩 상승시킴
        self.hide_guide_summary(entityId=29200005) # 혹시 마력의 구슬 제거하라는 경고 메시지 떠있는 상태일 경우를 대비해 메시지 제거 명령어 여기에 설정함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 단계_튜브대미지필드_처음단계2(self.ctx)


# 이 트리거에서는  <state name="종료"> 로 올일 없음
class 종료(common.Trigger):
    pass


initial_state = 시작대기중
