""" trigger/02000072_in/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001566], questStates=[3]):
            return 환자홀로있는집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001566], questStates=[2]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001566], questStates=[1]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001565], questStates=[3]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001565], questStates=[2]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001565], questStates=[1]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[3]):
            return 아르마노가출후(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[1]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[3]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[2]):
            return 아르마노가출전(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001563], questStates=[1]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[3]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001562], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001561], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001560], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001559], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001559], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001559], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001558], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001558], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001558], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001557], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001557], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001557], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001556], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001556], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001556], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001555], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001555], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001555], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001554], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001554], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001554], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001553], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001553], questStates=[2]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001553], questStates=[1]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[3]):
            return 마노비치혼자(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 오스칼퇴장대기(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[1]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[3]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[2]):
            return 침공직후상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[1]):
            return 빈집(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101,102,103,104,105,106,107])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 침공직후상태(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 오스칼퇴장연출(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[1]):
            return 침공직후상태01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[3]):
            return 침공직후상태01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001551], questStates=[2]):
            return 침공직후상태01(self.ctx)


class 침공직후상태01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 오스칼퇴장연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 침공직후상태02(self.ctx)
        """
        <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001551" arg3="3"> 
                <transition state="침공직후상태02"/>
            </condition>        
            <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001551" arg3="2"> 
                <transition state="침공직후상태02"/>
            </condition>
        """


class 침공직후상태02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 오스칼퇴장연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 침공직후상태01(self.ctx)
        """
        <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001552" arg3="1"> 
                <transition state="침공직후상태01"/>
            </condition>    
            <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001551" arg3="3"> 
                <transition state="침공직후상태01"/>
            </condition>        
            <condition name="퀘스트유저를감지하면" arg1="9000" arg2="50001551" arg3="2"> 
                <transition state="침공직후상태01"/>
            </condition>
        """


class 오스칼퇴장대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 오스칼퇴장연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 퀘스트조건체크(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 오스칼퇴장연출(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_Wayout_102_O')
        self.add_balloon_talk(spawnId=102, msg='$02000072_IN__MAIN__0$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 오스칼퇴장연출종료(self.ctx)


class 오스칼퇴장연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.destroy_monster(spawnIds=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001552], questStates=[2]):
            return 종료(self.ctx)
        """
        <condition name="!퀘스트유저를감지하면" arg1="9000" arg2="50001552" arg3="2"> 
                    <transition state="퀘스트조건체크"/>
                </condition>
        """


# 50001552 완료가능시 오스칼 퇴장하는 연출 종료
class 마노비치혼자(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 아르마노가출전(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,104,105,106], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출전01(self.ctx)


class 아르마노가출전01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출전02(self.ctx)


class 아르마노가출전02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출연출(self.ctx)
        if not self.quest_user_detected(boxIds=[9000], questIds=[50001564], questStates=[2]):
            return 아르마노가출전01(self.ctx)


class 아르마노가출대기(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,104,105,106], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 아르마노가출연출(self.ctx)


class 아르마노가출연출(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8010], returnView=False)
        self.move_user(mapId=2000072, portalId=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 아르마노대사01(self.ctx)


class 아르마노대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8011], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__1$', arg4=4, arg5=0)
        self.set_scene_skip(state=아르마노가출_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 아르마노대사02(self.ctx)


class 아르마노대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__2$', arg4=5, arg5=0)
        # <action name="NPC를이동시킨다" arg1="104" arg2="MS2PatrolData_Wayout_104_A" />
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스칼대사01(self.ctx)


class 오스칼대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8013], returnView=False)
        self.set_conversation(type=2, spawnId=11003245, script='$02000072_IN__MAIN__3$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 아르마노대사03(self.ctx)


class 아르마노대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__4$', arg4=5, arg5=0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 오스칼대사02(self.ctx)


class 오스칼대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8013], returnView=False)
        self.set_conversation(type=2, spawnId=11003245, script='$02000072_IN__MAIN__5$', arg4=8, arg5=0)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=8000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7500):
            return 오스칼대사03(self.ctx)


class 오스칼대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8013], returnView=False)
        self.set_conversation(type=2, spawnId=11003245, script='$02000072_IN__MAIN__6$', arg4=8, arg5=0)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=8000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 오스칼대사04(self.ctx)


class 오스칼대사04(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003245, script='$02000072_IN__MAIN__7$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Talk_A', duration=8000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 아르마노대사04(self.ctx)


class 아르마노대사04(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__8$', arg4=6, arg5=0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 아르마노대사05(self.ctx)


class 아르마노대사05(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__9$', arg4=8, arg5=0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 프레이대사01(self.ctx)


class 프레이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8012], returnView=False)
        self.set_conversation(type=2, spawnId=11003246, script='$02000072_IN__MAIN__10$', arg4=7, arg5=0)
        self.set_npc_emotion_loop(spawnId=106, sequenceName='Talk_A', duration=4000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 아르마노대사06(self.ctx)


class 아르마노대사06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__11$', arg4=8, arg5=0)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 프레이대사02(self.ctx)


class 프레이대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8012], returnView=False)
        self.set_conversation(type=2, spawnId=11003246, script='$02000072_IN__MAIN__12$', arg4=9, arg5=0)
        self.set_npc_emotion_loop(spawnId=106, sequenceName='Talk_A', duration=9000)
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 아르마노대사07(self.ctx)


class 아르마노대사07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8014,8015], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__13$', arg4=3, arg5=0)
        self.create_monster(spawnIds=[107])
        self.set_skip(state=아르마노가출_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아르마노대사08(self.ctx)


class 아르마노대사08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8015], returnView=False)
        self.set_conversation(type=2, spawnId=11003244, script='$02000072_IN__MAIN__14$', arg4=6, arg5=0)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 아르마노탈주(self.ctx)


class 아르마노탈주(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_Wayout_104_A')
        self.move_npc(spawnId=107, patrolName='MS2PatrolData_Walkin_107_J')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PC멈칫(self.ctx)


class PC멈칫(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[104])
        self.move_user_path(patrolName='MS2PatrolData_PC_Follow')
        # <action name="NPC를이동시킨다" arg1="107" arg2="MS2PatrolData_Walkin_107_J" />
        self.set_conversation(type=1, spawnId=0, script='$02000072_IN__MAIN__15$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 조디등장(self.ctx)


class 조디등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8016], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 조디대사01(self.ctx)


class 조디대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8017], returnView=False)
        self.set_conversation(type=2, spawnId=11003247, script='$02000072_IN__MAIN__16$', arg4=3, arg5=0)
        self.set_npc_emotion_loop(spawnId=107, sequenceName='Talk_A', duration=3000)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조디대사02(self.ctx)


class 조디대사02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003247, script='$02000072_IN__MAIN__17$', arg4=4, arg5=0)
        self.set_npc_emotion_loop(spawnId=107, sequenceName='Talk_A', duration=4000)
        # Missing State: 아르마노가출_스킵완료_조디제외
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC안녕(self.ctx)


class PC안녕(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Hello_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 조디대사03(self.ctx)


class 조디대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11003247, script='$02000072_IN__MAIN__18$', arg4=3, arg5=0)
        self.set_scene_skip() # setsceneskip 1 close

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 아르마노가출연출종료(self.ctx)


class 아르마노가출_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[107,108]) # 중복 스폰 막기 위해 이동하는 조디, 고정된 조디 소멸 처리
        self.destroy_monster(spawnIds=[104]) # 과정상 사라지는 아르마노 소멸
        self.create_monster(spawnIds=[108]) # 퀘스트 완료 npc 조디 스폰
        self.move_user_path(patrolName='MS2PatrolData_PC_Follow') # PC 조디 앞으로 이동. 안 되면 포탈 위치로 이동시킬 것

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 아르마노가출연출종료(self.ctx)


class 아르마노가출연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 아르마노가출후(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103,105,106,108], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001566], questStates=[3]):
            return 환자홀로있는집(self.ctx)
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 환자홀로있는집(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
