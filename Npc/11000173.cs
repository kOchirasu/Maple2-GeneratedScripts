using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000173: Ralph
/// </summary>
public class _11000173 : NpcScript {
    internal _11000173(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000723$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407000726$ 
                // - Everyone acts as if they're the purest, noblest people in the world, but on the inside, we're all equally rotten. Hey, $MyPCName$! Live your life the way you want. Don't let anyone tell you what to do! 
                return true;
            case 40:
                // $script:0831180407000727$ 
                // - Your youthful recklessness will be your undoing. Search $map:02000141$ if you can. I very much doubt you'll return alive.  
                return true;
            default:
                return true;
        }
    }
}
