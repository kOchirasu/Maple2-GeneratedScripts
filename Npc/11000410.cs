using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000410: Venus
/// </summary>
public class _11000410 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001731$
    // - $MyPCName$, nice to meet you!
    // $script:0831180407001732$
    // - I hope we can clean up this forest trail once more... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001733$
                // - This forest trail is the only path connecting us to $npcName:11000407[gender:0]$, and the monsters are making it unusable. $npcName:11000409[gender:0]$ and I are working to clear them out.
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
