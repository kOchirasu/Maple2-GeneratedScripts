using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000179: Albert
/// </summary>
public class _11000179 : NpcScript {
    internal _11000179(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;70
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000738$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000741$ 
                // - $MyPCName$, huh? You have a very... fitting name. 
                return true;
            case 70:
                // $script:0831180407000742$ 
                // - Ah, we meet again. Thank you for taking care of things last time. I was able to score the contract thanks to you! 
                return true;
            default:
                return true;
        }
    }
}
