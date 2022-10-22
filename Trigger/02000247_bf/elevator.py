""" trigger/02000247_bf/elevator.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073], enabled=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[401]):
            return 엘리베이터00()


class 엘리베이터00(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[402]):
            return 엘리베이터01()
        if not user_detected(boxIds=[999]):
            return 대기()


class 엘리베이터01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[403]):
            return 엘리베이터02()
        if not user_detected(boxIds=[999]):
            return 대기()


class 엘리베이터02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[404]):
            return 엘리베이터03()
        if not user_detected(boxIds=[401]):
            return 대기()
        if not user_detected(boxIds=[402]):
            return 대기()
        if not user_detected(boxIds=[403]):
            return 대기()
        if not user_detected(boxIds=[404]):
            return 대기()
        if not user_detected(boxIds=[999]):
            return 대기()


class 엘리베이터03(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=10)
        set_mesh(triggerIds=[301,302,303,304], visible=False)
        set_breakable(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1073], enabled=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()
        if not user_detected(boxIds=[999]):
            return 대기()


