""" trigger/52000132_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[101,102])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001599], questStates=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001584], questStates=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001583], questStates=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[2]):
            # 엘리넬 마법학원 : 50001582 퀘스트 진행 중인 상태
            return 아이들과만남_연출대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001582], questStates=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001581], questStates=[3]):
            return 빈집(self.ctx)


class 아이들과만남_연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000132, portalId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아이들과만남_연출시작(self.ctx)


class 아이들과만남_연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrolName='MS2PatrolData_PC00')
        self.set_scene_skip(state=아이들과인사_스킵완료, action='exit') # setsceneskip set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리안인사01(self.ctx)


class 리안인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__0$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Bore_B', duration=4000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린인사01(self.ctx)


"""
class 리안인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린인사01(self.ctx)

"""


class 메린인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__1$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=6000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC인사01(self.ctx)


"""
class 메린인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC인사01(self.ctx)

"""


class PC인사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__2$', duration=3000, align='right')
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=3000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사01(self.ctx)


"""
class PC인사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사01(self.ctx)

"""


class 리안대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__3$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사01(self.ctx)


"""
class 리안대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사01(self.ctx)

"""


class 메린대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__4$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_C', duration=7000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사02(self.ctx)


"""
class 메린대사01_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사02(self.ctx)

"""


class 리안대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__5$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Bore_A', duration=3000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사02(self.ctx)


"""
class 리안대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사02(self.ctx)

"""


class PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__6$', duration=3000, align='right')
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=1000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사03(self.ctx)


"""
class PC대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사03(self.ctx)

"""


class 리안대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__7$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=6000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사02(self.ctx)


"""
class 리안대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사02(self.ctx)

"""


class 메린대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__8$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4500)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이들이동01(self.ctx)


"""
class 메린대사02_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아이들이동01(self.ctx)

"""


class 아이들이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8003], returnView=False)
        # self.move_user_path(patrolName='MS2PatrolData_PC01')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy01')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_girl01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 유저이동01(self.ctx)


class 유저이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 리안대사04(self.ctx)


class 리안대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.select_camera_path(pathIds=[8003], returnView=False)
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__9$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=7000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사03(self.ctx)


"""
class 리안대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사03(self.ctx)

"""


class 메린대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__10$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=13000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사05(self.ctx)


"""
class 메린대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사05(self.ctx)

"""


class 리안대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__11$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4300)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이들이동02(self.ctx)


"""
class 리안대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아이들이동02(self.ctx)

"""


class 아이들이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004], returnView=False)
        # self.move_user_path(patrolName='MS2PatrolData_PC01')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy02')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_girl02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 유저이동02(self.ctx)


class 유저이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC02')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 메린대사04(self.ctx)


class 메린대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__12$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=8900)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사05(self.ctx)


"""
class 메린대사04_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사05(self.ctx)

"""


class 메린대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__13$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4700)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC대사03(self.ctx)


"""
class 메린대사05_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC대사03(self.ctx)

"""


class PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=0, illustId='0', msg='$52000132_QD__MAIN__14$', duration=3000, align='right')
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=2000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사06(self.ctx)


"""
class PC대사03_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사06(self.ctx)

"""


class 리안대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__15$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사06(self.ctx)


"""
class 리안대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사06(self.ctx)

"""


class 메린대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__16$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이들이동03(self.ctx)


"""
class 메린대사06_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아이들이동03(self.ctx)

"""


class 아이들이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8004], returnView=False)
        # self.move_user_path(patrolName='MS2PatrolData_PC01')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy03')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_girl03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 유저이동03(self.ctx)


class 유저이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC03')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 메린대사07(self.ctx)


class 메린대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__17$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=7400)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 리안대사07(self.ctx)


"""
class 메린대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 리안대사07(self.ctx)

"""


class 리안대사07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__18$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3700)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사08(self.ctx)


"""
class 리안대사07_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사08(self.ctx)

"""


class 메린대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__19$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=2000)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이들이동04(self.ctx)


"""
class 메린대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아이들이동04(self.ctx)

"""


class 아이들이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8005], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy04')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_girl04')
        self.move_user_path(patrolName='MS2PatrolData_PC04')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리안대사08(self.ctx)


class 리안대사08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8006], returnView=False)
        self.add_cinematic_talk(npcId=11003253, illustId='0', msg='$52000132_QD__MAIN__20$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3200)
        self.set_skip(state=아이들과인사_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 메린대사09(self.ctx)


"""
class 리안대사08_skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 메린대사09(self.ctx)

"""


class 메린대사09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003252, illustId='0', msg='$52000132_QD__MAIN__21$', duration=3000, align='right')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아이들달림(self.ctx)


class 아이들달림(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_boy_run')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_girl_run')
        self.move_user_path(patrolName='MS2PatrolData_PC05')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아이들과인사(self.ctx)


class 아이들과인사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC06')
        self.set_pc_emotion_sequence(sequenceNames=['Hello_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 방정리(self.ctx)


class 방정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=3)
        self.destroy_monster(spawnIds=[101,102])
        self.move_user_path(patrolName='MS2PatrolData_PC06')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 유저맵이동_연출종료(self.ctx)


class 유저맵이동_연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=3)
        self.destroy_monster(spawnIds=[101,102])
        self.move_user(mapId=52000132, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 아이들과인사_스킵완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=3)
        self.destroy_monster(spawnIds=[101,102])
        self.move_user(mapId=52000132, portalId=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=3)
        self.move_user(mapId=52000133, portalId=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
