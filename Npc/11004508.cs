using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004508: Mannstad Sentry
/// </summary>
public class _11004508 : NpcScript {
    internal _11004508(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012446$ 
                // - Zzz... N-no... I can't eat another bite...
                return true;
            case 10:
                // $script:1228182607012447$ 
                // - Zzz... N-no... I can't eat another bite...
                switch (selection) {
                    // $script:1228182607012448$
                    // - <b>Hello there!</b>
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1228182607012449$ 
                // - <b>Aaaah!</b> Don't hurt me! I-I mean... I'm awake. I'm awake!
                return true;
            default:
                return true;
        }
    }
}
