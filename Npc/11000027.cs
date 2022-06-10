using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000027: Corni
/// </summary>
public class _11000027 : NpcScript {
    internal _11000027(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000175$ 
                // - Yes? Yes? What do you need? How can I help? 
                return true;
            case 20:
                // $script:0831180407000177$ 
                // - I messed up. I messed it all up. Woe is meee! 
                return true;
            default:
                return true;
        }
    }
}
