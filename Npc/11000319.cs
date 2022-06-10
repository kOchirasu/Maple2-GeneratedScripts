using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000319: Shinby
/// </summary>
public class _11000319 : NpcScript {
    internal _11000319(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001238$ 
                // - Can I help you?
                return true;
            case 50:
                // $script:0831180407001243$ 
                // - Nice to meet you. I'm $npcName:11000319[gender:1]$. What's your name?
                switch (selection) {
                    // $script:0831180407001244$
                    // - I'm $MyPCName$.
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407001245$
                    // - It's a secret.
                    case 1:
                        Id = 52;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407001246$ 
                // - $MyPCName$? Ah, what a beautiful name!
                return true;
            case 52:
                // $script:0831180407001247$ 
                // - You don't have to tell me. It's $MyPCName$, right?
                switch (selection) {
                    // $script:0831180407001248$
                    // - How do you know that?
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:0831180407001249$ 
                // - It's a secret. Ho, ho!
                return true;
            default:
                return true;
        }
    }
}
