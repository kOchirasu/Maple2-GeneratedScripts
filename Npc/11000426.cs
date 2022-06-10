using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000426: Senox
/// </summary>
public class _11000426 : NpcScript {
    internal _11000426(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001775$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407001778$ 
                // - What have I gotten myself into? I should never have followed $npcName:11000425[gender:0]$ here. What's going on? And why's it snowing?
                return true;
            default:
                return true;
        }
    }
}
