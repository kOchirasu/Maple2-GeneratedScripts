""" trigger/52000068_qd/tria_seige_movie_02.xml """
from common import *
import state


class 연출페이즈2검사(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[20002264], questIds=[20002264], questStates=[3]):
            return 연출페이즈2시작()


#  챕터5 에필로그 [10002105 엇갈리는 마음]완료 시 연출맵으로 이동
class 연출페이즈2시작(state.State):
    def on_enter(self):
        set_scene_skip(state=Quit, arg2='exit')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000068, portalId=3)
        create_monster(spawnIds=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], arg2=False)
        create_monster(spawnIds=[13000,13001,13002,13003,13004,13005,13006,13007], arg2=False)
        destroy_monster(spawnIds=[11000,11001,11002,11003,11004,11005,11006,11007], arg2=False)
        set_visible_breakable_object(triggerIds=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012], arg2=False)
        set_sound(triggerId=90001, arg2=True) # TriaAttack

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출페이즈2대사01()


class 연출페이즈2대사01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        select_camera_path(pathIds=[15000,15001], returnView=False)
        set_conversation(type=2, spawnId=11001966, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__0$', arg4=7)
        set_skip(state=연출페이즈2대사01스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사01스킵()


class 연출페이즈2대사01스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사02()


class 연출페이즈2대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001966, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__1$', arg4=7)
        set_skip(state=연출페이즈2대사02스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사02스킵()


class 연출페이즈2대사02스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사03()


class 연출페이즈2대사03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15002,15003], returnView=False)
        set_conversation(type=2, spawnId=11001901, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__2$', arg4=7)
        set_skip(state=연출페이즈2대사03스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사03스킵()


class 연출페이즈2대사03스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사04()


class 연출페이즈2대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15004], returnView=False)
        set_conversation(type=2, spawnId=11001961, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__3$', arg4=7)
        set_skip(state=연출페이즈2대사04스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사04스킵()


class 연출페이즈2대사04스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사04b()


class 연출페이즈2대사04b(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15005,15006], returnView=False)
        set_conversation(type=2, spawnId=11001972, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__4$', arg4=7)
        set_skip(state=연출페이즈2대사04b스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 연출페이즈2대사04b스킵()


class 연출페이즈2대사04b스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사05()


class 연출페이즈2대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15007], returnView=False)
        set_conversation(type=2, spawnId=11001972, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__5$', arg4=7)
        set_skip(state=연출페이즈2대사05스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사05스킵()


class 연출페이즈2대사05스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사05b()


class 연출페이즈2대사05b(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15100,15101], returnView=False)
        set_conversation(type=2, spawnId=11001970, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__17$', arg4=7)
        set_skip(state=연출페이즈2대사05b스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사05b스킵()


class 연출페이즈2대사05b스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사06()


class 연출페이즈2대사06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15102,15103], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__6$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사06스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사06스킵()


class 연출페이즈2대사06스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사07()


class 연출페이즈2대사07(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15104,15105], returnView=False)
        move_npc(spawnId=13000, patrolName='MS2PatrolData_top_ereb_go') # 에레브 이동
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__7$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사07스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사07스킵()


class 연출페이즈2대사07스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사08()


class 연출페이즈2대사08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15106], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_sad', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__8$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사08스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사08스킵()


class 연출페이즈2대사08스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사09()


class 연출페이즈2대사09(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15107,15108], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__9$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사09스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사09스킵()


class 연출페이즈2대사09스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사10()


class 연출페이즈2대사10(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__10$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사10스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사10스킵()


class 연출페이즈2대사10스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사11()


class 연출페이즈2대사11(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15109], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__11$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사11스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사11스킵()


class 연출페이즈2대사11스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사12()


class 연출페이즈2대사12(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15110], returnView=False)
        set_conversation(type=2, spawnId=11001973, script='$52000068_QD__TRIA_SEIGE_MOVIE_02__18$', arg4=7)
        set_skip(state=연출페이즈2대사12스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사12스킵()


class 연출페이즈2대사12스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사13()


class 연출페이즈2대사13(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15111,15112], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__12$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사13스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출페이즈2대사13스킵()


class 연출페이즈2대사13스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사14()


class 연출페이즈2대사14(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__13$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사14스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사14스킵()


class 연출페이즈2대사14스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사15()


class 연출페이즈2대사15(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15113,15114], returnView=False)
        move_npc(spawnId=13000, patrolName='MS2PatrolData_top_ereb_back') # 에레브 이동
        add_cinematic_talk(npcId=11000075, illustId='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__14$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사15스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사15스킵()


class 연출페이즈2대사15스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사16()


class 연출페이즈2대사16(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000075, illustId='Ereb_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__15$', duration=7000, align='center')
        set_skip(state=연출페이즈2대사16스킵)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출페이즈2대사16스킵()


class 연출페이즈2대사16스킵(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return 연출페이즈2대사17()


class 연출페이즈2대사17(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[15115,15116], returnView=False)
        add_cinematic_talk(npcId=11000075, illustId='Ereb_serious', msg='$52000068_QD__TRIA_SEIGE_MOVIE_02__16$', duration=7000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 페이드아웃()


class 페이드아웃(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        remove_cinematic_talk()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 페이드아웃_1()


class 페이드아웃_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        move_user(mapId=2000001, portalId=17)


