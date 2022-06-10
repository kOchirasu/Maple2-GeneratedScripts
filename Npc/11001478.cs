using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001478: Ereve
/// </summary>
public class _11001478 : NpcScript {
    internal _11001478(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005759$ 
                // - $MyPCName$, what brings you to me? 
                return true;
            case 30:
                // $script:0106111607005762$ 
                // - This $map:52010007$ has opened by the power of the Lumenstone in the Sanctuary of Light, somewhere in Nazkar Temple. 
                switch (selection) {
                    // $script:0106111607005763$
                    // - What should I do now?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0106111607005764$ 
                // - There's only one thing to do. You must retrieve the Lumenstone before its chaotic light is consumed by darkness. 
                return true;
            default:
                return true;
        }
    }
}
