""" trigger/02020120_bf/daynightchangedebuff.xml """
import trigger_api


class Ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[2222], enable=True) # 맵 스킬 초기화 셋팅, 태양빛의 저주 디버프 스킬 On으로 초기 셋팅하기, 이 맵은 낮으로 시작하기 때문에
        self.set_skill(triggerIds=[1212], enable=False) # 맵 스킬 초기화 셋팅, 달빛의 저주 디버프 스킬 Off으로 초기 셋팅하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=199, boxId=1):
            return 낮밤변환신호대기(self.ctx)


class 낮밤변환신호대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DayNightChange', value=1):
            return 낮시간으로변화대기단계(self.ctx)
        if self.user_value(key='DayNightChange', value=2):
            return 밤시간으로변화대기단계(self.ctx)
        if self.user_value(key='DayNightChange', value=3): # 스킬 브레이크 막기 실패하면 이슈라AI에서  DungeonReset = 1 신호를 보내서 던전 초기화 시킴
            return 디버프모조리제거(self.ctx)
        if self.user_value(key='DungeonReset', value=1):
            return 낮시간으로변화하기_맵초기화(self.ctx)


class 낮시간으로변화대기단계(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1400):
            return 낮시간으로변화하기(self.ctx)


class 낮시간으로변화하기(trigger_api.Trigger):
    def on_enter(self):
        self.change_background(dds='BG_RedLapenta_A.dds')
        self.set_ambient_light(primary=[226,197,211]) # arg1 = ambient color RGB값
        self.set_directional_light(diffuseColor=[224,246,249], specularColor=[170,170,170]) # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_skill(triggerIds=[2222], enable=True) # 태양빛의 저주 디버프 스킬 On
        self.set_skill(triggerIds=[1212], enable=False) # 달빛의 저주 디버프 스킬 Off
        self.set_user_value(key='DayNightChange', value=0) # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 낮밤변환신호대기(self.ctx)


class 낮시간으로변화하기_맵초기화(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[299], skillId=50004547, level=2, isPlayer=False) # 레벨2: 시야 효과 8초 이상, 낮으로 변하면서 필터 이펙트 시야효과 애디녀설 부여하기, MS2TriggerBox   TriggerObjectID = 299,   299는 모든 전투판 범위임,  arg3 는 애디셔널 레벨임
        self.set_user_value(key='DungeonReset', value=0) # 스킬브레이크 실패하여 보스의 신호를 받아서 던전 리셋할때 사용하는 변수
        self.set_user_value(key='DayNightChange', value=0) # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기
        self.change_background(dds='BG_RedLapenta_A.dds')
        self.set_ambient_light(primary=[226,197,211]) # arg1 = ambient color RGB값
        self.set_directional_light(diffuseColor=[224,246,249], specularColor=[170,170,170]) # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_skill(triggerIds=[2222], enable=True) # 태양빛의 저주 디버프 스킬 On
        self.set_skill(triggerIds=[1212], enable=False) # 달빛의 저주 디버프 스킬 Off

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 낮밤변환신호대기(self.ctx)


class 밤시간으로변화대기단계(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1400):
            return 밤시간으로변화하기(self.ctx)


class 밤시간으로변화하기(trigger_api.Trigger):
    def on_enter(self):
        self.change_background(dds='BG_RedLapenta_B.dds') # 이슈라 보스 낮밤 변화 마법 동작에 맞추어 타이밍 맞게 트리거 신호 변화를 하기 위해, 여기  waitTick 시간 조절을 넣음
        self.set_ambient_light(primary=[120,119,183]) # arg1 = ambient color RGB값
        self.set_directional_light(diffuseColor=[193,100,119], specularColor=[170,170,170]) # arg1 = diffuse color RGB값,  arg2 = specular color RGB값
        self.set_skill(triggerIds=[2222], enable=False) # 태양빛의 저주 디버프 스킬 Off
        self.set_skill(triggerIds=[1212], enable=True) # 달빛의 저주 디버프 스킬 On
        self.set_user_value(key='DayNightChange', value=0) # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 낮밤변환신호대기(self.ctx)


class 디버프모조리제거(trigger_api.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[299], skillId=50005315, level=1, isPlayer=False) # 태양빛 달빛 각종 저주 디버프 전부 제거하기, MS2TriggerBox   TriggerObjectID = 299,   299는 모든 전투판 범위임,  arg3 는 애디셔널 레벨임
        self.set_user_value(key='DayNightChange', value=0) # DayNightChange 변수 0으로 초기하 하여 위쪽 단계 "낮밤변환신호대기" 에서 대기 상태가 되도록 하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1100):
            return 낮밤변환신호대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Ready
