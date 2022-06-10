using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001407: Mian
/// </summary>
public class _11001407 : NpcScript {
    internal _11001407(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005404$ 
                // - ...
                return true;
            case 40:
                // $script:1230100207005748$ 
                // - ...
                switch (selection) {
                    // $script:1230100907005749$
                    // - What's with the quiet act?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1230100907005750$ 
                // - <font color="#909090">($npcName:11001407[gender:0]$ stares at you without saying a word.)</font>
                return true;
            default:
                return true;
        }
    }
}
