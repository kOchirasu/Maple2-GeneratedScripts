using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000036: Arita
/// </summary>
public class _11000036 : NpcScript {
    internal _11000036(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000196$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000199$ 
                // - Love the flowers and trees as you love yourself. Without them, you wouldn't exist. 
                return true;
            default:
                return true;
        }
    }
}
