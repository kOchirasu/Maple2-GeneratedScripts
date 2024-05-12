""" trigger/52010052_qd/act01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000074], questStates=[2]):
            # 하늘의 안전 확보, 그러나...  완료 가능
            return NPC리젠03_담당관과트리스탄_02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[2]):
            # 전 대원 소집령 퀘스트 완료 가능
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000037], questStates=[2]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000075], questStates=[3]):
            # 미래의 평화를 위해 퀘스트 완료
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000074], questStates=[3]):
            # 하늘의 안전 확보, 그러나... 퀘스트 완료
            return NPC리젠03_담당관과트리스탄_02(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000063], questStates=[3]):
            # 그를 만나는 곳, 100m 전 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000058], questStates=[3]):
            # 달라진 트리스탄 퀘스트 완료
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000057], questStates=[3]):
            # 준비만이 살길이다 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000050], questStates=[3]):
            # 전 대원 소집령 퀘스트 완료
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000043], questStates=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠03_트리스탄솔로(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000049], questStates=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠02_담당관과트리스탄(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000046], questStates=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return NPC리젠01_5대세력담당관(self.ctx)
        if self.quest_user_detected(boxIds=[9001], questIds=[91000019], questStates=[3]):
            # 함대 최우선 임무 퀘스트 완료
            return 종료(self.ctx)


class NPC리젠03_트리스탄솔로(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2005], animationEffect=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class NPC리젠01_5대세력담당관(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2000], animationEffect=False) # 블리체
        self.create_monster(spawnIds=[2001], animationEffect=False) # 콘대르
        self.create_monster(spawnIds=[2002], animationEffect=False) # 메이슨
        self.create_monster(spawnIds=[2003], animationEffect=False) # 샤텐
        self.create_monster(spawnIds=[2004], animationEffect=False) # 네이린

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class NPC리젠02_담당관과트리스탄(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2000], animationEffect=False) # 블리체
        self.create_monster(spawnIds=[2001], animationEffect=False) # 콘대르
        self.create_monster(spawnIds=[2002], animationEffect=False) # 메이슨
        self.create_monster(spawnIds=[2003], animationEffect=False) # 샤텐
        self.create_monster(spawnIds=[2004], animationEffect=False) # 네이린
        self.create_monster(spawnIds=[2005], animationEffect=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9001], questIds=[91000057], questStates=[3]):
            # 준비만이 살길이다 완료
            return 트리스탄삐짐01(self.ctx)


class 트리스탄삐짐01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003790, illustId='Tristan_normal', msg='$52010052_QD__ACT01__0$', duration=4000) # 11003790: 트리스탄
        self.move_npc(spawnId=2005, patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 트리스탄삐짐02(self.ctx)


class 트리스탄삐짐02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class NPC리젠03_담당관과트리스탄_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2000], animationEffect=False) # 블리체
        self.create_monster(spawnIds=[2001], animationEffect=False) # 콘대르
        self.create_monster(spawnIds=[2002], animationEffect=False) # 메이슨
        self.create_monster(spawnIds=[2003], animationEffect=False) # 샤텐
        self.create_monster(spawnIds=[2004], animationEffect=False) # 네이린
        self.create_monster(spawnIds=[2005], animationEffect=False) # 트리스탄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = Wait
