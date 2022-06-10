using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001663: Ereve
/// </summary>
public class _11001663 : NpcScript {
    internal _11001663(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617211107006373$ 
                // - Welcome, $MyPCName$.
                return true;
            case 10:
                // $script:0617211107006374$ 
                // - You've grown strong, my hero. I look forward to hearing more great tales of your exploits.
                return true;
            case 20:
                // $script:0426085907008441$ 
                // - We hope our faith in you is well deserved.
                return true;
            default:
                return true;
        }
    }
}
