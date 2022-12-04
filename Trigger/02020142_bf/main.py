""" trigger/02020142_bf/main.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[45,21,28]) # arg1 = AmbientColor RGB값
        self.set_directional_light(diffuseColor=[16,30,29], specularColor=[130,130,130]) # arg1 = DiffuseColor RGB값,  arg2 = SpecularColor RGB값
        self.set_mesh(triggerIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924], visible=False, arg3=0, delay=0, scale=0) # 몬스터만 밟을 수 있는 투명벽 셋팅하기
        self.set_effect(triggerIds=[301], visible=True) # 1페이즈 전투판의 빛기둥 생성
        self.set_user_value(key='1PhaseSpawnStart', value=0) # 이 변수가 1이 되면, 1페이즈용 보스가 등장하면서 1페이즈 전투 시작을 알림
        self.set_user_value(key='2PhaseSpawnStart', value=0) # 이 변수가 1이 되면, 2페이즈용 보스가 등장하면서 2페이즈 전투 시작을 알림
        self.set_portal(portalId=108, visible=False, enable=False, minimapVisible=False) # 최초 시작 지점에서 1페이즈 전투판으로 가는 포탈 최초에 감추기, 108: 스타팅 지점에서 1페이지 전투판 근처로 도착
        self.set_portal(portalId=118, visible=False, enable=False, minimapVisible=False) # 첫번째 왼쪽 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=128, visible=False, enable=False, minimapVisible=False) # 첫번째 가운데 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=138, visible=False, enable=False, minimapVisible=False) # 첫번째 오른쪽 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=218, visible=False, enable=False, minimapVisible=False) # 두번째 왼쪽 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=228, visible=False, enable=False, minimapVisible=False) # 두번째 가운데 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=238, visible=False, enable=False, minimapVisible=False) # 두번째 오른쪽 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=328, visible=False, enable=False, minimapVisible=False) # 세번번째 가운데 졸구간 포탈 최초에 감추기
        self.set_portal(portalId=318, visible=False, enable=False, minimapVisible=False) # 졸구간 끝내고 2페이지 전투판으로 가는 왼쪽 포탈 최초에 감추기
        self.set_portal(portalId=428, visible=False, enable=False, minimapVisible=False) # 졸구간 끝내고 2페이지 전투판으로 가는 가운데 포탈 최초에 감추기
        self.set_portal(portalId=338, visible=False, enable=False, minimapVisible=False) # 졸구간 끝내고 2페이지 전투판으로 가는 오른쪽 포탈 최초에 감추기
        self.set_portal(portalId=599, visible=False, enable=False, minimapVisible=False) # 세번째페이즈 진행하는 맵 이동 포탈 처음에 감추기, 2페이즈 전투판에 설치한 포탈
        self.set_portal(portalId=598, visible=False, enable=False, minimapVisible=False) # 세번째페이즈 진행하는 맵 이동 포탈 처음에 감추기, 최초 시작 지점에 설치한 포탈
        self.set_mesh(triggerIds=[949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999], visible=True, arg3=1, delay=1, scale=1) # 플레이어만 막고 몬스터는 막지 않는 투명벽 설정
        self.set_user_value(key='TriggerMesh11', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh21', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh12', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh22', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh32', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh13', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TriggerMesh23', value=99) # 이 변수 99 하기, 이거 안하면   condition 에서  value="0" 체크되어 트리거 로직 꼬일 수 있음
        self.set_user_value(key='TurkaTwoPhaseEnd', value=99) # 이 변수 99 하기, 이거 안하면   나중에 condition 에서  value="1" 체크함

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[99], questIds=[10003330], questStates=[2]):
            return 이동(self.ctx)
        if self.quest_user_detected(boxIds=[99], questIds=[10003330], questStates=[3]):
            return 이동(self.ctx)
        if self.user_detected(boxIds=[99]):
            return 연출용보스등장(self.ctx)


class 연출용보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[100], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카대사연출(self.ctx)


class 투르카대사연출(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=23000120, illust='Turka_normal', duration=9000, script='$02020140_BF__PopUpCinema__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 페이즈보스등장대기1(self.ctx)


class 페이즈보스등장대기1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='1PhaseSpawnStart', value=1):
            return 페이즈보스등장1(self.ctx)


class 페이즈보스등장1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False) # 1페이즈용 투르카 보스 등장시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 페이즈전투진행1(self.ctx)


class 페이즈전투진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=108, visible=True, enable=True, minimapVisible=True) # 최초 시작 지점에서 1페이즈 전투판으로 가는 포탈 등장시키기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='2PhaseSpawnStart', value=1):
            return 페이즈전투완료_2페이즈투르카등장1(self.ctx)


class 페이즈전투완료_2페이즈투르카등장1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False) # 2페이즈용 투르카 보스 등장시키기
        self.remove_buff(boxId=98, skillId=50004418) # 플레이어에게 걸려있는 타겟팅 저주 디버프 제거하기, arg1="98"는 1페이즈 전투판을 커버하고 있는 트리거영역 ID임

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 졸구간시작연출딜레이(self.ctx)


class 졸구간시작연출딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[301], visible=False) # 1페이즈 전투판 빛기둥 제거
        self.set_ambient_light(primary=[255,140,172]) # arg1 = AmbientColor RGB값
        self.set_directional_light(diffuseColor=[146,221,218], specularColor=[130,130,130]) # arg1 = DiffuseColor RGB값,  arg2 = SpecularColor RGB값
        self.change_background(dds='BG_Turka_A.dds') # 2페이즈 부터 맵이 밝아지면서, 백그라운드 이미지 교체함

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StageOpen', value=1):
            return 최초졸구간몬스터등장(self.ctx)


class 최초졸구간몬스터등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh11', value=0) # 첫번째 왼쪽 졸구간 졸몹 마리수 체크하기 위한 변수 0  셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.set_user_value(key='TriggerMesh12', value=0) # 첫번째 가운데 졸구간 졸몹 마리수 체크하기 위한 변수 0  셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.set_user_value(key='TriggerMesh13', value=0) # 첫번째 오른쪽 졸구간 졸몹 마리수 체크하기 위한 변수 0  셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.create_monster(spawnIds=[1201,1202,1203,1204], animationEffect=False) # 중요: 이 졸몹은 등장하자마자 AI에서 트리거 쪽으로 TriggerMesh?? 변수 +1 신호를 보내야 하기 때문에 꼭 등장하자마자 바로 전투 상태가 되어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 졸구간본격진행(self.ctx)


class 졸구간본격진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=128, visible=True, enable=True, minimapVisible=True) # 첫번째 가운데 졸구간 진입 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 졸구간진행체크중(self.ctx)


class 졸구간진행체크중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TriggerMesh12', value=0):
            return 두번째가운데진행01(self.ctx)
        if self.user_value(key='TriggerMesh22', value=0):
            return 세번째가운데진행01(self.ctx)
        if self.user_value(key='TriggerMesh32', value=0):
            return 가운데지점보스방가는포탈생성(self.ctx)
        if self.user_value(key='2PhaseStartOk', value=1):
            return 모든졸구간지형과포탈생성(self.ctx)
        if self.user_value(key='TurkaTwoPhaseEnd', value=1): # ## 퀘스트용 투르카 던전은 가운데 지형만 지형하고 왼쪽 오른쪽 지형은 진행 필요 없어 주석처리함 ##
            return 이맵에서진행끝내고다음맵으로이동(self.ctx)


class 두번째왼쪽진행01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh11', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_user_value(key='TriggerMesh21', value=0) # 두번째 왼쪽 졸구간 졸몹 마리수 체크하기 위한 변수 0 초기화 셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.create_monster(spawnIds=[2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118], animationEffect=False) # 중요: 이 졸몹은 등장하자마자 AI에서 트리거 쪽으로 TriggerMesh?? 변수 +1 신호를 보내야 하기 때문에 꼭 등장하자마자 바로 전투 상태가 되어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3199):
            return 두번째왼쪽진행02(self.ctx)


class 두번째왼쪽진행02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=218, visible=True, enable=True, minimapVisible=True) # 두번째 왼쪽 졸구간 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=799):
            return 졸구간진행체크중(self.ctx)


class 두번째가운데진행01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh12', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_user_value(key='TriggerMesh22', value=0) # 두번째 가운데 졸구간 졸몹 마리수 체크하기 위한 변수 0 초기화 셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.create_monster(spawnIds=[2201,2202,2203,2204], animationEffect=False) # 중요: 이 졸몹은 등장하자마자 AI에서 트리거 쪽으로 TriggerMesh?? 변수 +1 신호를 보내야 하기 때문에 꼭 등장하자마자 바로 전투 상태가 되어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3199):
            return 두번째가운데진행02(self.ctx)


class 두번째가운데진행02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=228, visible=True, enable=True, minimapVisible=True) # 두번째 가운데 졸구간 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=799):
            return 졸구간진행체크중(self.ctx)


class 세번째가운데진행01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh22', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_user_value(key='TriggerMesh32', value=0) # 세번째 가운데 졸구간 졸몹 마리수 체크하기 위한 변수 0 초기화 셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.create_monster(spawnIds=[3201,3202,3203,3204], animationEffect=False) # 중요: 이 졸몹은 등장하자마자 AI에서 트리거 쪽으로 TriggerMesh?? 변수 +1 신호를 보내야 하기 때문에 꼭 등장하자마자 바로 전투 상태가 되어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3199):
            return 세번째가운데진행02(self.ctx)


class 세번째가운데진행02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=328, visible=True, enable=True, minimapVisible=True) # 세번째 왼쪽 졸구간 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=799):
            return 졸구간진행체크중(self.ctx)


class 두번째오른쪽진행01(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh13', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_user_value(key='TriggerMesh23', value=0) # 두번째 오른쪽 졸구간 졸몹 마리수 체크하기 위한 변수 0 초기화 셋팅하여 마리수 체크 시작하기, 이후 졸몹 등장하면 졸몹 AI에게 이 변수 +1씩 하여 마리수 체크하며, 죽으면 -1씩 하며, 결국 0이 되면 트리거 다음 단계로 넘어가도록 함
        self.create_monster(spawnIds=[2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315,2316,2317,2318], animationEffect=False) # 중요: 이 졸몹은 등장하자마자 AI에서 트리거 쪽으로 TriggerMesh?? 변수 +1 신호를 보내야 하기 때문에 꼭 등장하자마자 바로 전투 상태가 되어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3199):
            return 두번째오른쪽진행02(self.ctx)


class 두번째오른쪽진행02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=238, visible=True, enable=True, minimapVisible=True) # 두번째 오른쪽 졸구간 포탈 생성

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=799):
            return 졸구간진행체크중(self.ctx)


# 아래 3개는 졸구간 다 끝내고 2페이즈 보스 전투판으로 가는 포탈 생성하는 부분
class 왼쪽지점보스방가는포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh21', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_portal(portalId=318, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 왼쪽 졸구간 포탈 생성
        self.set_ai_extra_data(key='TwoPhaseMainBattle', value=1) # AI_TurkaHoodForce_Phase02.xml 에 있는 TwoPhaseMainBattle 변수에 1 설정해서 보스가 본격 2페이지 전투 시작하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 페이즈복격진행_안내메시지출력2(self.ctx)


class 가운데지점보스방가는포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh32', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_portal(portalId=428, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 가운데 졸구간 포탈 생성
        self.set_ai_extra_data(key='TwoPhaseMainBattle', value=1) # AI_TurkaHoodForce_Phase02.xml 에 있는 TwoPhaseMainBattle 변수에 1 설정해서 보스가 본격 2페이지 전투 시작하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 페이즈복격진행_안내메시지출력2(self.ctx)


class 오른쪽지점보스방가는포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='TriggerMesh23', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_portal(portalId=338, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 오른쪽 졸구간 포탈 생성
        self.set_ai_extra_data(key='TwoPhaseMainBattle', value=1) # AI_TurkaHoodForce_Phase02.xml 에 있는 TwoPhaseMainBattle 변수에 1 설정해서 보스가 본격 2페이지 전투 시작하도록 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 페이즈복격진행_안내메시지출력2(self.ctx)


class 페이즈복격진행_안내메시지출력2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6500):
            return 졸구간진행체크중(self.ctx)


class 모든졸구간지형과포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(key='2PhaseStartOk', value=-1) # 이 변수 -1 하여 무한루프에 빠지지 않게 함
        self.set_portal(portalId=118, visible=True, enable=True, minimapVisible=True) # 첫번째 왼쪽 졸구간 진입 포탈 생성
        self.set_portal(portalId=128, visible=True, enable=True, minimapVisible=True) # 첫번째 가운데 졸구간 진입 포탈 생성
        self.set_portal(portalId=138, visible=True, enable=True, minimapVisible=True) # 첫번째 오른쪽 졸구간 진입 포탈 생성
        self.set_portal(portalId=218, visible=True, enable=True, minimapVisible=True) # 두번째 왼쪽 졸구간 포탈 생성
        self.set_portal(portalId=228, visible=True, enable=True, minimapVisible=True) # 두번째 가운데 졸구간 포탈 생성
        self.set_portal(portalId=328, visible=True, enable=True, minimapVisible=True) # 세번째 왼쪽 졸구간 포탈 생성
        self.set_portal(portalId=238, visible=True, enable=True, minimapVisible=True) # 두번째 오른쪽 졸구간 포탈 생성
        self.set_portal(portalId=318, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 왼쪽 졸구간 포탈 생성
        self.set_portal(portalId=428, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 가운데 졸구간 포탈 생성
        self.set_portal(portalId=338, visible=True, enable=True, minimapVisible=True) # 보스 전투판으로 가는 오른쪽 졸구간 포탈 생성
        self.destroy_monster(spawnIds=[1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,2101,2102,2103,2104,2105,2106,2107,2108,2109,2110,2111,2112,2113,2114,2115,2116,2117,2118])
        self.destroy_monster(spawnIds=[1201,1202,1203,1204,2201,2202,2203,2204,3201,3202,3203,3204])
        self.destroy_monster(spawnIds=[1301,1302,1303,1304,1305,1306,1307,1308,1309,1310,1311,1312,1313,2301,2302,2303,2304,2305,2306,2307,2308,2309,2310,2311,2312,2313,2314,2315,2316,2317,2318])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 졸구간진행체크중(self.ctx)


class 이맵에서진행끝내고다음맵으로이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=599, visible=True, enable=True, minimapVisible=True) # 세번째페이즈 진행하는 다음 맵으로 이동시키기, 2페이지 전투판에 위치한 포탈
        self.set_portal(portalId=598, visible=True, enable=True, minimapVisible=True) # 세번째페이즈 진행하는 다음 맵으로 이동시키기, 최초 시작 지점에 위치한 포탈
        self.set_portal(portalId=108, visible=False, enable=False, minimapVisible=False) # 세번째페이즈 넘어가야 하는 상황이 되면, 최초 시작 지점에서 1페이즈 전투판으로 가는 포탈 다시 감추기, 108: 스타팅 지점에서 1페이지 전투판 근처로 도착

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 종료안내메시지_대기(self.ctx)


class 종료안내메시지_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[97]):
            return 종료안내메시지(self.ctx)


class 종료안내메시지(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[92], enable=True) # 보스가 맵 파괴 스킬 사용하기는 하나, 혹시 몰라서 맵 스킬쪽에서도 한번 더 파괴 행동을 함  CubeBreak ,  MS2TriggerSkill = 92 스킬코드 70000105(레벨2) 발동시켜 바닥 파괴하여, 맵 02020142 으로 갈수 있도록 하기
        self.destroy_monster(spawnIds=[-1]) # 안내 메시지 호출하기, 메시지 글씨 작성 엑셀파일은 여기 stringGuide.xlsx
        self.show_guide_summary(entityId=29200004, textId=29200004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15500):
            return 종료_메시지대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=29200004)


class 종료_메시지대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료안내메시지_다시출력_대기(self.ctx)


class 종료안내메시지_다시출력_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[97]):
            return 종료안내메시지_다시출력(self.ctx)


class 종료안내메시지_다시출력(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=29200004, textId=29200004)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15500):
            return 종료_메시지대기(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=29200004)


class 이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100304, portalId=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
