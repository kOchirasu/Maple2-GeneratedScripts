using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001476: Wei Hong
/// </summary>
public class _11001476 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1228113207005714$
    // - Betrayal is the quickest path to death.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1228113207005716$
                // - You're better than I thought. I never forget a debt... or a grudge. $MyPCName$...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
