using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004267: Sunny
/// </summary>
public class _11004267 : NpcScript {
    internal _11004267(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011217$ 
                // - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
                return true;
            case 10:
                // $script:0911203207011218$ 
                // - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
                switch (selection) {
                    // $script:0911203207011219$
                    // - When is this place gonna open?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011220$ 
                // - That's what I wanna know, too! I heard there's some kinda bug problem holding up the construction...
                // $script:0911203207011221$ 
                // - But honestly, they tell me I have the job, so shouldn't they open so I can start working? I already spent a fortune promoting myself... Anyway, remember my name, and watch as I become the best model in all Karkar!
                return true;
            default:
                return true;
        }
    }
}
