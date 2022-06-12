using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003091: Orde
/// </summary>
public class _11003091 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007936$
    // - $MyPCName$, you're here!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007937$
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
