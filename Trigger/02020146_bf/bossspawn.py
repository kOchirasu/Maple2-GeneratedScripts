""" trigger/02020146_bf/bossspawn.xml """
import trigger_api


class 시작대기중(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 맵 나가기 포탈, 시작 지점에
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False) # 맵 나가기 포탈, 전투판 지점에
        self.set_portal(portalId=601, visible=False, enable=False, minimapVisible=False) # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 보스등장이벤트대기(self.ctx)


class 보스등장이벤트대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # 이슈라 등장

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출대기(self.ctx)


class 연출대기(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__0$', duration=4000, voice='ko/Npc/00002192')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 전투진행(self.ctx)


class 전투진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=601, visible=True, enable=True, minimapVisible=True) # 맵 나가기 포탈, 전투판으로 가기 위한 맵 내부 포탈

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 종료딜레이(self.ctx)


class 종료딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(achieve='IshuraDungeonClear_Quest') # arg1 = "특정트리거 박스 안에 있는 유저만 체크하고자 할때"   arg2 = "trigger"    즉 trigger 이거만 쓸수 있음  특정 트리거 박스 안의 유저만 체크 방식을 사용하고자 할때 이 2개 넣어야 함

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 마무리연출(self.ctx)


class 마무리연출(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=23000113, illust='Ishura_Dark_Idle', script='$02020120_BF__BOSSSPAWN__2$', duration=6576, voice='ko/Npc/00002194')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 시작대기중
