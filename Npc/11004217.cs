using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004217: Jenna
/// </summary>
public class _11004217 : NpcScript {
    internal _11004217(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010773$ 
                // - Do you have business with me?
                return true;
            case 10:
                // $script:0806222707010774$ 
                // - Haha, let's get this party started! Pew pew! That's the sound of me blowing everyone away with the power of my cannon!
                return true;
            case 20:
                // $script:0806222707010775$ 
                // - If you want to be happy, there's one rule to live by: figure out what you wanna do, and do it! In my case, that's listening my cannon purr as it pumps out hundreds of rounds a minute.
                return true;
            default:
                return true;
        }
    }
}
