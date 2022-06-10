using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000185: Ms. Kim
/// </summary>
public class _11000185 : NpcScript {
    internal _11000185(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000773$ 
                // - Can I help you? 
                return true;
            case 50:
                // $script:0831180407000778$ 
                // - $map:2000123$. How may I help you? 
                switch (selection) {
                    // $script:0831180407000781$
                    // - What's been happening lately?
                    case 0:
                        Id = 53;
                        return false;
                    // $script:0831180407000782$
                    // - I was wondering how you're doing.
                    case 1:
                        Id = 54;
                        return false;
                }
                return true;
            case 53:
                // $script:0831180407000799$ 
                // - You mean the news? If I had good information, do you think I'd share it with you? 
                // $script:0831180407000800$ 
                // - Well, I would. Instead of seeking immediate gains, I invest for the future. That's my philosophy. 
                // $script:0831180407000801$ 
                // - Money or trust... which do you think is better for me in the long run? Heh, I'm still weighing my options. 
                return true;
            case 54:
                // $script:0831180407000805$ 
                // - What is this? Are you hitting on me? I'm sorry, but I don't answer questions that have nothing to do with my work. 
                // $script:0831180407000806$ 
                // - I'm aware of the rumors about me. One of them says I'm divorced. Another says I'm a widow.  
                // $script:0831180407000807$ 
                // - Some even say I'm the only daughter of Chairman Goldus. Ha, geez... 
                // $script:0831180407000808$ 
                // - I refuse to be gossip fodder. Don't these people have anything better to do with their lives? 
                // $script:0831180407000809$ 
                // - I'm sorry... I got carried away for a moment. Now, if you'll excuse me, I have developments to inspect. 
                return true;
            default:
                return true;
        }
    }
}
