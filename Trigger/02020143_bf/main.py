""" trigger/02020143_bf/main.xml """
import common


class 시작대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.check_user():
            return 기본셋팅(self.ctx)


class 기본셋팅(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False) # 나가기 포탈 최초에는 감추기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[2]):
            return 이동(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[3]):
            return 이동(self.ctx)
        if self.user_detected(boxIds=[102]):
            return 보스등장준비(self.ctx)


class 보스등장준비(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)
        self.add_buff(boxIds=[102], skillId=50000554, level=1, isPlayer=False, isSkillSet=False) # MS2TriggerBox   TriggerObjectID = 102, 이 트리거 박스 안의 플레이어에게 애디셔널 50000554(레벨1) 회복 버프 부여하기, 이 맵은 추락하면서 시작하는데 추락 대미지에 의해 죽을 수있기 때문에 시작하자마자 무조건 HP회복 버프 부여함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스등장(self.ctx)


class 보스등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[99], animationEffect=False) # EventSpawnPointNPC 의 SpawnPointID가 99 번, 즉   arg1="99"

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1100):
            return 클리어성공유무체크시작(self.ctx)


class 클리어성공유무체크시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 연출딜레이(self.ctx)
        if self.dungeon_time_out():
            return 던전실패(self.ctx)
        if self.dungeon_check_state(checkState='Fail'):
            return 던전실패(self.ctx)


class 던전실패(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True) # 나가기 포탈 생성하기, 졸구간 전투판에서 나가기 포탈

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            self.dungeon_fail()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.dungeon_enable_give_up(isEnable='0')


class 연출딜레이(common.Trigger):
    def on_enter(self):
        self.set_achievement(achieve='TurkaQuestDungeonClear') # arg3="TurkaQuestDungeonClear" 는 퀘스트와 트로피 업적 당설 완료 조건 처리 키값임, arg1="??" arg2="trigger" 은 해당 트리거 안에 만 있으면 클리어 처리 할때 사용하는 것인데, 이거 생략하면 맵 안에만 있으면 무조건 퀘스트와 트로피 업적을 완료 처리함

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.dungeon_set_end_time() # 시간 기능 종료시킴, 이 기능 잘 작동시키려면 DungeonRoom.xlsx 의 제한 시간 만료 시(isExpireTimeOut) 빈칸 설정 해야 함
        self.dungeon_close_timer()
        self.dungeon_clear()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 영상재생준비(self.ctx)


class 영상재생준비(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 영상재생(self.ctx)


class 영상재생(common.Trigger):
    def on_enter(self):
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(fileName='common\Kritias_03.usm', movieId=1)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return Quit(self.ctx)
        if self.wait_tick(waitTick=129000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003330], questStates=[2]):
            return 이동(self.ctx)


class 이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52100304, portalId=1)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 시작대기중(self.ctx)


initial_state = 시작대기중
