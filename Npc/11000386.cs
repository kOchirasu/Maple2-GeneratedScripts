using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000386: Hurum
/// </summary>
public class _11000386 : NpcScript {
    internal _11000386(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001571$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407001573$ 
                // - Hello. I am $npcName:11000386$. You seem surprised that I can talk. Don't be. Maple World is full of surprises after all. 
                return true;
            default:
                return true;
        }
    }
}
