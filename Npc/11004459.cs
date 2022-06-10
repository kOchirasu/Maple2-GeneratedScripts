using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004459: Farennis
/// </summary>
public class _11004459 : NpcScript {
    internal _11004459(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012056$ 
                // - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
                return true;
            case 10:
                // $script:1227192907012057$ 
                // - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
                // $script:1227192907012058$ 
                // - We could never have put a base like this together so quickly without Sky Fortress.
                switch (selection) {
                    // $script:1227192907012059$
                    // - How did you manage this, anyway?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1227192907012060$ 
                // - As soon as this mission began, Cat Sith started sending me data on the base's construction plans and materials.
                // $script:1227192907012061$ 
                // - I'm happy to report that not a single brick went to waste in constructing this place!
                switch (selection) {
                    // $script:1227192907012062$
                    // - What's Cat Sith?
                    case 0:
                        Id = 21;
                        return false;
                    // $script:1227192907012063$
                    // - What does Cat Sith mean?
                    case 1:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:1227192907012064$ 
                // - I'm surprised you haven't been briefed. It's the new shipboard AI. It's able to scour data from the Sky Fortress's memory banks and learn on its own.
                // $script:1227192907012065$ 
                // - The captain came up with the AI design and the tactical officer did all of the programming. I admit, I'm a little intimidated by their genius.
                switch (selection) {
                    // $script:0114160707012701$
                    // - Amazing.
                    case 0:
                        Id = 23;
                        return false;
                }
                return true;
            case 22:
                // $script:1227192907012066$ 
                // - You'd have to ask the captain, since she's the one who named it. I imagine it has something to do with cats. Just a hunch.
                return true;
            case 23:
                // $script:0114160707012702$ 
                // - Of course it is. Why, it's astonishing, even!
                return true;
            default:
                return true;
        }
    }
}
