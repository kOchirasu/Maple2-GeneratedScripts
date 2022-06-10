using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001239: Daon
/// </summary>
public class _11001239 : NpcScript {
    internal _11001239(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123154807004442$ 
                // - Bah! What do I do? 
                return true;
            case 30:
                // $script:1123154807004445$ 
                // - The grownups said not to leave the forest. But why not? What's out there? I gotta know! 
                switch (selection) {
                    // $script:1123154807004446$
                    // - You should listen to the grownups, kid.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1123154807004447$ 
                // - But they never let me do anything fun! I bet there's all kinds of toys and games beyond the forest, and the grownups are keeping it all to themselves! 
                switch (selection) {
                    // $script:1123154807004448$
                    // - Yeah, that's not it.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1123154807004449$ 
                // - Then maybe there's... there's just groves and groves of sweet fruit! There's got to be <i>something</i> out there! And I wanna see it! 
                return true;
            default:
                return true;
        }
    }
}
