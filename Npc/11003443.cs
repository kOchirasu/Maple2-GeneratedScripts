using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003443: Kaitlyn
/// </summary>
public class _11003443 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0721140007008691$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0721142007008709$
                // - What?
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
