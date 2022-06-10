using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001066: Treno
/// </summary>
public class _11001066 : NpcScript {
    internal _11001066(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003630$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407003633$ 
                // - Waiting for the $map:02000184$ tour train? We're sorry, but it won't be operating for a while. 
                return true;
            default:
                return true;
        }
    }
}
