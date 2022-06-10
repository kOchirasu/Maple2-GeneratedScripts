using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001922: Fisher
/// </summary>
public class _11001922 : NpcScript {
    internal _11001922(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121140707007423$ 
                // - I caught a prize fish! 
                return true;
            case 30:
                // $script:1121184207007430$ 
                // - Do you mind? I'm trying to enjoy some "me" time. 
                return true;
            default:
                return true;
        }
    }
}
