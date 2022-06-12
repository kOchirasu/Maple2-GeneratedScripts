using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004363: Aiden
/// </summary>
public class _11004363 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011775$
    // - So much commotion here... What's the big deal about a tree and some presents? Chill already!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011776$
                // - What's so exciting about snow? It's just ice crystals. Nobody gets excited about an ice machine.
                return 10;
            case (10, 1):
                // $script:1120223207011901$
                // - ...Though I admit, it's kinda pretty out here.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
