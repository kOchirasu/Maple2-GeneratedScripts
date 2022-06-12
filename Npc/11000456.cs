using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000456: Geno
/// </summary>
public class _11000456 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002018$
    // - I love staying around the house.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002021$
                // - My girlfriend keeps bugging me to go out, even though it's a great day to relax inside. You get that, right? Make her see reason. If she always insists on doing... things, I worry about our future.
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
