using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004380: Rufina
/// </summary>
public class _11004380 : NpcScript {
    internal _11004380(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011795$ 
                // - You won't know love if you don't express it. Confess your love to your crush for the holidays! It's the perfect gift! 
                return true;
            case 10:
                // $script:1109213607011796$ 
                // - The holidays are all about looooove. 
                switch (selection) {
                    // $script:1109213607011797$
                    // - ...
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109213607011798$ 
                // - I have a pair of skates I really love... so much so that I don't want to take them out of the box. 
                switch (selection) {
                    // $script:1109213607011799$
                    // - You skate with them still inside the box? Sounds kind of dangerous.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109213607011800$ 
                // - No way! I've never even worn them! I wonder what it'd be like to skate with them... Maybe that's what love is, taking risks. 
                return true;
            case 40:
                // $script:1120173007011871$ 
                // - The holidays are all about looooove. 
                switch (selection) {
                    // $script:1120173007011872$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1120173007011873$ 
                // - I know $npcName:11004348[gender:0]$, he's $npcName:11004345[gender:1]$'s father. I saw him last night at the gardening club meeting. But I didn't see him today. I bet he's just at home... He mentioned wanting to decorate his holiday tree. 
                return true;
            default:
                return true;
        }
    }
}
