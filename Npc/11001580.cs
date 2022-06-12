using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001580: Asimov
/// </summary>
public class _11001580 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006068$
    // - Welcome!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006122$
                // - This is not going to be easy. 
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
