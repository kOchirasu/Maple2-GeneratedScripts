""" trigger/02000421_bf/eventnpcappearance.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.true():
            return 보스등장대기(self.ctx)


class 보스등장대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.create_monster(spawnIds=[121], animationEffect=True)
        self.create_monster(spawnIds=[131], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='EventNpcAppearance', value=1):
            return 우호적NPC등장(self.ctx)


class 우호적NPC등장(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111], arg2=True)
        self.destroy_monster(spawnIds=[121], arg2=True)
        self.destroy_monster(spawnIds=[131], arg2=True) # 함교 안에 있었던  우호적 NPC 3인방이 전투판으로 나와 전투를 진행한다는 설정에 맞추어 전투판에 우호적 NPC 3인방을 등장시킴
        self.create_monster(spawnIds=[11], animationEffect=True)
        self.create_monster(spawnIds=[21], animationEffect=True)
        self.create_monster(spawnIds=[31], animationEffect=True) # 참고로 이 우호적 NPC 3인방 제거는 보스 몬스터가 죽을 때 AI 에서 신호 보내서 제거하는 방식을 사용함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 대기(self.ctx)


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='EventNpcAppearance', value=2):
            return 시작대기중(self.ctx)


initial_state = 시작대기중
