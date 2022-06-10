using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000960: Krin
/// </summary>
public class _11000960 : NpcScript {
    internal _11000960(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003325$ 
                // - Kyaaaaah! What? What?! 
                return true;
            case 20:
                // $script:0831180407003327$ 
                // - Wah! What are you doing? Don't you know how to knock?! 
                switch (selection) {
                    // $script:0831180407003328$
                    // - I didn't know someone was in here.
                    case 0:
                        Id = 0; // TODO: 21,22,23,24,25,26,27,28,29,30 | 
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407003329$ functionID=1 
                // - Get out of here! Oh, and take this with you. 
                return true;
            case 22:
                // $script:0831180407003330$ 
                // - What are you doing? OUT! 
                return true;
            case 23:
                // $script:0831180407003331$ 
                // - What are you doing? OUT! 
                return true;
            case 24:
                // $script:0831180407003332$ 
                // - What are you doing? OUT! 
                return true;
            case 25:
                // $script:0831180407003333$ 
                // - What is this? I can't focus... 
                return true;
            case 26:
                // $script:0831180407003334$ 
                // - What is this? I can't focus... 
                return true;
            case 27:
                // $script:0831180407003335$ 
                // - What is this? I can't focus... 
                return true;
            case 28:
                // $script:0831180407003336$ 
                // - Ah, I was about to leave... 
                return true;
            case 29:
                // $script:0831180407003337$ 
                // - Ah, I was about to leave... 
                return true;
            case 30:
                // $script:0831180407003338$ 
                // - Ah, I was about to leave... 
                return true;
            default:
                return true;
        }
    }
}
