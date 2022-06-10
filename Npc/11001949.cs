using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001949: Mochar
/// </summary>
public class _11001949 : NpcScript {
    internal _11001949(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007495$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1208184307007545$ 
                // - But I don't <i>want</i> to be a musician! 
                return true;
            default:
                return true;
        }
    }
}
