using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001576: Eupheria
/// </summary>
public class _11001576 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0504151707006064$
    // - Don't worry too much. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006118$
                // - I think everyone... will be all right... 
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
