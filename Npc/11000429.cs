using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000429: Remy
/// </summary>
public class _11000429 : NpcScript {
    internal _11000429(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;41
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001785$ 
                // - Ah, the smell of the sea!
                return true;
            case 30:
                // $script:0831180407001787$ 
                // - I just ate lunch, and I'm already hungry. 
                return true;
            case 40:
                // $script:0831180407001788$ 
                // - Mm? Do I know you?
                switch (selection) {
                    // $script:0831180407001789$
                    // - Come try $npcName:11000362[gender:0]$'s $itemPlural:30000140$!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001790$ 
                // - $itemPlural:30000140$? That sounds delicious! I'll be back for those.
                return true;
            default:
                return true;
        }
    }
}
