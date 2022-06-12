using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003083: Celine
/// </summary>
public class _11003083 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0113143107007770$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0113143107007771$
                // - $MyPCName$, I'm sorry you came all the way here for nothing.
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
