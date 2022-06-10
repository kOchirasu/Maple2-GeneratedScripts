using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000282: Besherel
/// </summary>
public class _11000282 : NpcScript {
    internal _11000282(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001098$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407001101$ 
                // - If you want something, then you'll have to pay the price.That's the way of the world. 
                return true;
            default:
                return true;
        }
    }
}
