using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000414: Carrela
/// </summary>
public class _11000414 : NpcScript {
    internal _11000414(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000158$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000831$ 
                // - Spooky houses are kind of charming, really.
                return true;
            case 20:
                // $script:1121222006000832$ 
                // - How would you like to create a haunted house?
                return true;
            default:
                return true;
        }
    }
}
