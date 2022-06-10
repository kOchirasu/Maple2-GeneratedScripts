using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000514: Belma
/// </summary>
public class _11000514 : NpcScript {
    internal _11000514(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002195$ 
                // - What brings you here? 
                return true;
            case 40:
                // $script:0831180407002199$ 
                // - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins. 
                switch (selection) {
                    // $script:0831180407002200$
                    // - I'm here to make amends for my deeds.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002201$
                    // - I'm just a tourist!
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002202$ 
                // - All misdeeds must be punished. The punishment must fit the crime, or else we risk the criminal committing their crimes again. 
                switch (selection) {
                    // $script:0831180407002203$
                    // - How can I reduce my sentence?
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407002207$ 
                // - See the prisoners in here? Remember that you can always end up the same if you fail to heed the law. 
                // $script:0831180407002208$ 
                // - And that's the reason I have a tourist program here. You could learn a thing or two. 
                return true;
            case 43:
                // $script:0831180407002204$ 
                // - How bold! You realize I don't issue pardons... 
                switch (selection) {
                    // $script:0831180407002205$
                    // - I'll do anything. ANYTHING.
                    case 0:
                        Id = 44;
                        return false;
                }
                return true;
            case 44:
                // $script:0831180407002206$ 
                // - Will you, now? Hmm... I like the sound of that. In some cases, hard labor can substitute for time served. How about you pull the weeds in the prison yard? Do a good job, and I'll consider reducing your sentence. 
                return true;
            case 50:
                // $script:1210061907004881$ 
                // - Maybe you don't realize this, but I'm the warden of this prison. I don't take walk-ins. 
                switch (selection) {
                    // $script:1210061907004882$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004883$ 
                // - Who? You can't expect me to remember every rodent who comes in and out of $map:2000124$. 
                switch (selection) {
                    // $script:1210061907004884$
                    // - Trust me, you'd remember this guy.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1210061907004885$ 
                // - <font color="#909090">(She listens begrudgingly as you describe $npcName:11001231[gender:0]$.)</font>
As a matter of fact, I do remember him. There was something mysterious about the man. 
                switch (selection) {
                    // $script:1210061907004886$
                    // - Do you know why he was here?
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1210061907004887$ 
                // - Only two kinds of people come to $map:2000124$: tourists and convicts. Since he's not rotting in one of our cells, I suppose he must have been a tourist. 
                return true;
            default:
                return true;
        }
    }
}
