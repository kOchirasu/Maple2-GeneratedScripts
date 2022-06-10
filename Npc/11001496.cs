using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001496: Tara
/// </summary>
public class _11001496 : NpcScript {
    internal _11001496(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005820$ 
                // - I'm happy to be friends with such great people.
                return true;
            case 30:
                // $script:0118150907005823$ 
                // - I'm hoping I can relax. At least for today.
                return true;
            default:
                return true;
        }
    }
}
