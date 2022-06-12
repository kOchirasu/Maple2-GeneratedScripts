using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000644: Prisoner 160917
/// </summary>
public class _11000644 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002629$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002632$
                // - Ah... I'm bored...
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
