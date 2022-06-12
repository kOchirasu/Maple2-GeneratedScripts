using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000251: Wei Hong
/// </summary>
public class _11000251 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001049$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001051$
                // - My organization is using $map:02000216$ as a foothold to expand its business to other areas. You didn't think we'd stay in the shadows forever, did you? Don't be ridiculous.  
                return -1;
            case (30, 0):
                // $script:0831180407001052$
                // - ...Get lost.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
