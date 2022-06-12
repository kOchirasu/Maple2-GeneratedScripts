using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004459: Farennis
/// </summary>
public class _11004459 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:1227192907012056$
    // - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012057$
                // - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
                return 10;
            case (10, 1):
                // $script:1227192907012058$
                // - We could never have put a base like this together so quickly without Sky Fortress.
                switch (selection) {
                    // $script:1227192907012059$
                    // - How did you manage this, anyway?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1227192907012060$
                // - As soon as this mission began, Cat Sith started sending me data on the base's construction plans and materials.
                return 20;
            case (20, 1):
                // $script:1227192907012061$
                // - I'm happy to report that not a single brick went to waste in constructing this place!
                switch (selection) {
                    // $script:1227192907012062$
                    // - What's Cat Sith?
                    case 0:
                        return 21;
                    // $script:1227192907012063$
                    // - What does Cat Sith mean?
                    case 1:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:1227192907012064$
                // - I'm surprised you haven't been briefed. It's the new shipboard AI. It's able to scour data from the Sky Fortress's memory banks and learn on its own.
                return 21;
            case (21, 1):
                // $script:1227192907012065$
                // - The captain came up with the AI design and the tactical officer did all of the programming. I admit, I'm a little intimidated by their genius.
                switch (selection) {
                    // $script:0114160707012701$
                    // - Amazing.
                    case 0:
                        return 23;
                }
                return -1;
            case (22, 0):
                // $script:1227192907012066$
                // - You'd have to ask the captain, since she's the one who named it. I imagine it has something to do with cats. Just a hunch.
                return -1;
            case (23, 0):
                // $script:0114160707012702$
                // - Of course it is. Why, it's astonishing, even!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.SelectableDistractor,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
