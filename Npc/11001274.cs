using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001274: Madares
/// </summary>
public class _11001274 : NpcScript {
    internal _11001274(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1207123607004816$ 
                // - Barabung! Chochakka!
                return true;
            case 30:
                // $script:1207123607004819$ 
                // - Won't do it.
                switch (selection) {
                    // $script:1207123607004820$
                    // - What won't you do?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1207123607004821$ 
                // - No talk. Stranger danger.
                switch (selection) {
                    // $script:1207123607004822$
                    // - I'm not a stranger. I'm $MyPCName$.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1207123607004823$ 
                // - $MyPCName$ stranger! No talk.
                return true;
            default:
                return true;
        }
    }
}
