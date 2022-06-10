using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000833: Alponi
/// </summary>
public class _11000833 : NpcScript {
    internal _11000833(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003047$ 
                // - Hello.
                return true;
            case 30:
                // $script:0831180407003050$ 
                // - Ooh, I hate wolves more than anything. They chew up our fences and take our sheep. I wish I could just move away... me and the sheep... 
                return true;
            default:
                return true;
        }
    }
}
