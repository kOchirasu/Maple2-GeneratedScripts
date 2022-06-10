using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000404: Snowy
/// </summary>
public class _11000404 : NpcScript {
    internal _11000404(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001634$ 
                // - May I help you? 
                return true;
            case 40:
                // $script:0831180407001638$ 
                // - $npcName:23000024[gender:1]$ carries a dark power. Try not to get poisoned. 
                return true;
            case 60:
                // $script:0831180407001639$ 
                // - Some folks think I must be a blacksmith. But not all yetis are smiths, you know! So stop trying to buy my stuff. 
                return true;
            default:
                return true;
        }
    }
}
