using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004072: Suspicious Tree
/// </summary>
public class _11004072 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010170$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010171$
                // - ...
                return 10;
            case (10, 1):
                // $script:0619202207010172$
                // - ...
                switch (selection) {
                    // $script:0619202207010173$
                    // - ...
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0619202207010174$
                // - ...
                switch (selection) {
                    // $script:0619202207010175$
                    // - ...
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0619202207010176$
                // - ...
                switch (selection) {
                    // $script:0619202207010177$
                    // - Huh. I didn't know trees could scream.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0619202207010178$
                // - Well obviously I'm not a tree! How did you even spot me? I'm here on a secret mission!
                switch (selection) {
                    // $script:0619202207010179$
                    // - You one of Frey's men?
                    case 0:
                        return 40;
                    // $script:0619202207010180$
                    // - Did the empress send you?
                    case 1:
                        return 50;
                    // $script:0619202207010181$
                    // - Liar.
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0619202207010182$
                // - I'm trying to keep a low profile here. Can't you pretend you didn't see me and just move along?
                return -1;
            case (50, 0):
                // $script:0619202207010183$
                // - You aren't worthy to even speak of her!
                return -1;
            case (60, 0):
                // $script:0619202207010184$
                // - Stop blathering. I'm on duty. Get out of here now, before you regret it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
