using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000442: Cathy Mart Employee
/// </summary>
public class _11000442 : NpcScript {
    internal _11000442(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001859$ 
                // - Can I help you? 
                return true;
            case 20:
                // $script:0831180407001861$ 
                // - I don't want to talk. I got ripped off by my boss, and then I almost got killed by robbers. My life sucks! 
                return true;
            case 30:
                // $script:0831180407001862$ 
                // - Do you want to know what the owner of Cathy Mart is like? The worst, that's what!  
                return true;
            default:
                return true;
        }
    }
}
