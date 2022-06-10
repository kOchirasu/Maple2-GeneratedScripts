using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001241: Minok
/// </summary>
public class _11001241 : NpcScript {
    internal _11001241(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123214707004450$ 
                // - Sigh...
                return true;
            case 30:
                // $script:1123214707004453$ 
                // - Agh... I'm so disappointed in myself! I can barely get anywhere in the $map:2000350$... and it's all because of those stupid $item:90000014$.
                switch (selection) {
                    // $script:1123214707004454$
                    // - Why are you so eager to be here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1123214707004455$ 
                // - Because everything is... <i>wrong</i>! This spreading darkness is turning our world cold and evil. So many fairies have already fallen trying to stem the tide, and I have to do my part too!
                switch (selection) {
                    // $script:1123214707004456$
                    // - You should leave this work to someone else.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1123214707004457$ 
                // - What? You think I can't do it just 'cause I'm fairfolk? What makes you so special? Typical human arrogance!
                // $script:1123214707004458$ 
                // - The fairies have kept the darkness from touching Maple World since before you were in diapers. We never ask for anything in return, either. And what do we get for our troubles? The disdain of humans. Pah!
                return true;
            default:
                return true;
        }
    }
}
