using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001969: Ereve
/// </summary>
public class _11001969 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0201161807007915$
    // - Welcome, $MyPCName$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0201161807007916$
                // - $MyPCName$, I'm looking forward to hearing more great stories of your heroism.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
