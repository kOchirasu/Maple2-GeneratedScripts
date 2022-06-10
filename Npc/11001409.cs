using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001409: Fubo
/// </summary>
public class _11001409 : NpcScript {
    internal _11001409(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005406$ 
                // - No exceptions. Not even for humans!
                return true;
            case 40:
                // $script:1222203907005486$ 
                // - You want to be strong, like the Meerkat Patrol? Then join our training!
                switch (selection) {
                    // $script:1222203907005487$
                    // - That sounds <i>adorable</i>. Sign me up!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005488$ 
                // - Don't underestimate us. If you cry and give up halfway through, you'll never live it down!
                switch (selection) {
                    // $script:1222203907005489$
                    // - I can handle anything you throw at me!
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1222203907005490$ 
                // - Heh... I'll see to it that you run away with your tail between your legs!
                return true;
            default:
                return true;
        }
    }
}
