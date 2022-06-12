using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001596: Landevian
/// </summary>
public class _11001596 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0504151707006084$
    // - Sigh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006133$
                // - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
                return -1;
            case (20, 0):
                // $script:0524142307006222$
                // - This isn't like $npcName:11001229[gender:0]$ at all. Wake up!
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
