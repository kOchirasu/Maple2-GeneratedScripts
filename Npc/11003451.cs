using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003451: Namid
/// </summary>
public class _11003451 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008657$
    // - Who will protect $map:02000051$?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008658$
                // - Who will protect $map:02000051$?
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
