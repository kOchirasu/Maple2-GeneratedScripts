using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001575: Landevian
/// </summary>
public class _11001575 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0504151707006063$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006117$
                // - I'll be back on my feet... before you know it... 
                return -1;
            case (20, 0):
                // $script:0524142307006214$
                // - Don't worry about me... I'll be back on my feet in no time... 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
