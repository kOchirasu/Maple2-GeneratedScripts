using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004335: Brighton
/// </summary>
public class _11004335 : NpcScript {
    internal _11004335(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011590$ 
                // - Now, isn't this something?
                return true;
            case 10:
                // $script:1010140307011591$ 
                // - I've gotta admit, I'm impressed.
                // $script:1010140307011592$ 
                // - This whole place is, like, the opposite of Maple World. No wonder the boss was so eager to check it out.
                // $script:1010140307011593$ 
                // - I didn't believe a word of it, of course. But $npcName:11004334[gender:1]$ insisted, and... Wow. Just wow.
                // $script:1010140307011594$ 
                // - $npcName:11003191[gender:0]$ doesn't know what he's missing!
                return true;
            default:
                return true;
        }
    }
}
