using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003334: Ralph
/// </summary>
public class _11003334 : NpcScript {
    internal _11003334(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0426090007008448$ 
                // - Who's behind this mess?
                return true;
            case 30:
                // $script:0426090007008451$ 
                // - You! What are <i>you</i> doing here?!
                switch (selection) {
                    // $script:0426090007008452$
                    // - Good to see you, too.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0426090007008453$ 
                // - I gave you what you wanted. Why are you bugging me?
                switch (selection) {
                    // $script:0426090007008454$
                    // - Did a blond man run through here?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0426090007008455$ 
                // - Yeah. He was headed for $map:02000138$. Now leave me alone!
                switch (selection) {
                    // $script:0426090007008456$
                    // - I'll see you later.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0426090007008457$ 
                // - Why would I ever want to see you again?!
                return true;
            default:
                return true;
        }
    }
}
