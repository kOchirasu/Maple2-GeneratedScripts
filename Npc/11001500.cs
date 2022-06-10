using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001500: Dunba
/// </summary>
public class _11001500 : NpcScript {
    internal _11001500(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005836$ 
                // - What do I want to eat this time?
                return true;
            case 30:
                // $script:0118150907005839$ 
                // - Could you stop bothering me? I'm eating!
                return true;
            default:
                return true;
        }
    }
}
