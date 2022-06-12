using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003137: Orde
/// </summary>
public class _11003137 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0208220907007947$
    // - $MyPCName$, you're here!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0208220907007948$
                // - I've learned so much about the world thanks to you, $MyPCName$. Thank you so much.
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
