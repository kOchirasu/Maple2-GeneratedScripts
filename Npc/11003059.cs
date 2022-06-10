using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003059: Ravole
/// </summary>
public class _11003059 : NpcScript {
    internal _11003059(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007626$ 
                // - It's nice to meet you!
                return true;
            case 30:
                // $script:0102155907007629$ 
                // - Nice to meet you, $MyPCName$! 
                switch (selection) {
                    // $script:0102155907007630$
                    // - Why did you come here?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0102155907007631$
                    // - What does the supply crew do around here?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0102155907007632$ 
                // - I came here with the supply crew, of course. We're here to keep the guards out here from turning into popsicles. But me... I'm here for another reason.
                switch (selection) {
                    // $script:0102155907007633$
                    // - So, why are you REALLY here?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0102155907007634$ 
                // - We keep the guards fed and clothed so they don't freeze or complain too much. Veterans like me handle supplies since we've learned what kind of gear we'll need. Honestly though, there's another reason I'm here.
                switch (selection) {
                    // $script:0102155907007635$
                    // - So, why are you REALLY here?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0102155907007636$ 
                // - I'm here to study a kingdom that once stood in this snowfield. It was a peaceful kingdom, but no one knows why it vanished into history. The survivors scattered, and none of them will talk to me, so I came here myself.
                // $script:0206154107007917$ 
                // - I've heard there's a shrine hidden somewhere in the snowfield kingdom. It was meant only for their kings and queens, to hold their most precious treasure. That means if I can get in there, I'll be rich! 
                // $script:0206154107007918$ 
                // - Hey, this is all completely grounded in fact! That's what my gut tells me, anyway. You look like you can handle a little adventure. If you come across the shrine, you gotta let me know!
                return true;
            default:
                return true;
        }
    }
}
