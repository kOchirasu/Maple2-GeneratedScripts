using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000296: Jasper
/// </summary>
public class _11000296 : NpcScript {
    internal _11000296(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001177$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407001180$ 
                // - Oh! I's so happy to see another human being here!
                return true;
            default:
                return true;
        }
    }
}
