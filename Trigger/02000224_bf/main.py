""" trigger/02000224_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[2]):
            return 다음맵으로(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 연출준비00(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[3]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[2]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[1]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[3]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[2]):
            return 아르마노있음(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[1]):
            return 기본상태(self.ctx)


class 기본상태(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 아르마노있음(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 연출준비(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 다음맵으로(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[104], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return 연출종료(self.ctx)


class 연출준비00(common.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=아르마노말썽_스킵완료, action='exit') # setsceneskip 정의
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 연출준비(self.ctx)


class 연출준비(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_user(mapId=2000224, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 티니에등장(self.ctx)


class 티니에등장(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__18$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Bore_C', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 티니에이동01(self.ctx)


class 티니에이동01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_girl01')
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__0$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아르마노대사01(self.ctx)


class 아르마노대사01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__1$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 티니에대사01(self.ctx)


class 아르마노대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에대사01(self.ctx)


class 티니에대사01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__2$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=티니에대사01_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6765):
            return 아르마노대사02(self.ctx)


class 티니에대사01_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아르마노대사02(self.ctx)


class 아르마노대사02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_girl02')
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__3$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4597):
            return 티니에대사02(self.ctx)


class 아르마노대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에대사02(self.ctx)


class 티니에대사02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__4$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=티니에대사02_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7471):
            return 티니에이동02(self.ctx)


class 티니에대사02_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에이동02(self.ctx)


class 티니에이동02(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_girl02')
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__5$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10109):
            return 티니에대사03(self.ctx)


class 티니에대사03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__6$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=티니에대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=9090):
            return 아르마노대사03(self.ctx)


class 티니에대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아르마노대사03(self.ctx)


class 아르마노대사03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__7$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아르마노대사03_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5146):
            return 티니에대사04(self.ctx)


class 아르마노대사03_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에대사04(self.ctx)


class 티니에대사04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__8$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=티니에대사04_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7418):
            return 아르마노대사04(self.ctx)


class 티니에대사04_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아르마노대사04(self.ctx)


class 아르마노대사04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__9$', arg4=4, arg5=0)
        self.set_skip(state=아르마노대사04_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아르마노대사05(self.ctx)


class 아르마노대사04_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아르마노대사05(self.ctx)


class 아르마노대사05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_conversation(type=2, spawnId=11003242, script='$02000224_BF__MAIN__10$', arg4=3, arg5=0)
        self.set_skip(state=아르마노대사05_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3030):
            return 아르마노탈주(self.ctx)


class 아르마노대사05_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 아르마노탈주(self.ctx)


class 아르마노탈주(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy01')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 티니에대사05(self.ctx)


class 티니에대사05(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_girl03')
        self.destroy_monster(spawnIds=[101])
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__11$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 티니에대사06(self.ctx)


class 티니에대사06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC01')
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__12$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Bore_C', duration=4000)
        self.set_skip(state=티니에대사06_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=11023):
            return PC대사01(self.ctx)


class 티니에대사06_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return PC대사01(self.ctx)


class PC대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02000224_BF__MAIN__13$', arg4=3, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 티니에대사07(self.ctx)


class 티니에대사07(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__14$', arg4=4, arg5=0)
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='ChatUp_A')
        self.set_skip(state=티니에대사07_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7810):
            return PC대사02(self.ctx)


class 티니에대사07_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에대사08(self.ctx)


class PC대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$02000224_BF__MAIN__15$', arg4=3, arg5=0)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 티니에대사08(self.ctx)


class 티니에대사08(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__16$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=티니에대사08_skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7497):
            return 티니에대사09(self.ctx)


class 티니에대사08_skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 티니에대사09(self.ctx)


class 티니에대사09(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003243, script='$02000224_BF__MAIN__17$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7157):
            return 연출종료(self.ctx)


class 아르마노말썽_스킵완료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,103])
        self.create_monster(spawnIds=[104], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='foolishson')
        self.move_user(mapId=2000054, portalId=10)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
