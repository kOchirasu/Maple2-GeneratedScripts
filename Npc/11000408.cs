using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000408: Mr. Grippa
/// </summary>
public class _11000408 : NpcScript {
    internal _11000408(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001723$ 
                // - Ah-choo! Aww. What is it?
                return true;
            case 10:
                // $script:0831180407001724$ 
                // - Ah-choo! I hate... pollen... ah-choo! It's terrib... ah-choo!
                return true;
            case 20:
                // $script:0831180407001725$ 
                // - Please... I need to stop... ah-choo! I need to stop sneezing... Bring me $item:30000125$... ah-choo! The wildflowers over there. Sniff... You can pick up $item:30000125$ with the Z key.
                return true;
            default:
                return true;
        }
    }
}
