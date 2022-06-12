using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000740: Pia
/// </summary>
public class _11000740 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407002877$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002881$
                // - Err? Are you a traveler? You look... cool. 
                return 40;
            case (40, 1):
                // $script:0831180407002882$
                // - I'm cooler, though. Hee hee!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
