using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000804: Liam
/// </summary>
public class _11000804 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002962$
    // - Do you have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002965$
                // - $MyPCName$, never let your guard down. Not for an instant. You're a long way from Maple World.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
