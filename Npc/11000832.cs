using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000832: Whitingale
/// </summary>
public class _11000832 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003044$
    // - Whew, I wish I had more hands.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003046$
                // - There's no better medicine than hope. Stop being a crybaby and come over here.
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
