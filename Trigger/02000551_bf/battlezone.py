""" trigger/02000551_bf/battlezone.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 트리거작동시작(self.ctx)


class 트리거작동시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=13, spawnIds=[101]):
            return 중앙전투판신호(self.ctx)
        if self.npc_detected(boxId=12, spawnIds=[101]):
            return 시전투판신호12(self.ctx)
        if self.npc_detected(boxId=3, spawnIds=[101]):
            return 시전투판신호3(self.ctx)
        if self.npc_detected(boxId=6, spawnIds=[101]):
            return 시전투판신호6(self.ctx)
        if self.npc_detected(boxId=9, spawnIds=[101]):
            return 시전투판신호9(self.ctx)
        if self.npc_detected(boxId=122, spawnIds=[101]):
            return 봄컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=45, spawnIds=[101]):
            return 여름컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=78, spawnIds=[101]):
            return 가을컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=1011, spawnIds=[101]): # arg2은 몬스터 스폰ID 102는 쉬운 난이도
            return 겨울컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=13, spawnIds=[102]):
            return 중앙전투판신호(self.ctx)
        if self.npc_detected(boxId=12, spawnIds=[102]):
            return 시전투판신호12(self.ctx)
        if self.npc_detected(boxId=3, spawnIds=[102]):
            return 시전투판신호3(self.ctx)
        if self.npc_detected(boxId=6, spawnIds=[102]):
            return 시전투판신호6(self.ctx)
        if self.npc_detected(boxId=9, spawnIds=[102]):
            return 시전투판신호9(self.ctx)
        if self.npc_detected(boxId=122, spawnIds=[102]):
            return 봄컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=45, spawnIds=[102]):
            return 여름컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=78, spawnIds=[102]):
            return 가을컨셉도로신호(self.ctx)
        if self.npc_detected(boxId=1011, spawnIds=[102]):
            return 겨울컨셉도로신호(self.ctx)
        if self.wait_tick(waitTick=2200):
            return 시간경과대기(self.ctx)


class 시간경과대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 트리거작동시작(self.ctx)


class 중앙전투판신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=13) # 보스AI에게 이 변수 13 신호를 보내서 보스가 중앙 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 시전투판신호12(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=12) # 보스AI에게 이 변수 12 신호를 보내서 보스가 12시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 시전투판신호3(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=3) # 보스AI에게 이 변수 3 신호를 보내서 보스가 3시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 시전투판신호6(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=6) # 보스AI에게 이 변수 6 신호를 보내서 보스가 6시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 시전투판신호9(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=9) # 보스AI에게 이 변수 9 신호를 보내서 보스가 9시쪽 전투판에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 봄컨셉도로신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=122) # 보스AI에게 이 변수 122 신호를 보내서 보스가 봄 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 여름컨셉도로신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=45) # 보스AI에게 이 변수 45 신호를 보내서 보스가 여름 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 가을컨셉도로신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=78) # 보스AI에게 이 변수 78 신호를 보내서 보스가 가을 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 겨울컨셉도로신호(trigger_api.Trigger):
    def on_enter(self):
        self.set_ai_extra_data(key='BattleZonePosition', value=1011) # 보스AI에게 이 변수 1011 신호를 보내서 보스가 겨울 컨셉 도로 중앙에 들어셨음을 알림,  즉 AI_CarParadeBlackbean.xml 혹은 AI_CarParadeBlackbeanBroken.xml 혹은 AI_Blackbean_Phase01.xml 에게 보냄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리거작동시작(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
