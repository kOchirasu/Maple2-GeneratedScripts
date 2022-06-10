using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003160: Mindy
/// </summary>
public class _11003160 : NpcScript {
    internal _11003160(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008063$ 
                // - Oh, hello.
                return true;
            case 30:
                // $script:0306155707008066$ 
                // - I don't think anyone hates flowers, right? Everyone has to have a favorite flower or two.
                return true;
            default:
                return true;
        }
    }
}
