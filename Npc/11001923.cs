using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001923: Fisher
/// </summary>
public class _11001923 : NpcScript {
    internal _11001923(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121140707007424$ 
                // - I caught a prize fish!
                return true;
            case 30:
                // $script:1121184207007433$ 
                // - Hey! Find your own spot!
                return true;
            default:
                return true;
        }
    }
}
