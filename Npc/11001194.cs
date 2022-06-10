using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001194: Hicut
/// </summary>
public class _11001194 : NpcScript {
    internal _11001194(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016202007004188$ 
                // - Sigh...
                //   I want to go home...
                return true;
            case 30:
                // $script:1016202007004191$ 
                // - This is no good. I can't get a good shot!
                //   What should I do? 
                switch (selection) {
                    // $script:1016202007004192$
                    // - What's wrong?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1016202007004193$ 
                // - It's may be bright out here, but our cameras our set up inside that cave, where it's much darker. I doubt we can get any usable footage as it stands.
                //   I should've brought $npcName:11001193[gender:1]$, my supervisor... 
                return true;
            default:
                return true;
        }
    }
}
