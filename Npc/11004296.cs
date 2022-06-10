using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004296: Ghost
/// </summary>
public class _11004296 : NpcScript {
    internal _11004296(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011366$ 
                // - How lovely!
                return true;
            case 30:
                // $script:1002141907011369$ 
                // - Tell me, what's the one thing you must never, ever forget when you travel?
                switch (selection) {
                    // $script:1002141907011370$
                    // - Your wallet, of course.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1002141907011371$
                    // - You can't travel without a suitcase.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011372$ 
                // - Oh! I suppose your wallet <i>is</i> important. But is it the most important? Think harder!
                switch (selection) {
                    // $script:1002141907011373$
                    // - You can't travel without a suitcase.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1002141907011374$ 
                // - That's right! All of your most important things go in your suitcase, after all. If you're looking for something, you should always check your suitcase first.
                return true;
            default:
                return true;
        }
    }
}
