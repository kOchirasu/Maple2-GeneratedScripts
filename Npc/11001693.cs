using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001693: Zabeth
/// </summary>
public class _11001693 : NpcScript {
    internal _11001693(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629205207006508$ 
                // - If you got something to say, say it.
                return true;
            case 30:
                // $script:0629205207006510$ 
                // - I don't care what $npcName:11001631[gender:0]$ says. I call the shots around here, and don't you forget it.
                // $script:0630212007006534$ 
                // - Remember, that guy's all talk and no action. I can beat him with one hand tied behind my back.
                return true;
            default:
                return true;
        }
    }
}
