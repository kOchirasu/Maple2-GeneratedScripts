using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001060: Blanche
/// </summary>
public class _11001060 : NpcScript {
    protected override int First() {
        return 60;
    }

    // Select 0:
    // $script:0831180306000373$
    // - Do you have business with me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0831180306000376$
                // - I don't think I'll do business with you, $MyPCName$. I prefer to work with those who have $achieve:23200015$ Trophies. I apologize for any inconvenience.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
