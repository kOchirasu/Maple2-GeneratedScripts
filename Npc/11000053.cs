using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000053: Luen
/// </summary>
public class _11000053 : NpcScript {
    internal _11000053(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000227$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000230$ 
                // - $MyPCName$! Are you here to make some money? The court festival must be great for business. Everywhere I look, folks are out doing something for it. 
                return true;
            case 40:
                // $script:0831180407000231$ 
                // - The priciest thing to come out of all this is $itemPlural:20000013$, and you can only get them from Turtle Hill, where $npcName:22300149$ is. 
                return true;
            default:
                return true;
        }
    }
}
