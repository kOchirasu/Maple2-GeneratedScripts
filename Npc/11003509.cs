using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003509: Troe
/// </summary>
public class _11003509 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0816160115009014$
    // - Ah... Hello...?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009015$
                // - Ah... Hello...? I want to make some monster friends...
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
