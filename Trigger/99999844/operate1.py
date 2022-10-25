""" trigger/99999844/operate1.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002122], stateValue=0):
            return 기믹공간(self.ctx)


class 기믹공간(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002123], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002123], stateValue=0):
            self.set_mesh(triggerIds=[1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118], visible=False, arg3=0, delay=0, scale=0)
            self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,1263,1264,1265,1266], visible=False, arg3=0, delay=0, scale=0)
            return 리젠대기(self.ctx)


class 리젠대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 레버작동(self.ctx)


class 레버작동(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048], visible=True, arg3=0, delay=40, scale=3)
        self.set_mesh(triggerIds=[1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118], visible=True, arg3=0, delay=60, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 기믹시작(self.ctx)


class 기믹시작(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1201,1202,1203,1204,1205,1206,1207,1208,1209,1210,1211,1212,1213,1214,1215,1216,1217,1218,1219,1220,1221,1222,1223,1224,1225,1226,1227,1228,1229,1230,1231,1232,1233,1234,1235,1236,1237,1238,1239,1240,1241,1242,1243,1244,1245,1246,1247,1248,1249,1250,1251,1252,1253,1254,1255,1256,1257,1258,1259,1260,1261,1262,1263,1264,1265,1266], visible=True, arg3=0, delay=20, scale=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 기믹공간(self.ctx)


initial_state = 대기
