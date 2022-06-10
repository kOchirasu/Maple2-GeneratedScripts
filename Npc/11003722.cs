using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003722: 
/// </summary>
public class _11003722 : NpcScript {
    internal _11003722(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1127164207009322$ 
                // - Good to see you.  
                return true;
            case 10:
                // $script:1127164207009323$ 
                // - Hi there, $MyPCName$. I'm Zakum, but little. You can call me Little Zakum. 
                switch (selection) {
                    // $script:1127164207009324$
                    // - Where's the real Zakum?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1127164207009325$ 
                // - Not happy with Little Zakum? That's fine. You can find the real deal at the Mirror Gate. Just check your Challenge Map!  
                return true;
            case 30:
                // $script:1130102607009374$ 
                // - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you! 
                switch (selection) {
                    // $script:1130104707009376$
                    // - Oh, oh, what is it?
                    case 0:
                        Id = 0; // TODO: 31 | 32
                        return false;
                }
                return true;
            case 31:
                // $script:1130104707009377$ functionID=1 
                // - You've got to open it to find out! I hope you like this gift to you from me, Little Zakum. 
                return true;
            case 32:
                // $script:1204155907009629$ 
                // - You've got to open it to find out! But, uh, it looks like you don't have enough room in your bag. Come back when you're ready for a gift from yours truly, Little Zakum! 
                return true;
            case 40:
                // $script:1130102607009375$ 
                // - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you, and... Hey, I already gave you a gift! You cheeky hero, you. 
                return true;
            default:
                return true;
        }
    }
}
