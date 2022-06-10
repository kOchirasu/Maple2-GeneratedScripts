using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001055: Sansakova
/// </summary>
public class _11001055 : NpcScript {
    internal _11001055(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003606$ 
                // - Welcome.
                return true;
            case 30:
                // $script:0831180407003607$ 
                // - No pizza can match Maggiore pizza. Chewy dough with simple toppings, just like Mom used to make! 
                return true;
            default:
                return true;
        }
    }
}
