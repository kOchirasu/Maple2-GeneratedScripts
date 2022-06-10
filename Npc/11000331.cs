using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000331: Brandon
/// </summary>
public class _11000331 : NpcScript {
    internal _11000331(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001339$ 
                // - Can I help you? 
                return true;
            case 20:
                // $script:0831180407001341$ 
                // - Hm... Have you ever felt like you're being watched? You get this itchy feeling on the back of your neck when that happens. I've been feeling it a lot lately. Why do you think that is? 
                return true;
            case 30:
                // $script:0831180407001342$ 
                // - Excuse me, have you seen a girl around here who looks like me? She has blond hair and blue eyes, just like I do. I don't remember what she was wearing, though. 
                // $script:0831180407001343$ 
                // - She's my sister. She went to do her hair and never came back. Does it take women a long time to do their hair? Huh... maybe she was getting it dyed. 
                return true;
            default:
                return true;
        }
    }
}
