using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004304: Ghost
/// </summary>
public class _11004304 : NpcScript {
    internal _11004304(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011434$ 
                // - Can you see me?
                return true;
            case 30:
                // $script:1002141907011437$ 
                // - I guess living people really can see ghosts on Halloween.
                // $script:1002141907011438$ 
                // - Please don't ask me if I saw anything...
                switch (selection) {
                    // $script:1002141907011439$
                    // - Did you see anything?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011440$ 
                // - N-no! I don't want <i>that woman</i> coming after me, so the answer is no!
                return true;
            default:
                return true;
        }
    }
}
