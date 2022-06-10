using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000056: Leonard
/// </summary>
public class _11000056 : NpcScript {
    internal _11000056(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000241$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000244$ 
                // - Hmph, the oarsman at $map:63000002$ is so greedy. He charges a huge fee just to take you to $map:02000062$. Isn't that crazy?
                switch (selection) {
                    // $script:0831180407000245$
                    // - It really is.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000246$
                    // - I don't know.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000247$ 
                // - Seriously! Some people stay in $map:63000002$ for ages just to make enough money to get on his boat!
                switch (selection) {
                    // $script:0831180407000248$
                    // - What do people do to make money?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000251$ 
                // - Really? Well, I guess the fare would be nothing if I could win $npcName:11000441[gender:0]$'s prize money.
                switch (selection) {
                    // $script:0831180407000252$
                    // - Wait, what's this about $npc:11000441[gender:0]$'s prize money?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407000249$ 
                // - Oh, they hunt monsters or pick up junk that washes up on the shore. Some of it is pretty valuable.
                // $script:0831180407000250$ 
                // - But I'll never go there. I don't want to be trampled by $npcName:22300149$ before I get to the mainland.
                return true;
            case 34:
                // $script:0831180407000253$ 
                // - I told you. Enter $map:61000005$ behind me and survive until the end, and $npc:11000441[gender:0]$ will shower you with money.
                return true;
            default:
                return true;
        }
    }
}
