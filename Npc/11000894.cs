using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000894: Aina
/// </summary>
public class _11000894 : NpcScript {
    internal _11000894(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003264$ 
                // - Everyone, wake up! We need to be alert.
                return true;
            case 20:
                // $script:0831180407003265$ 
                // - May the winds bring you comfort.
                return true;
            default:
                return true;
        }
    }
}
