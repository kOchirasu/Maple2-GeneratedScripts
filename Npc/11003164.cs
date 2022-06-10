using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003164: Joddy
/// </summary>
public class _11003164 : NpcScript {
    internal _11003164(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0310134607008081$ 
                // - Whew! That was a close one.
                return true;
            case 30:
                // $script:0310134607008084$ 
                // - You really pulled me out of the fire.
                switch (selection) {
                    // $script:0310134607008085$
                    // - What are you talking about?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0310134607008086$
                    // - You're welcome, I guess?
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0310134607008087$ 
                // - You drove off that big, bad doggy! If it weren't for you... Jeez, I'd really be in a pickle.
                switch (selection) {
                    // $script:0310134607008088$
                    // - You... do know how to fight, don't you?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0310134607008089$ 
                // - Sure do! I even fought a rogue $npcName:21000001$ once! I mean, I lost, but I sure gave it my best!
                // $script:0310134607008090$ 
                // - Aw, jeez. I don't know about that look you're giving me...
                return true;
            case 33:
                // $script:0310134607008091$ 
                // - You really know a thing or two about being a hero, don't you? Wow!
                switch (selection) {
                    // $script:0310134607008092$
                    // - A hero...?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0310134607008093$ 
                // - Yeah, a real, live hero! One day I'll be just like you. Just you wait!
                return true;
            default:
                return true;
        }
    }
}
