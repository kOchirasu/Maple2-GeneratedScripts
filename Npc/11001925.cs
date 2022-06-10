using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001925: Fisher
/// </summary>
public class _11001925 : NpcScript {
    internal _11001925(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121140707007426$ 
                // - I caught a prize fish!
                return true;
            case 30:
                // $script:1121184207007439$ 
                // - I coated my hook with chocolate. Who doesn't like chocolate?
                return true;
            default:
                return true;
        }
    }
}
