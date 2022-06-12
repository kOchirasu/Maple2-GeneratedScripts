using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004514: Mannstad Quartermaster
/// </summary>
public class _11004514 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1228182607012472$
    // - We'll be eating shoe leather at this rate...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1228182607012473$
                // - We'll be eating shoe leather at this rate...
                return 10;
            case (10, 1):
                // $script:1228182607012474$
                // - With all the land routes cut off, we've been relying on air drops for supplies. We don't have the spare planes to keep that up forever, though. If something doesn't happen soon, the fortress will fall.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
