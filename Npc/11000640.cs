using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000640: Prisoner 150122
/// </summary>
public class _11000640 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407002608$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002612$
                // - Argh, this place is a sty! I hate prison! 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
