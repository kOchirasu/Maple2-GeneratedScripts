""" trigger/52000121_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.create_monster(spawnIds=[121,122,123,124,125,126,127,128,129,130,131], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[1]):
            return 연출준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[2]):
            return 최종맵이동(self.ctx)


class 연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103,104], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 위기상황00(self.ctx)


class 위기상황00(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.select_camera_path(pathIds=[8000], returnView=False)
        self.set_scene_skip(state=전투직전_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return 위기상황01(self.ctx)


class 위기상황01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 위기상황02(self.ctx)


class 위기상황02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 위기상황03(self.ctx)


class 위기상황03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 위기상황04(self.ctx)


class 위기상황04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 대치상황시작(self.ctx)


class 대치상황시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8010], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 오스칼대사01(self.ctx)


class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003309, script='$52000121_QD__MAIN__0$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Talk_B', duration=4000)
        self.set_skip(state=오스칼대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 투르카대사01(self.ctx)


class 오스칼대사01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 투르카대사01(self.ctx)


class 투르카대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__1$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Bore_B', duration=4000)
        self.set_skip(state=투르카대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 마노비치대사01(self.ctx)


class 투르카대사01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사01(self.ctx)


class 마노비치대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8022], returnView=False)
        self.set_conversation(type=2, spawnId=11003308, script='$52000121_QD__MAIN__2$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=마노비치대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대사02(self.ctx)


class 마노비치대사01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 투르카대사02(self.ctx)


class 투르카대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8023], returnView=False)
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__3$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=투르카대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대사03(self.ctx)


class 투르카대사02_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 투르카대사03(self.ctx)


class 투르카대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__4$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=3000)
        self.set_skip(state=투르카대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오스칼대사02(self.ctx)


class 투르카대사03_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 오스칼대사02(self.ctx)


class 오스칼대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8021], returnView=False)
        self.set_conversation(type=2, spawnId=11003309, script='$52000121_QD__MAIN__5$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Attack_Idle_A', duration=4000)
        self.set_skip(state=오스칼대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대사04(self.ctx)


class 오스칼대사02_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 투르카대사04(self.ctx)


class 투르카대사04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8023], returnView=False)
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__6$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=투르카대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아르마노열폭준비(self.ctx)


class 투르카대사04_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아르마노열폭준비(self.ctx)


class 아르마노열폭준비(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8025], returnView=False)
        self.face_emotion(spawnId=104, emotionName='Angry')
        # <action name="SetNpcEmotionLoop" arg1="104" arg2="Talk_A" arg3="1000"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아르마노열폭시작(self.ctx)


class 아르마노열폭시작(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=104, emotionName='Angry')
        self.add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__7$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아르마노달려(self.ctx)


class 아르마노달려(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8024], returnView=False)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104_run')
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_101_Attack" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카공격00(self.ctx)


class 투르카공격00(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8030], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_Attack')
        self.add_cinematic_talk(npcId=11003362, msg='$52000121_QD__MAIN__8$', duration=1000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 투르카공격01(self.ctx)


class 투르카공격01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8031], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_02_B')
        self.set_npc_emotion_loop(spawnId=104, sequenceName='Run_A', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 마노비치대사02(self.ctx)


class 마노비치대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8022], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=11003308, msg='$52000121_QD__MAIN__9$', duration=1500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 리셋대기01(self.ctx)


class 리셋대기01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,104])
        self.create_monster(spawnIds=[105,106], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 리셋대기02(self.ctx)


class 리셋대기02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8040], returnView=False)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Down_Idle_A', duration=30000)
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 잠시후(self.ctx)


class 잠시후(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8041], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 불효자멘붕(self.ctx)


class 불효자멘붕(trigger_api.Trigger):
    def on_enter(self):
        self.face_emotion(spawnId=106, emotionName='Cry')
        self.add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__10$', duration=1500, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 오스칼멘붕(self.ctx)


class 오스칼멘붕(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=103, sequenceName='Stun_A', duration=3000)
        self.add_cinematic_talk(npcId=11003309, illustId='Oskhal_normal', msg='$52000121_QD__MAIN__11$', duration=2000, align='left')
        self.set_skip(state=오스칼멘붕_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 투르카대사05(self.ctx)


class 오스칼멘붕_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 투르카대사05(self.ctx)


class 투르카대사05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8035], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_01')
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__12$', arg4=4, arg5=0)
        self.set_skip(state=투르카대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC등장대기(self.ctx)


class 투르카대사05_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return PC등장대기(self.ctx)


class PC등장대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8036], returnView=False)
        self.move_user(mapId=52000121, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 투르카대사06(self.ctx)


class 투르카대사06(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_02')
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__13$', arg4=3, arg5=0)
        # <action name="스킵을설정한다" arg1="투르카대사06_skip"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC등장(self.ctx)


class PC등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8034], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_PC_Run')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_04')
        self.set_conversation(type=1, spawnId=0, script='$52000121_QD__MAIN__14$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 투르카대사07(self.ctx)


class 투르카대사07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8036], returnView=False)
        # <action name="NPC를이동시킨다" arg1="101" arg2="MS2PatrolData_101_disappear_02" />
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__15$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 투르카대사08(self.ctx)


class 투르카대사08(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101_disappear_03')
        self.set_conversation(type=2, spawnId=11003362, script='$52000121_QD__MAIN__16$', arg4=2, arg5=0)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몬스터등장00(self.ctx)


class 몬스터등장00(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111], animationEffect=True)
        self.destroy_monster(spawnIds=[101])
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장01(self.ctx)


class 몬스터등장01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8037], returnView=False)
        self.destroy_monster(spawnIds=[103])
        self.create_monster(spawnIds=[110], animationEffect=True)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장02(self.ctx)


class 몬스터등장02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8038], returnView=False)
        self.create_monster(spawnIds=[108], animationEffect=True)
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장03(self.ctx)


class 몬스터등장03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8039], returnView=False)
        self.create_monster(spawnIds=[112], animationEffect=True)
        self.set_skip()
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투대기01(self.ctx)


class 전투직전_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[8036], returnView=False)
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,108])
        self.create_monster(spawnIds=[105,106], animationEffect=False)
        self.create_monster(spawnIds=[108,110,111,112], animationEffect=True)
        self.move_user(mapId=52000121, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투대기01(self.ctx)


class 전투대기01(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=2)
        # <action name="AddCinematicTalk" npcID="29000251" illustID="Oskhal_normal" msg="$52000121_QD__MAIN__17$" duration="2000" align="left" />

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투준비01(self.ctx)


class 전투준비01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[110,111,112]):
            return 전투시작02(self.ctx)


class 전투시작02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[113,114,115], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[113,114,115]):
            return 전투끝(self.ctx)


class 전투끝(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8040], returnView=False)
        self.set_achievement(triggerId=9000, type='trigger', achieve='ManovichMobKill')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 암전02(self.ctx)


class 암전02(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return npc교체01(self.ctx)


class npc교체01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[108])
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 아빠와아들대기(self.ctx)


class 아빠와아들대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8040], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=마노비치리타이어_스킵완료, action='exit') # setsceneskip 2 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마노비치대사03(self.ctx)


class 마노비치대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__18$', arg4=2, arg5=0)
        self.set_skip(state=마노비치대사03_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아르마노대사01(self.ctx)


class 마노비치대사03_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아르마노대사01(self.ctx)


class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8042], returnView=False)
        self.set_conversation(type=2, spawnId=11003364, script='$52000121_QD__MAIN__19$', arg4=3, arg5=0)
        self.set_skip(state=아르마노대사01_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아르마노대사02(self.ctx)


class 아르마노대사01_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 아르마노대사02(self.ctx)


class 아르마노대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003364, script='$52000121_QD__MAIN__20$', arg4=3, arg5=0)
        self.set_skip(state=아르마노대사02_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마노비치대사04(self.ctx)


class 아르마노대사02_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사04(self.ctx)


class 마노비치대사04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8041], returnView=False)
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__21$', arg4=3, arg5=0)
        self.set_skip(state=마노비치대사04_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마노비치대사05(self.ctx)


class 마노비치대사04_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사05(self.ctx)


class 마노비치대사05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__22$', arg4=3, arg5=0)
        self.set_skip(state=마노비치대사05_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마노비치대사06(self.ctx)


class 마노비치대사05_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사06(self.ctx)


class 마노비치대사06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8046], returnView=False)
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__23$', arg4=3, arg5=0)
        self.set_skip(state=마노비치대사06_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 마노비치대사07(self.ctx)


class 마노비치대사06_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사07(self.ctx)


class 마노비치대사07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8043], returnView=False)
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__24$', arg4=2, arg5=0)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Event_02_A')
        self.set_skip(state=마노비치대사07_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마노비치대사08(self.ctx)


class 마노비치대사07_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치대사08(self.ctx)


class 마노비치대사08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8047], returnView=False)
        self.set_conversation(type=2, spawnId=11003361, script='$52000121_QD__MAIN__25$', arg4=2, arg5=0)
        # <action name="SetNpcEmotionSequence" arg1="105" arg2="Event_03_A"/>
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Event_03_A', duration=10000)
        self.set_skip(state=마노비치대사08_skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 마노비치죽음(self.ctx)


class 마노비치대사08_skip(trigger_api.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 마노비치죽음(self.ctx)


class 마노비치죽음(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8044], returnView=False)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Event_04_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 아르마노오열(self.ctx)


class 아르마노오열(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8050], returnView=False)
        self.add_cinematic_talk(npcId=11003364, msg='$52000121_QD__MAIN__26$', duration=4000, align='left')
        self.set_scene_skip() # setsceneskip 2 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 마노비치리타이어_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[108])
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=9000, type='trigger', achieve='ManovichRetire')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


class 최종맵이동(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000072, portalId=1)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_WhiteFlash.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 최종맵이동(self.ctx)


initial_state = 대기
