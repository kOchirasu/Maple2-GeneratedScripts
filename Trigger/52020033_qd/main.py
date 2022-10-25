""" trigger/52020033_qd/main.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[3]):
            return 가버려_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[2]):
            return 가버려_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 부유도_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[3]):
            return 기본_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[2]):
            return 소개_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[1]):
            return 소개_대기(self.ctx)


class 기본(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 기본_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 부유도_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 조건확인_대기01(self.ctx)


class 조건확인_대기01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 부유도_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[3]):
            return 조건확인_대기02(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[2]):
            return 조건확인_대기02(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 조건확인_대기02(self.ctx)


class 조건확인_대기02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 부유도_대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[3]):
            return 조건확인_대기01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001750], questStates=[2]):
            return 조건확인_대기01(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[1]):
            return 조건확인_대기01(self.ctx)


class 가버려_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[3]):
            return 부유도로가버려(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[2]):
            return 부유도로가버려(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001751], questStates=[3]):
            return 퀘스트조건체크(self.ctx)


class 부유도로가버려(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020001, portalId=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부유도로가버려(self.ctx)


class 소개_대기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52020033, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 소개_준비(self.ctx)


class 소개_준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 소개_세로줌인01(self.ctx)


class 소개_세로줌인01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000,8001], returnView=False)
        self.show_caption(type='NameCaption', title='$map:52020033$', desc='크리티아스 정찰 임무 지원 중', align='centerLeft', offsetRateX=-0.05, offsetRateY=0.15, duration=12000, scale=2)
        self.set_scene_skip(state=소개_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 소개_가로줌인01(self.ctx)


class 소개_가로줌인01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walking')
        self.add_balloon_talk(spawnId=0, msg='흠…', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=101, msg='…네, 현재까지 이상 없습니다.', duration=2000, delayTick=5)
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 소개_완료(self.ctx)


class 소개_스킵완료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52020033, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 전투시작01


class 소개_완료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 조건확인_대기01(self.ctx)


class 부유도_대기(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52020033, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부유도_준비(self.ctx)


class 부유도_준비(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부유도_탐색01(self.ctx)


class 부유도_탐색01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8003], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Walking')
        self.add_cinematic_talk(npcId=0, msg='(함선 아래서부터 들려오는 요란한 소리.\n침입자를 막기 위한 결계, 그리고 방어군과의 전투가 벌어진 듯하다.)', duration=4000)
        self.set_scene_skip(state=부유도_스킵완료, action='nextState') # setsceneskip 2 set

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 부유도_탐색02(self.ctx)


class 부유도_탐색02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.add_cinematic_talk(npcId=11003650, illustId='Neirin_serious', msg='…네, 함장님.\n알겠습니다.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부유도_탐색03(self.ctx)


class 부유도_탐색03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.add_cinematic_talk(npcId=11003650, illustId='Neirin_serious', msg='$MyPCName$님. 함장님께서는 더 이상의 접근은 어렵다고 판단하셨습니다.\n스카이 포트리스로는요.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부유도_탐색04(self.ctx)


class 부유도_탐색04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003650, illustId='Neirin_serious', msg='하지만 비상 탈출에 성공하신다면 크리티아스에 진입할 수는 있을 거예요.\n위험할 수도 있겠지만…', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부유도_탐색05(self.ctx)


class 부유도_탐색05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=0, msg='어떻게든, 저곳에 가야 하니…\n무엇이든 해 보겠습니다.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부유도_탐색06(self.ctx)


class 부유도_탐색06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003650, illustId='Neirin_serious', msg='탈출용 수송선이 있는 격납고도 공격받고 있고…\n지금으로는 낙하산을 타고 주변 섬으로 내려가 경로를 찾는 방법 뿐이에요.', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 부유도_탐색07(self.ctx)


class 부유도_탐색07(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003650, illustId='Neirin_serious', msg='끝까지 지원해 드리지 못해 죄송합니다, $MyPCName$님.\n그럼… 행운을 빕니다!', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자막구간_00(self.ctx)


class 자막구간_00(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 자막구간_01(self.ctx)


class 자막구간_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='나는 작은 낙하산 하나에 몸을 의지한 채\n짙은 안개 속으로 몸을 던졌다.')
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 자막구간_03(self.ctx)


class 자막구간_02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='이방인의 침입을 허락하지 않겠다는 듯 나를 밀어내는 강한 바람…\n이 안개 너머에서는 무슨 일이 벌어지고 있는 것일까.')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return 자막구간_03(self.ctx)


class 자막구간_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=9, script='안개 사이로 찢어진 땅이 보인다….\n저곳으로 내려가, 크리티아스로 들어갈 방법을 찾아보자!')
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 부유도_종료(self.ctx)


class 부유도_스킵완료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 부유도_종료(self.ctx)


class 부유도_종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020001, portalId=1) # 안개 속 부유도로 자동 이동
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
