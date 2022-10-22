""" trigger/02000338_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[120], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[121], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[122], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[123], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[124], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[110], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[111], visible=False, animationEffect=False, animationDelay=0)
        set_ladder(triggerIds=[112], visible=False, animationEffect=False, animationDelay=0)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20,21,22,23,24,25,26,27,28,29,30,31,32], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020,20021,20022,20023,20024,20025,20026,20027,20028,20029,20030,20031,20032,20033,20034,20035,20036,20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050,20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064,20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080,20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093,20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106,20107,20108,20109,20110,20111,20112,20113,20114,20115,20116,20117,20118,20119,20120,20121,20122,20123,20124,20125,20126,20127,20128,20129,20130,20131,20132,20133,20134,20135,20136,20137,20138,20139,20140,20141,20142,20143,20144,20145,20146,20147,20148,20149,20150,20151,20152,20153,20154,20155,20156,20157,20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169,20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184,20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198,20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210,20211,20212,20213,20214,20215,20216,20217,20218,20219,20220,20221,20222,20223,20224,20225,20226,20227,20228,20229,20230,20231,20232,20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247], visible=True, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[32000], visible=False) # Vibrate
        set_effect(triggerIds=[32001], visible=False) # Vibrate
        set_effect(triggerIds=[32002], visible=True) # monochrome
        set_effect(triggerIds=[90000], visible=False) # monochrome
        set_effect(triggerIds=[73001], visible=False) # DownArrow
        set_effect(triggerIds=[73002], visible=False) # DownArrow
        set_effect(triggerIds=[74500], visible=False)
        set_effect(triggerIds=[75000], visible=False) # GuideArrow
        set_effect(triggerIds=[75001], visible=False) # GuideArrow
        set_effect(triggerIds=[75002], visible=False) # GuideArrow
        set_effect(triggerIds=[75003], visible=False) # GuideArrow
        set_effect(triggerIds=[75004], visible=False) # GuideArrow
        set_effect(triggerIds=[75005], visible=False) # GuideArrow
        set_effect(triggerIds=[76000], visible=False) # GuideArrow
        set_effect(triggerIds=[76001], visible=False) # GuideArrow
        set_effect(triggerIds=[76002], visible=False) # GuideArrow
        set_effect(triggerIds=[73004], visible=False)
        set_effect(triggerIds=[73005], visible=False)
        set_effect(triggerIds=[73006], visible=False)
        set_effect(triggerIds=[73007], visible=False)
        set_effect(triggerIds=[74512], visible=False)
        destroy_monster(spawnIds=[5000])
        destroy_monster(spawnIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009,5010])
        set_interact_object(triggerIds=[10000777], state=0)
        set_interact_object(triggerIds=[10000778], state=0)
        set_interact_object(triggerIds=[10000779], state=0)
        set_interact_object(triggerIds=[10000780], state=0)
        set_interact_object(triggerIds=[10000781], state=0)
        set_interact_object(triggerIds=[10000782], state=0)
        create_monster(spawnIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109], arg2=False)
        set_mesh(triggerIds=[33,34,35,36,37,38,39,40,41], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[42,43,44,45,46,47,48], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[49,50,51,52,53,54,55], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[56,57,58,59,60,61,62,63,64,65,66], visible=False, arg3=0, arg4=0, arg5=0)
        destroy_monster(spawnIds=[5100])
        destroy_monster(spawnIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5121,5122,5123,5124,5125])
        set_mesh(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_agent(triggerIds=[8000], visible=True)
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        set_agent(triggerIds=[8009], visible=True)
        set_agent(triggerIds=[8010], visible=True)
        set_agent(triggerIds=[8011], visible=True)
        set_agent(triggerIds=[8012], visible=True)
        set_agent(triggerIds=[8013], visible=True)
        set_agent(triggerIds=[8014], visible=True)
        set_agent(triggerIds=[8015], visible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return state.DungeonStart()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[5100], arg2=False)
        set_mesh(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[70010], visible=True, arg3=250, arg4=50, arg5=2)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraWalk01()

state.DungeonStart = DungeonStart


class CameraWalk01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[74512], visible=True)
        select_camera(triggerId=30200, enable=True)
        set_skip(state=CameraWalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CameraWalk03()


class CameraWalk03(state.State):
    def on_enter(self):
        select_camera(triggerId=30201, enable=True)
        set_skip(state=CameraWalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return CameraWalk04()


class CameraWalk04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_effect(triggerIds=[74500], visible=True)
        set_skip(state=CameraWalk05)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return CameraWalk05()


class CameraWalk05(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5000], arg2=False)
        move_npc(spawnId=5000, patrolName='MS2PatrolData5000')
        set_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return GroundFall01()


class GroundFall01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[32000], visible=True)
        set_effect(triggerIds=[32001], visible=True)
        set_mesh(triggerIds=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020], visible=False, arg3=100, arg4=0, arg5=0)
        set_mesh(triggerIds=[20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247], visible=False, arg3=100, arg4=0, arg5=50)
        set_mesh(triggerIds=[20226,20227,20228,20229,20230,20231], visible=False, arg3=100, arg4=0, arg5=0)
        set_mesh(triggerIds=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034], visible=False, arg3=200, arg4=0, arg5=0)
        set_mesh(triggerIds=[20021,20022,20023,20024,20025,20026,20027,20028], visible=False, arg3=250, arg4=50, arg5=2)
        set_mesh(triggerIds=[20029,20030,20031,20032,20033,20034,20035,20036], visible=False, arg3=500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050], visible=False, arg3=750, arg4=50, arg5=2)
        set_mesh(triggerIds=[20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064], visible=False, arg3=1000, arg4=50, arg5=2)
        set_mesh(triggerIds=[20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080], visible=False, arg3=1250, arg4=50, arg5=2)
        set_mesh(triggerIds=[20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093], visible=False, arg3=1500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106], visible=False, arg3=1500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20107,20108,20109,20110,20111,20112,20113,20114,20115], visible=False, arg3=1750, arg4=50, arg5=2)
        set_mesh(triggerIds=[20116,20117,20118,20119,20120,20121,20122,20123], visible=False, arg3=2000, arg4=50, arg5=2)
        set_mesh(triggerIds=[20124,20125,20126,20127,20128,20129], visible=False, arg3=2250, arg4=50, arg5=2)
        set_mesh(triggerIds=[20130,20131,20132,20133,20134,20135], visible=False, arg3=2500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20136,20137,20138,20139,20140,20141,20142,20143], visible=False, arg3=2750, arg4=50, arg5=2)
        set_mesh(triggerIds=[20144,20145,20146,20147,20148,20149,20150,20151,20152], visible=False, arg3=3000, arg4=50, arg5=2)
        set_mesh(triggerIds=[20153,20154,20155,20156,20157], visible=False, arg3=3250, arg4=50, arg5=2)
        set_mesh(triggerIds=[20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169], visible=False, arg3=3500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20232], visible=False, arg3=3500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184], visible=False, arg3=3750, arg4=50, arg5=2)
        set_mesh(triggerIds=[20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198], visible=False, arg3=4000, arg4=50, arg5=2)
        set_mesh(triggerIds=[20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210], visible=False, arg3=4250, arg4=50, arg5=2)
        set_mesh(triggerIds=[20211,20212,20213,20214,20215,20216], visible=False, arg3=4500, arg4=50, arg5=2)
        set_mesh(triggerIds=[20217,20218,20219], visible=False, arg3=4750, arg4=50, arg5=2)
        set_mesh(triggerIds=[20220,20221,20222,20223,20224,20225], visible=False, arg3=5000, arg4=50, arg5=2)
        set_skip(state=차어나운스3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차어나운스3()


class 차어나운스3(state.State):
    def on_enter(self):
        set_skip()
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Ready01()


class Ready01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_mesh(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010], visible=False, arg3=0, arg4=0, arg5=0)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[75000], visible=True) # GuideArrow
        set_effect(triggerIds=[75001], visible=True) # GuideArrow
        set_effect(triggerIds=[75002], visible=True) # GuideArrow
        set_effect(triggerIds=[75003], visible=True) # GuideArrow
        set_effect(triggerIds=[75004], visible=True) # GuideArrow
        set_effect(triggerIds=[75005], visible=True) # GuideArrow
        set_mesh(triggerIds=[20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20233,20234,20235,20236,20237,20238,20239,20240,20241,20242,20243,20244,20245,20246,20247], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20226,20227,20228,20229,20230,20231], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20021,20022,20023,20024,20025,20026,20027,20028], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20029,20030,20031,20032,20033,20034,20035,20036], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20107,20108,20109,20110,20111,20112,20113,20114,20115], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20116,20117,20118,20119,20120,20121,20122,20123], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20124,20125,20126,20127,20128,20129], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20130,20131,20132,20133,20134,20135], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20136,20137,20138,20139,20140,20141,20142,20143], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20144,20145,20146,20147,20148,20149,20150,20151,20152], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20153,20154,20155,20156,20157], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20158,20159,20160,20161,20162,20163,20164,20165,20166,20167,20168,20169], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20232], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20170,20171,20172,20173,20174,20175,20176,20177,20178,20179,20180,20181,20182,20183,20184], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20185,20186,20187,20188,20189,20190,20191,20192,20193,20194,20195,20196,20197,20198], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20199,20200,20201,20202,20203,20204,20205,20206,20207,20208,20209,20210], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20211,20212,20213,20214,20215,20216], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20217,20218,20219], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[20220,20221,20222,20223,20224,20225], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FirstBattle01()


class FirstBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        create_monster(spawnIds=[5001,5002,5003], arg2=False)
        set_effect(triggerIds=[73001], visible=True)
        set_interact_object(triggerIds=[10000777], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000777], arg2=0):
            return FirstBridgeOn01()


class FirstBridgeOn01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[75000], visible=False) # GuideArrow
        set_effect(triggerIds=[75001], visible=False) # GuideArrow
        set_effect(triggerIds=[75002], visible=False) # GuideArrow
        set_effect(triggerIds=[75003], visible=False) # GuideArrow
        set_effect(triggerIds=[75004], visible=False) # GuideArrow
        set_effect(triggerIds=[75005], visible=False) # GuideArrow
        set_agent(triggerIds=[8000], visible=False)
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        hide_guide_summary(entityId=20003382)
        set_effect(triggerIds=[73001], visible=False)
        set_mesh(triggerIds=[20,21,22,23,24,25,26,27,28,29,30,31,32], visible=True, arg3=100, arg4=50, arg5=2)
        create_monster(spawnIds=[5004,5005,5006,5007,5008,5009,5010], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return SecondBattle01()


class SecondBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        set_interact_object(triggerIds=[10000778], state=1)
        set_effect(triggerIds=[73002], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000778], arg2=0):
            return SecondBridgeOn01()


class SecondBridgeOn01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        hide_guide_summary(entityId=20003382)
        show_guide_summary(entityId=20003386, textId=20003386, duration=5000)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        set_effect(triggerIds=[73002], visible=False)
        set_mesh(triggerIds=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], visible=True, arg3=100, arg4=50, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[5000]):
            return ThirdBattle01()


class ThirdBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[76000], visible=True) # GuideArrow
        set_effect(triggerIds=[76001], visible=True) # GuideArrow
        set_effect(triggerIds=[76002], visible=True) # GuideArrow
        set_ladder(triggerIds=[120], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[121], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[122], visible=True, animationEffect=True, animationDelay=6)
        set_ladder(triggerIds=[123], visible=True, animationEffect=True, animationDelay=8)
        set_ladder(triggerIds=[124], visible=True, animationEffect=True, animationDelay=10)
        set_ladder(triggerIds=[110], visible=True, animationEffect=True, animationDelay=2)
        set_ladder(triggerIds=[111], visible=True, animationEffect=True, animationDelay=4)
        set_ladder(triggerIds=[112], visible=True, animationEffect=True, animationDelay=6)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999998]):
            return ThirdBrigeOn01()


class ThirdBrigeOn01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[76000], visible=False) # GuideArrow
        set_effect(triggerIds=[76001], visible=False) # GuideArrow
        set_effect(triggerIds=[76002], visible=False) # GuideArrow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return FourthBattle01()


class FourthBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        set_interact_object(triggerIds=[10000779], state=1)
        set_effect(triggerIds=[73004], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000779], arg2=0):
            return FourthBridgeOn01()


class FourthBridgeOn01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20003382)
        set_effect(triggerIds=[73004], visible=False)
        set_mesh(triggerIds=[33,34,35,36,37,38,39,40,41], visible=True, arg3=100, arg4=50, arg5=2)
        create_monster(spawnIds=[5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5121], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return FifthBattle01()


class FifthBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        set_interact_object(triggerIds=[10000780], state=1)
        set_effect(triggerIds=[73005], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000780], arg2=0):
            return FifthBridgeOn01()


class FifthBridgeOn01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        hide_guide_summary(entityId=20003382)
        set_effect(triggerIds=[73005], visible=False)
        set_mesh(triggerIds=[42,43,44,45,46,47,48], visible=True, arg3=100, arg4=50, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SixthBattle01()


class SixthBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        set_interact_object(triggerIds=[10000781], state=1)
        set_effect(triggerIds=[73006], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000781], arg2=0):
            return SixthBridgeOn01()


class SixthBridgeOn01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8009], visible=False)
        set_agent(triggerIds=[8010], visible=False)
        hide_guide_summary(entityId=20003382)
        set_effect(triggerIds=[73006], visible=False)
        set_mesh(triggerIds=[49,50,51,52,53,54,55], visible=True, arg3=100, arg4=50, arg5=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return SeventhBattle01()


class SeventhBattle01(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003382, textId=20003382)
        set_interact_object(triggerIds=[10000782], state=1)
        set_effect(triggerIds=[73007], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000782], arg2=0):
            return SeventhBridgeOn01()


#  보스 전투 돌입 
class SeventhBridgeOn01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8011], visible=False)
        set_agent(triggerIds=[8012], visible=False)
        set_agent(triggerIds=[8013], visible=False)
        set_agent(triggerIds=[8014], visible=False)
        set_agent(triggerIds=[8015], visible=False)
        hide_guide_summary(entityId=20003382)
        set_mesh(triggerIds=[56,57,58,59,60,61,62,63,64,65,66], visible=True, arg3=100, arg4=50, arg5=2)
        play_system_sound_in_box(boxIds=[102], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20003381, textId=20003381, duration=7000)
        set_effect(triggerIds=[73007], visible=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[5100]):
            return BossBattle01()


class BossBattle01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        dungeon_clear()
        set_mesh(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009], visible=True, arg3=200, arg4=50, arg5=2)
        set_mesh(triggerIds=[70010], visible=True, arg3=250, arg4=50, arg5=2)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return PCGetOut01()


class PCGetOut01(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return PCGetOut02()


class PCGetOut02(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return PCGetOut03()


class PCGetOut03(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return PCGetOut04()


class PCGetOut04(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


