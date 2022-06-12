using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001380: Balba
/// </summary>
public class _11001380 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005377$
    // - Mm? What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005380$
                // - Who are these guys? Get them out of here! The match would already be over by now if they didn't ruin everything!
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
