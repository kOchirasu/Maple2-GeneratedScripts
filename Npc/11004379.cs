using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004379: Maximilian
/// </summary>
public class _11004379 : NpcScript {
    internal _11004379(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011793$ 
                // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
                return true;
            case 10:
                // $script:1109213607011794$ 
                // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
                return true;
            case 40:
                // $script:1120173007011868$ 
                // - I'll be honest, I didn't think this place was so merry until <i>you</i> showed up.
                switch (selection) {
                    // $script:1120173007011869$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1120173007011870$ 
                // - $npcName:11004345[gender:1]$? That's $npcName:11004347[gender:1]$'s daughter. She's my boss, but she's off today. You sure she's not at home?
                return true;
            default:
                return true;
        }
    }
}
