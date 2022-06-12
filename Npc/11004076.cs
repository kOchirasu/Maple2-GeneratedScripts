using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004076: Yellow Butterfly
/// </summary>
public class _11004076 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010213$
    // - Look at that dumb wormy-worm!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010214$
                // - Look at that dumb wormy-worm!
                return 10;
            case (10, 1):
                // $script:0619202207010215$
                // - You see that fat little bug over there? Do <i>you</i> think he can become a butterfly?
                switch (selection) {
                    // $script:0619202207010216$
                    // - That's correct.
                    case 0:
                        return 40;
                    // $script:0619202207010217$
                    // - No.
                    case 1:
                        return 41;
                }
                return -1;
            case (40, 0):
                // $script:0619202207010218$
                // - Pssh! You think that's how a real caterpillar looks? You must have a tiny brain.
                return -1;
            case (41, 0):
                // $script:0619202207010219$
                // - Yeah, exactly. Yet that poor creature actually think it's gonna be a butterfly. Can you believe that?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
