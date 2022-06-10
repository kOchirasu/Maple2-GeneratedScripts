using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001945: Clarinet Student
/// </summary>
public class _11001945 : NpcScript {
    internal _11001945(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007491$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007533$ 
                // - Toot too-toot!
                //   <font color="#909090">(He mumbles something into his clarinet.)</font>
                return true;
            default:
                return true;
        }
    }
}
