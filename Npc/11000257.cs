using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000257: Douglas
/// </summary>
public class _11000257 : NpcScript {
    internal _11000257(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000408$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:0831180610000413$ functionID=1 
                // - Being strong is important, but looking fabulous while you fight is the true key to happiness, y'know. So... wanna spruce up your gear?
                switch (selection) {
                    // $script:0831180610000414$
                    // - Yes! I need more color in my life!
                    case 0:
                        Id = 0;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
