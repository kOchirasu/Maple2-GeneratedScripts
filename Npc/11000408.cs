using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000408: Mr. Grippa
/// </summary>
public class _11000408 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407001723$
    // - Ah-choo! Aww. What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001724$
                // - Ah-choo! I hate... pollen... ah-choo! It's terrib... ah-choo!
                return -1;
            case (20, 0):
                // $script:0831180407001725$
                // - Please... I need to stop... ah-choo! I need to stop sneezing... Bring me $item:30000125$... ah-choo! The wildflowers over there. Sniff... You can pick up $item:30000125$ with the Z key.
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
