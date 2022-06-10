using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001497: Tara
/// </summary>
public class _11001497 : NpcScript {
    internal _11001497(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005824$ 
                // - I'm happy to be friends with such great people. 
                return true;
            case 30:
                // $script:0118150907005827$ 
                // - I'm hoping I can relax. At least for today. 
                return true;
            default:
                return true;
        }
    }
}
